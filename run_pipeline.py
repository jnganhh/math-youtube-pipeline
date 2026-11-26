"""
run_pipeline.py
End-to-end orchestrator:
Produces 1 or 4 daily MPM2D math videos (~2:30, white & light theme), verifies each with ffprobe,
and uploads them to YouTube scheduled for 5:30 PM, 7:30 PM, 8:30 PM, and 10:00 PM (America/Toronto).
"""

import argparse
import fcntl
import json
import os
import subprocess
from pathlib import Path
from uuid import uuid4

from generate_math_video import generate_math_video, select_topic, topic_bank
from verify_video import verify_video
from upload_youtube import load_credentials, upload_video, get_publish_at_iso, DEFAULT_TOKEN_PATH


def main() -> None:
    parser = argparse.ArgumentParser(description="Run MPM2D Math YouTube pipeline.")
    parser.add_argument("--topic-id", default=None, help="Specific topic or proof ID")
    parser.add_argument("--mode", choices=("lesson", "visual_proof", "mixed"), default="lesson")
    parser.add_argument(
        "--output-dir",
        default="/content/drive/MyDrive/MathYouTube",
        help="Directory for rendered .mp4 files",
    )
    parser.add_argument("--token", default=DEFAULT_TOKEN_PATH, help="Path to YouTube OAuth token.json")
    parser.add_argument("--batch", type=int, default=4, help="Number of videos to produce & schedule (default: 4)")
    parser.add_argument("--tz", default="America/Toronto", help="Timezone for 5:30/7:30/8:30/10:00 PM slots")
    parser.add_argument("--landscape", action="store_true", help="Render 1920x1080 instead of 1080x1920")
    parser.add_argument("--skip-upload", action="store_true", help="Skip YouTube upload (local test)")
    parser.add_argument("--history", type=Path, default=Path("published_history.json"),
                        help="Shared publication history file")
    parser.add_argument("--sync-history", action="store_true",
                        help="Checkpoint history to the publication-history Git branch (CI)")
    args = parser.parse_args()
    if args.topic_id and args.batch != 1:
        parser.error("--topic-id requires --batch 1")
    if args.landscape and args.mode != "lesson":
        parser.error("--landscape is only supported in lesson mode")
    if args.batch < 1:
        parser.error("--batch must be positive")
    args.history = args.history.resolve()
    args.history.parent.mkdir(parents=True, exist_ok=True)
    with args.history.with_suffix(".lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        run_batch(args)


def checkpoint(args, state):
    history = args.history
    tmp = history.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    tmp.replace(history)
    if args.sync_history:
        for command in (["add", "--", history.name],
                        ["commit", "-m", "Checkpoint MPM2D publication history", "--", history.name],
                        ["push", "origin", "HEAD:refs/heads/publication-history"]):
            subprocess.run(["git", *command], cwd=history.parent, check=True)


def run_batch(args):
    state = (json.loads(args.history.read_text(encoding="utf-8")) if args.history.exists()
             else {"cycle": 1, "published": [], "pending": None})
    if state["pending"] and not args.skip_upload:
        raise RuntimeError(
            f"Verify the pending upload in YouTube Studio: {state['pending']}. "
            "If uploaded, append its topic ID to published. Clear pending after checking "
            "and save the corrected history before restarting."
        )
    os.makedirs(args.output_dir, exist_ok=True)
    is_short = not args.landscape
    bank = {topic["id"] for topic in topic_bank(args.mode)}

    for slot in range(args.batch):
        print(f"\n=== Video {slot + 1}/{args.batch} ===")
        out_mp4 = os.path.join(args.output_dir, f"mpm2d_slot_{slot + 1}.mp4")

        if bank.issubset(state["published"]):
            state.update(cycle=state["cycle"] + 1,
                         published=[topic_id for topic_id in state["published"] if topic_id not in bank])
        seen = () if args.skip_upload and args.topic_id else state["published"]
        # Give the first daily slot to a proof while one is available in the shared cycle.
        prefer_proof = (slot == 0 and args.mode == "mixed" and not args.topic_id
                        and any(proof["id"] not in seen for proof in topic_bank("visual_proof")))
        topic = select_topic("visual_proof" if prefer_proof else args.mode,
                             args.topic_id, published=seen)
        gen_result = generate_math_video(
            output_mp4=out_mp4,
            topic_id=topic["id"],
            is_short=is_short,
            mode=args.mode,
        )
        video_path = gen_result["output_mp4"]
        topic_title = gen_result["topic"]["title"]

        print("Verifying rendered video...")
        info = verify_video(video_path)
        print("Verification passed:", json.dumps(info, indent=2))

        if args.skip_upload:
            print("Skipping YouTube upload (--skip-upload set).")
            state["published"].append(topic["id"])
            continue

        publish_at = get_publish_at_iso(slot_index=slot, tz_name=args.tz)
        credentials = load_credentials(args.token)
        # A timeout after YouTube accepts a video must never trigger a blind retry.
        state["pending"] = {"topic": topic["id"], "publish_at": publish_at,
                            "attempt": uuid4().hex}
        checkpoint(args, state)
        studio_url = upload_video(
            video_path=video_path,
            topic=topic_title,
            token_path=args.token,
            creds=credentials,
            is_short=is_short,
            publish_at=publish_at,
            curricula=topic.get("curricula"),
        )
        state["published"].append(topic["id"])
        state["pending"] = None
        checkpoint(args, state)
        print(f"Scheduled slot {slot + 1} ({publish_at}): {studio_url}")


if __name__ == "__main__":
    main()

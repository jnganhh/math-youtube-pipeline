"""
run_pipeline.py
End-to-end orchestrator:
Produces 1 or 4 daily MPM2D math videos (~2:30, white & light theme), verifies each with ffprobe,
and uploads them to YouTube scheduled for 5:30 PM, 7:30 PM, 8:30 PM, and 10:00 PM (America/Toronto).
"""

import argparse
import json
import os

from generate_math_video import generate_math_video
from verify_video import verify_video
from upload_youtube import upload_video, get_publish_at_iso, DEFAULT_TOKEN_PATH


def main() -> None:
    parser = argparse.ArgumentParser(description="Run MPM2D Math YouTube pipeline.")
    parser.add_argument("--topic-id", default=None, help="Specific MPM2D topic ID (optional)")
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
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    is_short = not args.landscape

    for slot in range(args.batch):
        print(f"\n=== Video {slot + 1}/{args.batch} ===")
        out_mp4 = os.path.join(args.output_dir, f"mpm2d_slot_{slot + 1}.mp4")

        gen_result = generate_math_video(
            output_mp4=out_mp4,
            topic_id=args.topic_id if args.batch == 1 else None,
            offset=slot,
            is_short=is_short,
        )
        video_path = gen_result["output_mp4"]
        topic_title = gen_result["topic"]["title"]

        print("Verifying rendered video...")
        info = verify_video(video_path)
        print("Verification passed:", json.dumps(info, indent=2))

        if args.skip_upload:
            print("Skipping YouTube upload (--skip-upload set).")
            continue

        publish_at = get_publish_at_iso(slot_index=slot, tz_name=args.tz)
        studio_url = upload_video(
            video_path=video_path,
            topic=topic_title,
            token_path=args.token,
            is_short=is_short,
            publish_at=publish_at,
        )
        print(f"Scheduled slot {slot + 1} ({publish_at}): {studio_url}")


if __name__ == "__main__":
    main()

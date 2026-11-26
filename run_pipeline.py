"""
run_pipeline.py
End-to-end orchestrator:
1. Generate math educational video (Manim + edge-tts + ffmpeg)
2. Verify .mp4 exists, has non-zero duration, and has an audio track
3. Upload to YouTube as a PRIVATE draft and print the YouTube Studio link
"""

import argparse
import json
import os

from generate_math_video import generate_math_video
from verify_video import verify_video
from upload_youtube import upload_video, DEFAULT_TOKEN_PATH


def main() -> None:
    parser = argparse.ArgumentParser(description="Run end-to-end Math YouTube pipeline.")
    parser.add_argument(
        "--topic",
        default="Visual proof of completing the square for quadratics",
        help="Math topic",
    )
    parser.add_argument(
        "--output",
        default="/content/drive/MyDrive/MathYouTube/completing_the_square.mp4",
        help="Output .mp4 path",
    )
    parser.add_argument(
        "--token",
        default=DEFAULT_TOKEN_PATH,
        help="Path to YouTube OAuth token.json",
    )
    parser.add_argument("--landscape", action="store_true", help="Render 1920x1080 instead of 1080x1920")
    parser.add_argument("--skip-upload", action="store_true", help="Skip YouTube upload (local test)")
    args = parser.parse_args()

    is_short = not args.landscape

    # Step 1: Generate video
    video_path = generate_math_video(
        output_mp4=args.output,
        topic=args.topic,
        is_short=is_short,
    )

    # Step 2: Verify video before calling YouTube API
    print("Verifying rendered video...")
    info = verify_video(video_path)
    print("Verification passed:", json.dumps(info, indent=2))

    # Step 3: Upload as PRIVATE draft
    if args.skip_upload:
        print("Skipping YouTube upload (--skip-upload set).")
        return

    studio_url = upload_video(
        video_path=video_path,
        topic=args.topic,
        token_path=args.token,
        is_short=is_short,
    )
    print(f"\nDone! Review your private draft at:\n{studio_url}")


if __name__ == "__main__":
    main()

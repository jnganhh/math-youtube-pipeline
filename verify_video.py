"""
verify_video.py
Verifies that a rendered .mp4 file exists, has non-zero duration,
and contains both video and audio tracks using ffprobe.
"""

import json
import os
import subprocess
import sys
from typing import Dict, Any


def verify_video(video_path: str) -> Dict[str, Any]:
    """
    Verify that `video_path` exists, has duration > 0, and has an audio track.
    Raises FileNotFoundError or ValueError on failure.
    Returns a dict with duration, width, height, and audio_codec.
    """
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"Rendered video not found: {video_path}")

    if os.path.getsize(video_path) == 0:
        raise ValueError(f"Rendered video file is empty (0 bytes): {video_path}")

    cmd = [
        "ffprobe",
        "-v", "quiet",
        "-print_format", "json",
        "-show_format",
        "-show_streams",
        video_path,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"ffprobe failed on {video_path}: {result.stderr}")

    probe = json.loads(result.stdout)
    streams = probe.get("streams", [])
    fmt = probe.get("format", {})

    duration = float(fmt.get("duration", 0.0))
    if duration <= 0.0:
        raise ValueError(f"Video duration must be > 0, got {duration}s")

    video_streams = [s for s in streams if s.get("codec_type") == "video"]
    audio_streams = [s for s in streams if s.get("codec_type") == "audio"]

    if not video_streams:
        raise ValueError(f"No video stream found in {video_path}")
    if not audio_streams:
        raise ValueError(f"No audio stream found in {video_path}")

    return {
        "path": video_path,
        "duration_sec": round(duration, 2),
        "width": video_streams[0].get("width"),
        "height": video_streams[0].get("height"),
        "video_codec": video_streams[0].get("codec_name"),
        "audio_codec": audio_streams[0].get("codec_name"),
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python verify_video.py <path_to_mp4>")
        sys.exit(1)
    info = verify_video(sys.argv[1])
    print("Verification passed:", json.dumps(info, indent=2))

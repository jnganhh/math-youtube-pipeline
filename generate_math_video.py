"""
generate_math_video.py
Generates a short math educational video (1080x1920 vertical Shorts or 1920x1080 landscape)
using Manim for step-by-step math animations, edge-tts for voiceover, and ffmpeg for muxing.
"""

import argparse
import asyncio
import json
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, Any, Optional

from mpm2d_topics import pick_topic


SCENE_SCRIPT_TEMPLATE = '''
import json
from manim import *

TOPIC_DATA = json.loads(r"""__TOPIC_JSON__""")

class MPM2DTopicScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f172a"
        max_w = 4.0 if self.camera.frame_width < 6 else 11.0

        # Top zone: Title
        title = Text(TOPIC_DATA["title"], font_size=34, color=WHITE, weight=BOLD)
        if title.width > max_w:
            title.set(width=max_w)
        subtitle = Text("MPM2D Quadratics", font_size=24, color="#38bdf8")
        header = VGroup(title, subtitle).arrange(DOWN, buff=0.14).to_edge(UP, buff=0.55)

        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.15), run_time=1.8)
        self.wait(0.8)

        # Middle zone: Step-by-step cards (non-overlapping vertical stack)
        steps = TOPIC_DATA["steps"]
        step_groups = []
        for label, tex, color in steps:
            lbl = Text(label, font_size=24, color="#94a3b8")
            if lbl.width > max_w:
                lbl.set(width=max_w)
            eq = MathTex(tex, font_size=40, color=color)
            if eq.width > max_w:
                eq.set(width=max_w)
            grp = VGroup(lbl, eq).arrange(DOWN, buff=0.16)
            step_groups.append(grp)

        stack = VGroup(*step_groups).arrange(DOWN, buff=0.45)
        stack.next_to(header, DOWN, buff=0.55)

        # Ensure stack fits above bottom margin
        available_h = (header.get_bottom()[1] - 0.55) - (-self.camera.frame_height / 2 + 0.6)
        if stack.height > available_h:
            stack.set(height=available_h)
            stack.next_to(header, DOWN, buff=0.45)

        for grp in step_groups:
            self.play(FadeIn(grp[0], shift=UP * 0.1), Write(grp[1]), run_time=1.8)
            self.wait(1.6)

        self.wait(3.0)
'''


async def _generate_tts(text: str, output_mp3: str, voice: str = "en-US-AriaNeural") -> None:
    import edge_tts

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_mp3)


def generate_voiceover(output_mp3: str, script_text: str) -> str:
    """Generate voiceover MP3 using edge-tts."""
    asyncio.run(_generate_tts(script_text, output_mp3))
    if not os.path.isfile(output_mp3) or os.path.getsize(output_mp3) == 0:
        raise RuntimeError(f"Failed to generate voiceover audio at {output_mp3}")
    return output_mp3


def render_manim_video(
    output_dir: str,
    topic_data: Dict[str, Any],
    is_short: bool = True,
) -> str:
    """Render the Manim scene to an MP4 file and return its path."""
    os.makedirs(output_dir, exist_ok=True)
    scene_file = os.path.join(output_dir, "scene_mpm2d.py")
    scene_code = SCENE_SCRIPT_TEMPLATE.replace("__TOPIC_JSON__", json.dumps(topic_data))
    with open(scene_file, "w", encoding="utf-8") as f:
        f.write(scene_code)

    resolution = "1080,1920" if is_short else "1920,1080"
    cmd = [
        "manim",
        "-qh",
        "--resolution", resolution,
        "--media_dir", os.path.join(output_dir, "media"),
        scene_file,
        "MPM2DTopicScene",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"Manim render failed:\n{result.stderr}\n{result.stdout}")

    media_root = Path(output_dir) / "media" / "videos"
    mp4_files = list(media_root.rglob("MPM2DTopicScene.mp4"))
    if not mp4_files:
        raise FileNotFoundError(f"Could not find rendered Manim MP4 under {media_root}")
    return str(mp4_files[0])


def mux_audio_video(video_path: str, audio_path: str, output_mp4: str) -> str:
    """Mux video and audio using ffmpeg, ensuring both streams are present."""
    os.makedirs(os.path.dirname(os.path.abspath(output_mp4)), exist_ok=True)
    cmd = [
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        output_mp4,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg mux failed:\n{result.stderr}")
    return output_mp4


def generate_math_video(
    output_mp4: str,
    topic_id: Optional[str] = None,
    is_short: bool = True,
) -> Dict[str, Any]:
    """End-to-end content generation: pick MPM2D topic + Manim + edge-tts + ffmpeg mux."""
    topic_data = pick_topic(topic_id)
    print(f"Selected MPM2D topic [{topic_data['id']}]: {topic_data['title']}")
    print(f"Format: {'1080x1920 (YouTube Shorts)' if is_short else '1920x1080 (Landscape)'}")

    with tempfile.TemporaryDirectory() as tmpdir:
        raw_video = render_manim_video(tmpdir, topic_data, is_short=is_short)
        voice_mp3 = os.path.join(tmpdir, "voiceover.mp3")
        generate_voiceover(voice_mp3, topic_data["voiceover"])
        mux_audio_video(raw_video, voice_mp3, output_mp4)

    print(f"Final video saved to: {output_mp4}")
    return {"output_mp4": output_mp4, "topic": topic_data}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an MPM2D math educational video.")
    parser.add_argument(
        "--output",
        default="/content/drive/MyDrive/MathYouTube/mpm2d_short.mp4",
        help="Output .mp4 path",
    )
    parser.add_argument("--topic-id", default=None, help="Specific MPM2D topic ID (optional)")
    parser.add_argument("--landscape", action="store_true", help="Render 1920x1080 instead of 1080x1920")
    args = parser.parse_args()

    generate_math_video(
        output_mp4=args.output,
        topic_id=args.topic_id,
        is_short=not args.landscape,
    )

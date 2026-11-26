"""
generate_math_video.py
Generates a ~2:30 (150s) MPM2D math educational video in a clean WHITE & LIGHT theme
(1080x1920 vertical or 1920x1080 landscape) using Manim, edge-tts, and ffmpeg.
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
TARGET_DURATION = 150.0  # ~2:30 target video length in seconds

class MPM2DTopicScene(Scene):
    def construct(self):
        self.camera.background_color = "#ffffff"
        max_w = 4.0 if self.camera.frame_width < 6 else 11.0
        elapsed = 0.0

        # Light header banner
        title = Text(TOPIC_DATA["title"], font_size=34, color="#0f172a", weight=BOLD)
        if title.width > max_w:
            title.set(width=max_w)
        subtitle = Text("MPM2D • Grade 10 Academic Math", font_size=22, color="#2563eb")
        header = VGroup(title, subtitle).arrange(DOWN, buff=0.12).to_edge(UP, buff=0.45)

        rule_box = RoundedRectangle(
            corner_radius=0.15,
            width=max_w + 0.3,
            height=0.95,
            color="#cbd5e1",
            fill_color="#f1f5f9",
            fill_opacity=1.0,
            stroke_width=2,
        )
        rule_tex = MathTex(TOPIC_DATA["rule"], font_size=30, color="#1e293b")
        if rule_tex.width > max_w - 0.15:
            rule_tex.set(width=max_w - 0.15)
        rule_tex.move_to(rule_box.get_center())
        rule_card = VGroup(rule_box, rule_tex).next_to(header, DOWN, buff=0.35)

        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.1), run_time=2.0)
        self.play(FadeIn(rule_card, shift=UP * 0.1), run_time=1.8)
        self.wait(6.0)
        elapsed += 9.8

        # Part 1: Worked Example
        steps = TOPIC_DATA["steps"]
        step_groups = []
        for label, tex, color in steps:
            lbl = Text(label, font_size=22, color="#475569", weight=BOLD)
            if lbl.width > max_w:
                lbl.set(width=max_w)
            eq = MathTex(tex, font_size=38, color=color)
            if eq.width > max_w:
                eq.set(width=max_w)
            grp = VGroup(lbl, eq).arrange(DOWN, buff=0.12)
            step_groups.append(grp)

        stack1 = VGroup(*step_groups).arrange(DOWN, buff=0.38).next_to(rule_card, DOWN, buff=0.45)
        avail_h = (rule_card.get_bottom()[1] - 0.45) - (-self.camera.frame_height / 2 + 0.6)
        if stack1.height > avail_h:
            stack1.set(height=avail_h)
            stack1.next_to(rule_card, DOWN, buff=0.4)

        for grp in step_groups:
            self.play(FadeIn(grp[0], shift=UP * 0.1), Write(grp[1]), run_time=2.5)
            self.wait(11.5)
            elapsed += 14.0

        # Transition to Practice Problem
        self.play(FadeOut(stack1), run_time=1.2)
        elapsed += 1.2

        # Part 2: Practice Problem ("Try It Yourself")
        practice = TOPIC_DATA["practice"]
        prac_groups = []
        for label, tex, color in practice:
            lbl = Text(label, font_size=24, color="#2563eb", weight=BOLD)
            if lbl.width > max_w:
                lbl.set(width=max_w)
            eq = MathTex(tex, font_size=40, color=color)
            if eq.width > max_w:
                eq.set(width=max_w)
            grp = VGroup(lbl, eq).arrange(DOWN, buff=0.14)
            prac_groups.append(grp)

        stack2 = VGroup(*prac_groups).arrange(DOWN, buff=0.48).next_to(rule_card, DOWN, buff=0.55)
        if stack2.height > avail_h:
            stack2.set(height=avail_h)
            stack2.next_to(rule_card, DOWN, buff=0.45)

        for idx, grp in enumerate(prac_groups):
            self.play(FadeIn(grp[0], shift=UP * 0.1), Write(grp[1]), run_time=2.5)
            wait_t = 16.0 if idx == 0 else 12.0
            self.wait(wait_t)
            elapsed += 2.5 + wait_t

        # Pad remaining time to reach ~150s (2:30)
        remaining = max(3.0, TARGET_DURATION - elapsed)
        self.wait(remaining)
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
    """Mux video and audio using ffmpeg without cutting off the longer stream."""
    os.makedirs(os.path.dirname(os.path.abspath(output_mp4)), exist_ok=True)
    cmd = [
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        output_mp4,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg mux failed:\n{result.stderr}")
    return output_mp4


def generate_math_video(
    output_mp4: str,
    topic_id: Optional[str] = None,
    offset: int = 0,
    is_short: bool = True,
) -> Dict[str, Any]:
    """End-to-end content generation: pick MPM2D topic + Manim + edge-tts + ffmpeg mux."""
    topic_data = pick_topic(topic_id, offset=offset)
    print(f"Selected MPM2D topic [{topic_data['id']}]: {topic_data['title']}")
    print(f"Theme: White & Light | Target length: ~2:30 | Format: {'1080x1920' if is_short else '1920x1080'}")

    with tempfile.TemporaryDirectory() as tmpdir:
        raw_video = render_manim_video(tmpdir, topic_data, is_short=is_short)
        voice_mp3 = os.path.join(tmpdir, "voiceover.mp3")
        generate_voiceover(voice_mp3, topic_data["voiceover"])
        mux_audio_video(raw_video, voice_mp3, output_mp4)

    print(f"Final video saved to: {output_mp4}")
    return {"output_mp4": output_mp4, "topic": topic_data}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a 2:30 light-theme MPM2D math video.")
    parser.add_argument(
        "--output",
        default="/content/drive/MyDrive/MathYouTube/mpm2d_lesson.mp4",
        help="Output .mp4 path",
    )
    parser.add_argument("--topic-id", default=None, help="Specific MPM2D topic ID (optional)")
    parser.add_argument("--offset", type=int, default=0, help="Topic rotation offset (0..3)")
    parser.add_argument("--landscape", action="store_true", help="Render 1920x1080 instead of 1080x1920")
    args = parser.parse_args()

    generate_math_video(
        output_mp4=args.output,
        topic_id=args.topic_id,
        offset=args.offset,
        is_short=not args.landscape,
    )

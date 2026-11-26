"""
generate_math_video.py
Generates a short math educational video (1080x1920 vertical Shorts or 1920x1080 landscape)
using Manim for step-by-step math animations, edge-tts for voiceover, and ffmpeg for muxing.
"""

import argparse
import asyncio
import os
import subprocess
import tempfile
from pathlib import Path


VOICEOVER_SCRIPT = (
    "Ever wondered why completing the square actually works? "
    "Let's see it visually. "
    "Start with x squared plus b x. "
    "x squared is just a square with side length x. "
    "And b x is a rectangle with width b and height x. "
    "Now, split that rectangle into two equal halves, each of width b over 2. "
    "Move one half to the bottom of the square. "
    "Look! We almost have a bigger square of side x plus b over 2. "
    "All that's missing is a tiny corner square of area b over 2, squared. "
    "Add that missing corner to complete the square, and subtract it to keep the equation balanced. "
    "And that's why x squared plus b x equals x plus b over 2 squared, minus b over 2 squared!"
)


MANIM_SCENE_TEMPLATE = '''
from manim import *

class CompletingTheSquareScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f172a"

        # Title
        title = Text("Completing the Square", font_size=44, color=WHITE, weight=BOLD)
        subtitle = Text("Visual Proof", font_size=30, color="#38bdf8")
        header = VGroup(title, subtitle).arrange(DOWN, buff=0.18).to_edge(UP, buff=0.7)

        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.2), run_time=2.0)
        self.wait(1.5)

        # Step 1: Initial expression
        eq1 = MathTex("x^2", "+", "bx", font_size=52, color=WHITE)
        eq1.next_to(header, DOWN, buff=0.6)
        self.play(Write(eq1), run_time=1.8)
        self.wait(1.5)

        # Step 2: x^2 square + bx rectangle
        sq_x = Square(side_length=2.2, color="#38bdf8", fill_color="#0284c7", fill_opacity=0.45)
        lbl_x2 = MathTex("x^2", font_size=40, color=WHITE).move_to(sq_x.get_center())
        lbl_x_left = MathTex("x", font_size=32, color="#94a3b8").next_to(sq_x, LEFT, buff=0.2)
        lbl_x_top = MathTex("x", font_size=32, color="#94a3b8").next_to(sq_x, UP, buff=0.2)
        group_x2 = VGroup(sq_x, lbl_x2, lbl_x_left, lbl_x_top)

        rect_bx = Rectangle(width=1.4, height=2.2, color="#34d399", fill_color="#059669", fill_opacity=0.45)
        rect_bx.next_to(sq_x, RIGHT, buff=0.25)
        lbl_bx = MathTex("bx", font_size=40, color=WHITE).move_to(rect_bx.get_center())
        lbl_b_top = MathTex("b", font_size=32, color="#94a3b8").next_to(rect_bx, UP, buff=0.2)
        group_bx = VGroup(rect_bx, lbl_bx, lbl_b_top)

        shapes_step1 = VGroup(group_x2, group_bx).move_to(ORIGIN).shift(DOWN * 0.3)

        self.play(Create(sq_x), Write(lbl_x2), FadeIn(lbl_x_left), FadeIn(lbl_x_top), run_time=2.2)
        self.wait(1.2)
        self.play(Create(rect_bx), Write(lbl_bx), FadeIn(lbl_b_top), run_time=2.2)
        self.wait(2.0)

        # Step 3: Split bx into two (b/2)x rectangles
        half_w = 0.7
        rect_r = Rectangle(width=half_w, height=2.2, color="#34d399", fill_color="#059669", fill_opacity=0.45)
        rect_r.next_to(sq_x, RIGHT, buff=0.05)
        lbl_r = MathTex(r"\\frac{b}{2}x", font_size=28, color=WHITE).move_to(rect_r.get_center())
        lbl_r_top = MathTex(r"\\frac{b}{2}", font_size=26, color="#94a3b8").next_to(rect_r, UP, buff=0.2)

        rect_b = Rectangle(width=2.2, height=half_w, color="#34d399", fill_color="#059669", fill_opacity=0.45)
        rect_b.next_to(sq_x, DOWN, buff=0.05)
        lbl_b = MathTex(r"\\frac{b}{2}x", font_size=28, color=WHITE).move_to(rect_b.get_center())
        lbl_b_left = MathTex(r"\\frac{b}{2}", font_size=26, color="#94a3b8").next_to(rect_b, LEFT, buff=0.2)

        self.play(
            FadeOut(group_bx),
            FadeIn(rect_r), FadeIn(lbl_r), FadeIn(lbl_r_top),
            run_time=1.8,
        )
        self.wait(1.2)
        self.play(
            FadeIn(rect_b), FadeIn(lbl_b), FadeIn(lbl_b_left),
            run_time=2.2,
        )
        self.wait(2.5)

        # Step 4: Missing corner (b/2)^2
        corner = Square(side_length=half_w, color="#fbbf24", fill_color="#d97706", fill_opacity=0.55)
        corner.next_to(rect_r, DOWN, buff=0.05)
        lbl_corner = MathTex(r"\\left(\\frac{b}{2}\\right)^2", font_size=20, color=WHITE).move_to(corner.get_center())

        self.play(Create(corner), Write(lbl_corner), run_time=2.2)
        self.wait(2.5)

        # Step 5: Final equation
        eq_final = MathTex(
            r"x^2 + bx = \\left(x + \\frac{b}{2}\\right)^2 - \\left(\\frac{b}{2}\\right)^2",
            font_size=36,
            color="#fbbf24",
        ).to_edge(DOWN, buff=1.1)

        self.play(ReplacementTransform(eq1, eq_final), run_time=2.5)
        self.wait(4.0)
'''


async def _generate_tts(text: str, output_mp3: str, voice: str = "en-US-AriaNeural") -> None:
    import edge_tts

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_mp3)


def generate_voiceover(output_mp3: str, script_text: str = VOICEOVER_SCRIPT) -> str:
    """Generate voiceover MP3 using edge-tts."""
    asyncio.run(_generate_tts(script_text, output_mp3))
    if not os.path.isfile(output_mp3) or os.path.getsize(output_mp3) == 0:
        raise RuntimeError(f"Failed to generate voiceover audio at {output_mp3}")
    return output_mp3


def render_manim_video(
    output_dir: str,
    is_short: bool = True,
) -> str:
    """Render the Manim scene to an MP4 file and return its path."""
    os.makedirs(output_dir, exist_ok=True)
    scene_file = os.path.join(output_dir, "scene_completing_square.py")
    with open(scene_file, "w", encoding="utf-8") as f:
        f.write(MANIM_SCENE_TEMPLATE)

    resolution = "1080,1920" if is_short else "1920,1080"
    cmd = [
        "manim",
        "-qh",
        "--resolution", resolution,
        "--media_dir", os.path.join(output_dir, "media"),
        scene_file,
        "CompletingTheSquareScene",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"Manim render failed:\n{result.stderr}\n{result.stdout}")

    # Locate rendered mp4
    media_root = Path(output_dir) / "media" / "videos"
    mp4_files = list(media_root.rglob("CompletingTheSquareScene.mp4"))
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
    topic: str = "Visual proof of completing the square for quadratics",
    is_short: bool = True,
) -> str:
    """End-to-end content generation: Manim + edge-tts + ffmpeg mux."""
    print(f"Generating math video for topic: {topic}")
    print(f"Format: {'1080x1920 (YouTube Shorts)' if is_short else '1920x1080 (Landscape)'}")

    with tempfile.TemporaryDirectory() as tmpdir:
        raw_video = render_manim_video(tmpdir, is_short=is_short)
        voice_mp3 = os.path.join(tmpdir, "voiceover.mp3")
        generate_voiceover(voice_mp3, VOICEOVER_SCRIPT)
        mux_audio_video(raw_video, voice_mp3, output_mp4)

    print(f"Final video saved to: {output_mp4}")
    return output_mp4


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a math educational video.")
    parser.add_argument(
        "--output",
        default="/content/drive/MyDrive/MathYouTube/completing_the_square.mp4",
        help="Output .mp4 path",
    )
    parser.add_argument(
        "--topic",
        default="Visual proof of completing the square for quadratics",
        help="Math topic",
    )
    parser.add_argument("--landscape", action="store_true", help="Render 1920x1080 instead of 1080x1920")
    args = parser.parse_args()

    generate_math_video(
        output_mp4=args.output,
        topic=args.topic,
        is_short=not args.landscape,
    )

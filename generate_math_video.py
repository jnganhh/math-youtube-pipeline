"""
generate_math_video.py
Generates an engaging, 100% audio-video synced MPM2D math video in a clean WHITE & LIGHT theme
using per-segment edge-tts durations + Manim visual scenes (parabola graphs, area models, algebra).
"""

import argparse
import asyncio
import json
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, Any, List, Optional

from mpm2d_topics import pick_topic


SCENE_SCRIPT_TEMPLATE = '''
import json
from manim import *

TOPIC_DATA = json.loads(r"""__TOPIC_JSON__""")
SEG_DURATIONS = json.loads(r"""__DURATIONS_JSON__""")

config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class MPM2DVisualScene(Scene):
    def build_graph_visual(self, max_w):
        g = TOPIC_DATA["graph"]
        xr = g["x_range"]
        yr = g["y_range"]
        axes = Axes(
            x_range=xr,
            y_range=yr,
            x_length=max_w - 0.3,
            y_length=2.8,
            axis_config={"color": "#64748b", "stroke_width": 2, "include_tip": True},
            tips=True,
        )
        axes_labels = axes.get_axis_labels(
            MathTex("x", font_size=22, color="#475569"),
            MathTex("y", font_size=22, color="#475569"),
        )
        objs = VGroup(axes, axes_labels)
        curves_grp = VGroup()
        for c in g.get("curves", []):
            a, h, k = c["a"], c["h"], c["k"]
            curve = axes.plot(
                lambda x, a=a, h=h, k=k: a * (x - h) ** 2 + k,
                x_range=[xr[0], xr[1]],
                color=c["color"],
                stroke_width=3.5,
            )
            # Clip visually to y_range
            curves_grp.add(curve)
        dots_grp = VGroup()
        for dx, dy, dcol, dtxt in g.get("dots", []):
            pt = axes.coords_to_point(dx, dy)
            dot = Dot(pt, color=dcol, radius=0.07)
            dots_grp.add(dot)
            if dtxt:
                lbl = Text(dtxt, font_size=16, color=dcol, weight=BOLD).next_to(dot, UR, buff=0.06)
                dots_grp.add(lbl)
        aos_grp = VGroup()
        if "aos" in g:
            ax_x = g["aos"]
            p1 = axes.coords_to_point(ax_x, yr[0])
            p2 = axes.coords_to_point(ax_x, yr[1])
            aos_grp.add(DashedLine(p1, p2, color="#dc2626", stroke_width=2.5))
        return objs, curves_grp, dots_grp, aos_grp

    def build_area_visual(self, max_w):
        al = TOPIC_DATA["area_labels"]
        top_l, top_r, left_t, left_b, c11, c12, c21, c22 = al
        w, h = 1.35, 0.85
        b11 = Rectangle(width=w, height=h, color="#38bdf8", fill_color="#e0f2fe", fill_opacity=1.0)
        b12 = Rectangle(width=w, height=h, color="#34d399", fill_color="#d1fae5", fill_opacity=1.0).next_to(b11, RIGHT, buff=0.04)
        b21 = Rectangle(width=w, height=h, color="#34d399", fill_color="#d1fae5", fill_opacity=1.0).next_to(b11, DOWN, buff=0.04)
        b22 = Rectangle(width=w, height=h, color="#fbbf24", fill_color="#fef3c7", fill_opacity=1.0).next_to(b21, RIGHT, buff=0.04)

        t11 = MathTex(c11, font_size=26, color="#0369a1").move_to(b11)
        t12 = MathTex(c12, font_size=26, color="#047857").move_to(b12)
        t21 = MathTex(c21, font_size=26, color="#047857").move_to(b21)
        t22 = MathTex(c22, font_size=26, color="#b45309").move_to(b22)

        h_top1 = MathTex(top_l, font_size=24, color="#0f172a").next_to(b11, UP, buff=0.12)
        h_top2 = MathTex(top_r, font_size=24, color="#0f172a").next_to(b12, UP, buff=0.12)
        h_left1 = MathTex(left_t, font_size=24, color="#0f172a").next_to(b11, LEFT, buff=0.12)
        h_left2 = MathTex(left_b, font_size=24, color="#0f172a").next_to(b21, LEFT, buff=0.12)

        grid = VGroup(b11, b12, b21, b22, t11, t12, t21, t22, h_top1, h_top2, h_left1, h_left2)
        if grid.width > max_w:
            grid.set(width=max_w)
        return grid

    def build_linear_graph(self):
        data = TOPIC_DATA["linear_graph"]
        lo, hi = data["range"]
        axes = Axes(x_range=[lo, hi, data["tick"]], y_range=[lo, hi, data["tick"]],
                    x_length=3, y_length=3, tips=False,
                    axis_config={"color": "#94a3b8", "stroke_width": 2})
        x_label = MathTex("x", font_size=18, color="#475569").next_to(axes.x_axis, RIGHT, buff=.06)
        y_label = MathTex("y", font_size=18, color="#475569").next_to(axes.y_axis, UP, buff=.06)
        diagram = VGroup(axes, x_label, y_label)
        strokes = [(axes.c2p(lo, 0), axes.c2p(hi, 0)),
                   (axes.c2p(0, lo), axes.c2p(0, hi))]
        for (a, b, c), color in zip(data["lines"], ["#2563eb", "#d97706"]):
            # Clip ax + by = c to the square, including vertical lines.
            points = []
            if b:
                points.extend((x, (c - a*x)/b) for x in (lo, hi))
            if a:
                points.extend(((c - b*y)/a, y) for y in (lo, hi))
            ends = []
            for x, y in points:
                p = axes.c2p(x, y)
                if lo <= x <= hi and lo <= y <= hi and not any(np.allclose(p, q) for q in ends):
                    ends.append(p)
            if len(ends) == 2:
                diagram.add(Line(*ends, color=color, stroke_width=3))
                strokes.append(ends)
        radius = data.get("radius")
        if radius:
            diagram.add(Circle(radius=axes.x_axis.unit_size * radius,
                               color="#d97706" if data["lines"] else "#2563eb",
                               stroke_width=3).move_to(axes.c2p(0, 0)))
        dots = [(axes.c2p(x, y), name) for x, y, name in data["dots"]]
        locations = {name: p for p, name in dots}
        for start, end in data.get("segments", []):
            p, q = locations[start], locations[end]
            diagram.add(Line(p, q, color="#2563eb", stroke_width=3))
            strokes.append((p, q))
        occupied = [(p, np.array([.05, .05])) for p, _ in dots]
        occupied.extend((label.get_center(), np.array([label.width, label.height]) / 2)
                        for label in (x_label, y_label))

        def clear_label(label):
            centre = label.get_center()
            half = np.array([label.width, label.height]) / 2 + .025
            if any(np.all(np.abs((centre - q)[:2]) < half + size) for q, size in occupied):
                return False
            if radius:
                offset = np.abs((centre - axes.c2p(0, 0))[:2])
                near = np.linalg.norm(np.maximum(offset - half, 0))
                far = np.linalg.norm(offset + half)
                if near <= axes.x_axis.unit_size * radius <= far:
                    return False
            for start, end in strokes:
                dx, dy, _ = end - start
                normal = np.array([-dy, dx])
                if abs(normal @ (centre - start)[:2]) <= abs(normal) @ half:
                    return False
            return True

        for p, name in dots:
            dot = Dot(p, radius=.047, color="#047857")
            label = Text(name, font_size=18, color="#0f172a")
            for gap in (.06, .12, .2, .32, .5):
                for direction in (UR, UL, DR, DL, UP, RIGHT, LEFT, DOWN):
                    label.next_to(dot, direction, buff=gap)
                    if clear_label(label):
                        break
                else:
                    continue
                break
            else:
                raise ValueError(f"No clear position for graph label {name}")
            occupied.append((label.get_center(), np.array([label.width, label.height]) / 2))
            diagram.add(dot, label)
        caption = Text(f"Grid step: {data['tick']} unit" + ("s" if data['tick'] != 1 else ""),
                       font_size=16, color="#475569")
        diagram.add(caption.next_to(diagram, DOWN, buff=.12))
        return diagram

    def build_triangle(self):
        data = TOPIC_DATA["triangle"]
        points = np.array([[x, y, 0.] for x, y in data["points"]])
        points *= 3 / max(np.ptp(points[:, 0]), np.ptp(points[:, 1]))
        centre = points.mean(axis=0)
        diagram = VGroup()
        for i, (value, color) in enumerate(zip(data["sides"], ["#2563eb", "#059669", "#d97706"])):
            p, q = points[i], points[(i+1) % 3]
            edge = Line(p, q, color=color, stroke_width=5)
            normal = rotate_vector(edge.get_unit_vector(), PI/2)
            if np.dot(normal, edge.get_center()-centre) < 0:
                normal *= -1
            label = MathTex(value, font_size=24, color=color)
            gap = .09 + (abs(normal[0])*label.width + abs(normal[1])*label.height)/2
            label.move_to(edge.get_center() + gap*normal)
            diagram.add(edge, label)
        for i, value in enumerate(data["angles"]):
            if not value:
                continue
            p = points[i]
            first = Line(p, points[(i+1) % 3])
            last = Line(p, points[(i-1) % 3])
            radius = min(.34, first.get_length()/4, last.get_length()/4)
            if value == "right":
                diagram.add(RightAngle(first, last, length=radius*.65, color="#475569"))
            else:
                diagram.add(Angle(first, last, radius=radius, color="#475569"))
                outward = -(first.get_unit_vector() + last.get_unit_vector())
                label = MathTex(value, font_size=22, color="#0f172a")
                label.next_to(VectorizedPoint(p), outward / np.linalg.norm(outward), buff=.07)
                diagram.add(label)
        if data["angles"][1] == "right":
            key = VGroup(*(Text(s, color=c, font_size=16) for s, c in
                         [("Adjacent", "#2563eb"), ("Opposite", "#059669"),
                          ("Hypotenuse", "#d97706")])).arrange(RIGHT, buff=.18)
            diagram.add(key.next_to(diagram, DOWN, buff=.15))
        return diagram

    def construct(self):
        self.camera.background_color = "#ffffff"
        max_w = 4.0 if self.camera.frame_width < 6 else 11.0

        # Top header
        title = Text(TOPIC_DATA["title"], font_size=32, color="#0f172a", weight=BOLD)
        if title.width > max_w:
            title.set(width=max_w)
        subtitle = Text(TOPIC_DATA["subtitle"], font_size=20, color="#2563eb")
        if subtitle.width > max_w:
            subtitle.set(width=max_w)
        header = VGroup(title, subtitle).arrange(DOWN, buff=0.1).to_edge(UP, buff=0.4)

        rule_box = RoundedRectangle(
            corner_radius=0.12,
            width=max_w + 0.2,
            height=0.82,
            color="#cbd5e1",
            fill_color="#f8fafc",
            fill_opacity=1.0,
            stroke_width=2,
        )
        rule_tex = MathTex(TOPIC_DATA["rule"], font_size=26, color="#1e293b")
        if rule_tex.width > max_w - 0.15:
            rule_tex.set(width=max_w - 0.15)
        rule_tex.move_to(rule_box.get_center())
        rule_card = VGroup(rule_box, rule_tex).next_to(header, DOWN, buff=0.25)

        self.add(header, rule_card)

        # Middle Visual Stage (Graph / Area Model / Progress Accent)
        visual_mode = TOPIC_DATA.get("visual", "algebra")
        visual_anchor = rule_card.get_bottom()[1] - 0.35

        graph_objs = None
        diagram = None
        if visual_mode == "graph":
            axes_grp, curves_grp, dots_grp, aos_grp = self.build_graph_visual(max_w)
            full_graph = VGroup(axes_grp, curves_grp, dots_grp, aos_grp)
            full_graph.move_to([0, visual_anchor - full_graph.height / 2 - 0.1, 0])
            graph_objs = (axes_grp, curves_grp, dots_grp, aos_grp)
            card_top_y = full_graph.get_bottom()[1] - 0.35
        elif visual_mode in {"area", "triangle", "linear_graph"}:
            if visual_mode == "area":
                diagram = self.build_area_visual(max_w)
            elif visual_mode == "triangle":
                diagram = self.build_triangle()
            else:
                diagram = self.build_linear_graph()
            diagram.scale(min(1, max_w / diagram.width, 2.9 / diagram.height))
            diagram.move_to([0, visual_anchor - diagram.height / 2 - 0.15, 0])
            card_top_y = diagram.get_bottom()[1] - 0.35
        else:
            card_top_y = visual_anchor - 0.3

        # Lower Zone: Synced Step Card (replaces cleanly each segment)
        active_card = None
        segments = TOPIC_DATA["segments"]
        for i, seg in enumerate(segments):
            dur = float(SEG_DURATIONS[i])
            lbl = Text(seg["label"], font_size=22, color="#475569", weight=BOLD)
            if lbl.width > max_w:
                lbl.set(width=max_w)
            eq = MathTex(seg["tex"], font_size=36, color=seg["color"])
            if eq.width > max_w - 0.2:
                eq.set(width=max_w - 0.2)
            content = VGroup(lbl, eq).arrange(DOWN, buff=0.14)
            box = RoundedRectangle(
                corner_radius=0.14,
                width=max_w + 0.2,
                height=max(1.35, content.height + 0.45),
                color=seg["color"],
                fill_color="#f8fafc",
                fill_opacity=1.0,
                stroke_width=2.5,
            )
            content.move_to(box.get_center())
            new_card = VGroup(box, content)
            new_card.move_to([0, card_top_y - new_card.height / 2, 0])

            reveal = FadeIn(new_card, shift=UP * 0.1)
            if active_card is None:
                anims = [reveal]
            else:
                anims = [Succession(FadeOut(active_card), reveal)]

            # Trigger visual animations in sync with early segments
            if visual_mode == "graph" and graph_objs is not None:
                axes_grp, curves_grp, dots_grp, aos_grp = graph_objs
                if i == 0:
                    anims.append(Create(axes_grp))
                elif i == 1:
                    anims.append(Create(curves_grp))
                elif i == 2:
                    if len(dots_grp) > 0:
                        anims.append(FadeIn(dots_grp))
                    if len(aos_grp) > 0:
                        anims.append(Create(aos_grp))
            elif diagram is not None:
                if i == 0:
                    anims.append(FadeIn(diagram))

            rt = min(1.4, max(0.5, dur * 0.35))
            self.play(*anims, run_time=rt)
            if dur - rt > 0.05:
                self.wait(dur - rt)
            active_card = new_card
'''


async def _generate_tts(text: str, output_mp3: str, voice: str = "en-US-AriaNeural") -> None:
    import edge_tts

    communicate = edge_tts.Communicate(text, voice, rate="+5%")
    await communicate.save(output_mp3)


def _get_audio_duration(mp3_path: str) -> float:
    cmd = [
        "ffprobe",
        "-v", "quiet",
        "-print_format", "json",
        "-show_format",
        mp3_path,
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return float(json.loads(res.stdout)["format"]["duration"])


def generate_synced_voiceover(segments: List[Dict[str, Any]], tmpdir: str, out_mp3: str) -> List[float]:
    """Generate one MP3 per segment, measure exact durations, and concatenate into out_mp3."""
    durations: List[float] = []
    concat_list_path = os.path.join(tmpdir, "concat.txt")

    with open(concat_list_path, "w", encoding="utf-8") as cf:
        for idx, seg in enumerate(segments):
            seg_mp3 = os.path.join(tmpdir, f"seg_{idx}.mp3")
            asyncio.run(_generate_tts(seg["narration"], seg_mp3))
            dur = _get_audio_duration(seg_mp3)
            durations.append(round(dur, 3))
            cf.write(f"file '{seg_mp3}'\n")

    cmd = [
        "ffmpeg",
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list_path,
        "-c", "copy",
        out_mp3,
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if res.returncode != 0:
        raise RuntimeError(f"ffmpeg concat failed:\n{res.stderr}")
    return durations


def render_manim_video(
    output_dir: str,
    topic_data: Dict[str, Any],
    durations: List[float],
    is_short: bool = True,
) -> str:
    """Render the Manim scene with exact per-segment durations."""
    os.makedirs(output_dir, exist_ok=True)
    scene_file = os.path.join(output_dir, "scene_mpm2d.py")
    scene_code = (
        SCENE_SCRIPT_TEMPLATE
        .replace("__TOPIC_JSON__", json.dumps(topic_data))
        .replace("__DURATIONS_JSON__", json.dumps(durations))
    )
    with open(scene_file, "w", encoding="utf-8") as f:
        f.write(scene_code)

    resolution = "1080,1920" if is_short else "1920,1080"
    cmd = [
        "manim",
        "-qh",
        "--fps", "30",
        "--resolution", resolution,
        "--media_dir", os.path.join(output_dir, "media"),
        scene_file,
        "MPM2DVisualScene",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"Manim render failed:\n{result.stderr}\n{result.stdout}")

    media_root = Path(output_dir) / "media" / "videos"
    mp4_files = list(media_root.rglob("MPM2DVisualScene.mp4"))
    if not mp4_files:
        raise FileNotFoundError(f"Could not find rendered Manim MP4 under {media_root}")
    return str(mp4_files[0])


def mux_audio_video(video_path: str, audio_path: str, output_mp4: str) -> str:
    """Mux synced video and audio using ffmpeg."""
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
    """End-to-end content generation with frame-accurate per-segment audio-video sync."""
    topic_data = pick_topic(topic_id, offset=offset)
    print(f"Selected MPM2D topic [{topic_data['id']}]: {topic_data['title']} (visual={topic_data.get('visual')})")

    with tempfile.TemporaryDirectory() as tmpdir:
        voice_mp3 = os.path.join(tmpdir, "voiceover.mp3")
        durations = generate_synced_voiceover(topic_data["segments"], tmpdir, voice_mp3)
        print(f"Per-segment audio durations (total {sum(durations):.1f}s): {durations}")
        raw_video = render_manim_video(tmpdir, topic_data, durations, is_short=is_short)
        mux_audio_video(raw_video, voice_mp3, output_mp4)

    print(f"Final synced video saved to: {output_mp4}")
    return {"output_mp4": output_mp4, "topic": topic_data}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a synced light-theme MPM2D math video.")
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

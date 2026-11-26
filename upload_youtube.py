"""
upload_youtube.py
Uploads a rendered .mp4 video to YouTube using YouTube Data API v3 (videos.insert),
supporting scheduled publishing via `publishAt` (e.g., 5:30 PM, 7:30 PM, 8:30 PM, 10:00 PM).
"""

import argparse
import os
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Tuple
from zoneinfo import ZoneInfo

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
DEFAULT_TOKEN_PATH = "/content/drive/MyDrive/MathYouTube/token.json"

# Daily scheduled publish slots in local time (America/Toronto)
DAILY_SLOTS: List[Tuple[int, int]] = [
    (17, 30),  # 5:30 PM
    (19, 30),  # 7:30 PM
    (20, 30),  # 8:30 PM
    (22, 0),   # 10:00 PM
]


def get_publish_at_iso(
    slot_index: int,
    tz_name: str = "America/Toronto",
) -> str:
    """
    Compute the next UTC ISO-8601 publishAt timestamp for the given daily slot (0..3).
    If today's slot has already passed, schedules for tomorrow.
    """
    tz = ZoneInfo(tz_name)
    now_local = datetime.now(tz)
    hour, minute = DAILY_SLOTS[slot_index % len(DAILY_SLOTS)]
    target_local = now_local.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if target_local <= now_local + timedelta(minutes=5):
        target_local += timedelta(days=1)
    target_utc = target_local.astimezone(timezone.utc)
    return target_utc.strftime("%Y-%m-%dT%H:%M:%SZ")


def load_credentials(token_path: str = DEFAULT_TOKEN_PATH) -> Credentials:
    """Load OAuth credentials from token.json and refresh if expired."""
    if not os.path.isfile(token_path):
        raise FileNotFoundError(
            f"OAuth token file not found at {token_path}. "
            "Please place your YouTube OAuth token.json in Google Drive."
        )

    creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds.valid:
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open(token_path, "w", encoding="utf-8") as f:
                f.write(creds.to_json())
        else:
            raise RuntimeError(
                "YouTube OAuth credentials are invalid and cannot be refreshed. "
                "Re-authenticate and regenerate token.json."
            )
    return creds


def generate_metadata(topic: str, is_short: bool = True) -> Dict[str, object]:
    """Auto-generate an engaging title, description, and relevant tags."""
    short_tag = " #Shorts" if is_short else ""
    title = f"{topic} | MPM2D Grade 10 Math{short_tag}"
    if len(title) > 100:
        title = title[:97] + "..."

    description = (
        f"A clear, step-by-step MPM2D math lesson on: {topic}.\n\n"
        "In this 2.5-minute walkthrough:\n"
        "- Core rule & formula\n"
        "- Step-by-step worked example\n"
        "- Practice problem to test yourself\n\n"
        "#MPM2D #Grade10Math #Quadratics #MathTutorial #VisualMath"
        + (" #Shorts" if is_short else "")
    )

    tags: List[str] = [
        "MPM2D",
        "Grade 10 Math",
        "quadratics",
        "math",
        "algebra",
        "manim",
        "education",
    ]
    if is_short:
        tags.append("Shorts")

    return {
        "title": title,
        "description": description,
        "tags": tags,
        "categoryId": "27",  # Education
    }


def upload_video(
    video_path: str,
    topic: str,
    token_path: str = DEFAULT_TOKEN_PATH,
    is_short: bool = True,
    publish_at: Optional[str] = None,
    creds: Optional[Credentials] = None,
) -> str:
    """
    Upload `video_path` to YouTube.
    If `publish_at` (UTC ISO-8601) is set, YouTube holds it as private and auto-publishes at that time.
    """
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    if creds is None:
        creds = load_credentials(token_path)

    youtube = build("youtube", "v3", credentials=creds)
    meta = generate_metadata(topic, is_short=is_short)

    status_body: Dict[str, object] = {
        "selfDeclaredMadeForKids": False,
    }
    if publish_at:
        # YouTube requires privacyStatus='private' when scheduling publishAt
        status_body["privacyStatus"] = "private"
        status_body["publishAt"] = publish_at
    else:
        status_body["privacyStatus"] = "public"

    body = {
        "snippet": {
            "title": meta["title"],
            "description": meta["description"],
            "tags": meta["tags"],
            "categoryId": meta["categoryId"],
        },
        "status": status_body,
    }

    media = MediaFileUpload(
        video_path,
        mimetype="video/mp4",
        chunksize=1024 * 1024 * 4,
        resumable=True,
    )

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media,
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Upload progress: {int(status.progress() * 100)}%")

    video_id = response["id"]
    studio_url = f"https://studio.youtube.com/video/{video_id}/edit"
    if publish_at:
        print(f"Scheduled upload complete! Video ID: {video_id} | Publishes at: {publish_at}")
    else:
        print(f"Public upload complete! Video ID: {video_id}")
    print(f"YouTube Studio: {studio_url}")
    return studio_url


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload math video to YouTube.")
    parser.add_argument("--video", required=True, help="Path to the final .mp4 file")
    parser.add_argument("--topic", required=True, help="Math topic for metadata generation")
    parser.add_argument("--token", default=DEFAULT_TOKEN_PATH, help="Path to token.json")
    parser.add_argument("--publish-at", default=None, help="UTC ISO-8601 publishAt timestamp")
    parser.add_argument("--landscape", action="store_true", help="Set if 1920x1080 instead of Shorts")
    args = parser.parse_args()

    upload_video(
        video_path=args.video,
        topic=args.topic,
        token_path=args.token,
        is_short=not args.landscape,
        publish_at=args.publish_at,
    )

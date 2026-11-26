"""
upload_youtube.py
Uploads a rendered .mp4 video to YouTube as a PRIVATE draft using
YouTube Data API v3 (videos.insert) with auto-refreshing OAuth credentials.
"""

import argparse
import os
from typing import Dict, List, Optional

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
DEFAULT_TOKEN_PATH = "/content/drive/MyDrive/MathYouTube/token.json"


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
    title = f"{topic} (Visual Proof!){short_tag}"
    if len(title) > 100:
        title = title[:97] + "..."

    description = (
        f"A visual, step-by-step math breakdown of: {topic}.\n\n"
        "Concept Summary:\n"
        "Instead of memorizing formulas, we use geometry to see why the algebra works.\n"
        "Watch how each term corresponds to an actual area, making the solution intuitive.\n\n"
        "#math #mathematics #visualproof #algebra #education"
        + (" #shorts" if is_short else "")
    )

    tags: List[str] = [
        "math",
        "mathematics",
        "visual proof",
        "algebra",
        "math animation",
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
    creds: Optional[Credentials] = None,
) -> str:
    """
    Upload `video_path` to YouTube as a PRIVATE draft.
    Returns the YouTube Studio URL for the uploaded video.
    """
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    if creds is None:
        creds = load_credentials(token_path)

    youtube = build("youtube", "v3", credentials=creds)
    meta = generate_metadata(topic, is_short=is_short)

    body = {
        "snippet": {
            "title": meta["title"],
            "description": meta["description"],
            "tags": meta["tags"],
            "categoryId": meta["categoryId"],
        },
        "status": {
            # HARD REQUIREMENT: Always upload as private draft
            "privacyStatus": "private",
            "selfDeclaredMadeForKids": False,
        },
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
    print(f"Upload complete! Video ID: {video_id}")
    print(f"YouTube Studio (Private Draft): {studio_url}")
    return studio_url


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload math video to YouTube as private draft.")
    parser.add_argument("--video", required=True, help="Path to the final .mp4 file")
    parser.add_argument(
        "--topic",
        default="Visual proof of completing the square for quadratics",
        help="Math topic for metadata generation",
    )
    parser.add_argument("--token", default=DEFAULT_TOKEN_PATH, help="Path to token.json")
    parser.add_argument("--landscape", action="store_true", help="Set if 1920x1080 instead of Shorts")
    args = parser.parse_args()

    upload_video(
        video_path=args.video,
        topic=args.topic,
        token_path=args.token,
        is_short=not args.landscape,
    )

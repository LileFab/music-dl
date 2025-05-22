#!/usr/bin/env python

__author__ = "Lucas PERFEITO"
__email__ = "lucas@perfeito.fr"
__version__ = "0.0.1"

from requests import post, get
from subprocess import call
from config.config import (CLIENT_ID, CLIENT_SECRET, USER_ID)
from logging import getLogger
import os
from datetime import datetime
from auth import get_access_token
from download_song import download_song
logger = getLogger(__name__)

LIKED_TRACKS_URL = f"users/{USER_ID}/likes/tracks?linked_partitioning=true"

def fetch_likes() -> list[str]:
    logger.info("Fetching likes...")
    access_token = get_access_token()

    liked_tracks_response = get(
        f"https://api.soundcloud.com/{LIKED_TRACKS_URL}",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    tracks = liked_tracks_response.json()
    tracks_list = []
    tracks_list.extend(tracks["collection"])

    while tracks["next_href"]:
        try:
            next_href = tracks["next_href"]
            liked_tracks_response = get(
                next_href,
                headers={"Authorization": f"Bearer {access_token}"},
            )
            tracks = liked_tracks_response.json()
            tracks_list.extend(tracks["collection"])
        except KeyError:
            break
    return tracks_list

def main():
    tracks_list = [item["permalink_url"] for item in fetch_likes()]
    current = 1
    for item in tracks_list:
        logger.info("Track {}/{}".format(current, len(tracks_list)))
        download_song(item)

if __name__ == "__main__":
    main()

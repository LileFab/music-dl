from logging import getLogger
import os
from datetime import datetime
from subprocess import call
logger = getLogger(__name__)

def download_song(url: str) -> None:
    now = datetime.now().strftime("%Y-%m-%d")
    folder = os.path.join("downloads", now)
    os.makedirs(folder, exist_ok=True)

    logger.info(f"Downloading song to {folder}... (URL: {url})")
    call(f'scdl -l {url} --path "{folder}"', shell=True)
    logger.info("Song downloaded!\n")
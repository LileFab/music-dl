from config.config import (CLIENT_ID, CLIENT_SECRET, USER_ID)
from auth import get_access_token
from requests import post, get
from download_song import download_song

GET_PLAYLISTS_LIST_URL = f"/users/{USER_ID}/playlists?show_tracks=false&limit=20&access[]=public&access[]=private&access[]=logged-in"
BASE_URL = "https://api.soundcloud.com"

def get_list(access_token: str) -> list[object]:
    playlist_response = get(
        f"{BASE_URL + GET_PLAYLISTS_LIST_URL}",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    json = playlist_response.json()
    urns = [{"title": pl["title"], "urn": pl["urn"]} for pl in json]
    return urns

def get_tracks_from_playlist(url: str, access_token: str):
    URL = f"{BASE_URL}/playlists/{url}/tracks"
    playlist_response = get(
        f"{BASE_URL + GET_PLAYLISTS_LIST_URL}",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    tracks = playlist_response.json()

    tracks_url = [item["tracks_uri"] for item in tracks]
    return tracks_url


def get_all():
    access_token = get_access_token()

    list_tracks = []
    playlists = get_list(access_token)
    playlist_urn = [a["urn"] for a in playlists]
    for urn in playlist_urn:
        list_tracks.extend(get_tracks_from_playlist(urn, access_token=access_token))

    tracks_urls = []
    for t in list_tracks:
        track_response = get(
            f"{t}",
            headers={"Authorization": f"Bearer {access_token}"}
        ).json()
        tracks_urls.extend([t["permalink_url"] for t in track_response])
       
    tracks_urls = set(tracks_urls)
    tracks_urls = list(tracks_urls)
    print(tracks_urls)
    print(f"{len(tracks_urls)} tracks à télécharger")
    for url in tracks_urls:
        download_song(url)

def main():
    get_all()


if __name__ == "__main__":
    main()
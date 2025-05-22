from config.config import (SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
from base64 import b64encode
from requests import post

AUTH_URL = "https://accounts.spotify.com/api/token"

def get_spotify_access_token():
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": SPOTIFY_CLIENT_ID,
        "client_secret": SPOTIFY_CLIENT_SECRET
    }

    response = post(AUTH_URL, headers=headers, data=data)
    json_response = response.json()
    print(json_response)

    print(f"access_token : {json_response["access_token"]}")
    return json_response["access_token"]

def main():
    get_spotify_access_token()


if __name__ == "__main__":
    main()

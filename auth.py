from config.config import (CLIENT_ID, CLIENT_SECRET, USER_ID)
from base64 import b64encode
from requests import post


API_AUTH_URL = "https://secure.soundcloud.com/oauth/token"

def get_access_token():
    credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    encoded_credentials = b64encode(credentials.encode()).decode()

    headers = {
        "accept": "application/json; charset=utf-8",
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {encoded_credentials}",
    }
    data = {
        "grant_type": "client_credentials"
    }

    response = post(API_AUTH_URL, headers=headers, data=data)
    json_response = response.json()

    print(f"access_token : {json_response["access_token"]}")
    return json_response["access_token"]

def main():
    get_access_token()


if __name__ == "__main__":
    main()
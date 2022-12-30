import os
import sys
import wget
import requests

from SwSpotify import spotify
from SwSpotify import SpotifyNotRunning, SpotifyPaused

import src.main.config as config

from colorama import init, Fore

init(autoreset=True)


class CurrentTrack:

    def __init__(self):
        pass


    def return_track(self):
        try:
            string = f"{spotify.artist()}%20-%20{spotify.song()}"
            # this fucking shit breaking whole app 💀
            if "#" in string:
                string = string.replace("#", "")
            return string
        except SpotifyNotRunning as not_running:
            pass
        except SpotifyPaused as paused:
            pass
        except ImportError as imperr:
            pass


    def pretty_string(self):
        try:
            prettystring = f"{spotify.artist()} - {spotify.song()}"
            return prettystring
        except SpotifyNotRunning as not_running:
            print("not running bitch")
        except SpotifyPaused as paused:
            print("paused bitch")
        except ImportError as imperr:
            pass


class GetCover:

    def __init__(self):
        self.get_cover()


    def waiting(self):
        print("waiting untill spotify run...")


    def download(self, url):
        full_path = f"{config.full_path}/spotify_wallpaper/src/resources/temp_layers"
        dirlist = os.listdir(full_path)
        try:
            ls = dirlist.pop()
            if "temp_layer.png" in ls:
                os.remove(f"{full_path}/temp_layer.png")
                wget.download(url, f"{full_path}/temp_layer.png")
            else:
                wget.download(url, f"{full_path}/temp_layer.png")
        except Exception as e:
            wget.download(url, f"{full_path}/temp_layer.png")


    def get_cover(self):
        search_line = CurrentTrack()
        search_line = search_line.return_track()
        if search_line == None:
            self.waiting()
        else:
            AUTH_URL = "https://accounts.spotify.com/api/token"
            auth_response = requests.post(AUTH_URL, {
                "grant_type": "client_credentials",
                "client_id": f"{config.client_id}",
                "client_secret": f"{config.client_secret}",
            })

            auth_response_data = auth_response.json()
            access_token = auth_response_data["access_token"]
            headers = {
                "Authorization": f"Bearer {access_token}"
            }

            base_url = "https://api.spotify.com/v1"
            bang = f"{base_url}/search?q={search_line}&type=track&offset=0&limit=1"
            response = requests.get(bang, headers=headers)
            resp = response.json()
            tracks = resp.get("tracks")
            items = tracks.get("items")
            items = items[0]
            album = items.get("album")
            images = album.get("images")
            images = images[1]
            coverURL = images.get("url")
            self.download(coverURL)

import sys
sys.path.insert(0, '...')

import os
import wget
import requests
from SwSpotify import spotify
from SwSpotify import SpotifyNotRunning, SpotifyPaused

import config


class CurrentTrack:

    def return_track(self):
        try:
            # this fucking shit breaking whole app 💀
            string = f"{spotify.artist()}%20-%20{spotify.song()}"
            if "#" in string:
                string = string.replace("#", "")
            return string
        except SpotifyNotRunning:
            raise Exception("Spotify is not running")
        except SpotifyPaused:
            raise Exception("Spotify is paused") 
        except ImportError as imperr:
            raise Exception("ImportError:", imperr)
        except:
            return "Unknown"


    def pretty_string(self):
        try:
            return f"{spotify.artist()} - {spotify.song()}"
        except SpotifyNotRunning:
            raise Exception("Spotify is not running")
        except SpotifyPaused:
            raise Exception("Spotify is paused") 
        except ImportError as imperr:
            raise Exception("ImportError:", imperr)
        except:
            return "Unknown"


class GetCover:

    def __init__(self):
        self.get_cover()


    def waiting(self):
        print("waiting untill spotify run...")


    def download(self, url):
        full_path = fr"{config.full_path}\src\resources\temp_layers"
        try:
            os.makedirs(full_path, exist_ok=True)
            temp_layer_path = os.path.join(full_path, "temp_layer.png")
            if os.path.exists(temp_layer_path):
                os.remove(temp_layer_path)
            wget.download(url, temp_layer_path)
        except Exception as e:
            print("Error downloading cover:", e)


    def get_cover(self):
        try:
            search_line = CurrentTrack().return_track()
            if search_line == "Unknown":
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
                items = resp.get("tracks").get("items")[0]
                coverURL = items.get("album").get("images")[1].get("url")
                self.download(coverURL)
        except SpotifyNotRunning:
            self.waiting()
        except SpotifyPaused:
            print("Playback is paused")
        except Exception as e:
            print("Failed to get cover image:", e)

from src.main.track_listener import GetCover, CurrentTrack
from src.main.makingimage import MakeImage
from src.main.wallpaper import SetWallpaper

import src.main.config as config

from time import sleep

def setup():
    song = CurrentTrack()
    song = song.pretty_string()
    if song == None:
        print("i hate this")
    else:
        print("getting song cover image...")
        GetCover()
        print("\nmaking image...")
        MakeImage(song)
        print("setting wallpaper...")
        wp = SetWallpaper()
        wp.setwallpaper()


def listen():
    song = CurrentTrack()
    current_song = song.pretty_string()
    print(f"listening if {current_song} skipped...")
    skipped = True
    while skipped:
        sleep(3)
        track = song.pretty_string()
        if current_song == track:
            continue
        elif current_song != track:
            print("song is skipped.\nseting up new song")
            current_song = track
            print(f"listening if {current_song} skipped...")
            setup()
        else:
            print(f"{current_song=} | {track=}")


def main():
    setup()
    listen()


if __name__ == "__main__":
    main()
    if config.set_back:
        print("setting wallpaper back to default...")
        wp = SetWallpaper()
        wp.set_back()

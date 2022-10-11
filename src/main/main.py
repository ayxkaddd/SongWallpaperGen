from track_listener import GetCover, CurrentTrack
from makingimage import MakeImage
from wallpaper import SetWallpaper

from time import sleep

def setup():
    print("getting song cover image...")
    GetCover()
    print("\nmaking image...")
    MakeImage()
    print("setting wallpaper...")
    SetWallpaper()


def listen():
    song = CurrentTrack()
    current_song = song.pretty_string()
    print(f"listening if {current_song} skipped...")
    skipped = True
    while skipped:
        sleep(3)
        track = song.pretty_string()
        if current_song == track:
            print(f"{current_song=} | {track=}")
            continue
        elif current_song != track:
            print(f"{current_song=} | {track=}")
            print("song is skipped.\nseting up new song")
            setup()
            current_song = track
        else:
            print(f"{current_song=} | {track=}")


def main():
    setup()
    listen()
    

main()

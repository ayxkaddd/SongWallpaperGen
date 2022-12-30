from src.main.track_listener import GetCover, CurrentTrack
from src.main.makingimage import MakeImage
from src.main.wallpaper import SetWallpaper

import src.main.config as config

from colorama import init, Fore, Style

init(autoreset=True)


def setup():
    try:
        song = CurrentTrack()
        song = song.pretty_string()
        if song == None:
            print(Fore.CYAN + "paused")
        elif song == " - Advertisement":
            print(Fore.YELLOW + Style.BRIGHT + "get premium LMAO !!! :rofl:")
        else:
            print(Fore.BLUE + Style.DIM + "getting song cover...")
            GetCover()
            print(Fore.BLUE + Style.DIM + "\nmaking image...")
            MakeImage(song)
            print(Fore.BLUE + Style.DIM + "setting wallpaper...")
            wp = SetWallpaper()
            wp.setwallpaper()
            print(Fore.GREEN + Style.DIM + "everything is set")
            print(Fore.CYAN + Style.BRIGHT + f"Current Song: {song}")
    except Exception as e:
        main()
    finally:
        pass


def listen():
    song = CurrentTrack()
    current_song = song.pretty_string()

    skipped = True
    while skipped:
        track = song.pretty_string()
        if current_song == track:
            continue
        elif current_song != track:
            current_song = track

            print(Fore.BLUE + Style.DIM + "song is skipped\nseting up new song")
            print(Fore.BLUE + Style.DIM + f"listening if {current_song} skipped")
            setup()
        else:
            print(Fore.RED + Style.RIM + f"{current_song=} | {track=}")


def main():
    setup()
    listen()


if __name__ == "__main__":
    wp = SetWallpaper()
    try:
        main()
    except KeyboardInterrupt:
        if config.set_back:
            print(Fore.YELLOW + Style.BRIGHT +  "setting wallpaper back to default...")
            wp.set_back()
    finally:
        wp.set_back()

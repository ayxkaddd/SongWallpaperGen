import config

from src.main.makingimage import MakeImage
from src.main.wallpaper import SetWallpaper
from src.main.track_listener import GetCover, CurrentTrack

from colorama import init, Fore, Style

init(autoreset=True)

def setup():
    try:
        song = CurrentTrack().pretty_string()
        if song == "Unknown":
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
        print(Fore.RED + Style.BRIGHT + f"Error setting up song: {e}")


def listen():
    current_song = ""
    while True:
        try:
            song = CurrentTrack().pretty_string()
            if song != current_song:
                current_song = song
                print(Fore.BLUE + Style.DIM + f"listening if {current_song} skipped")
                setup()
        except Exception as e:
            print(Fore.RED + Style.BRIGHT + f"Error listening to song: {e}")


if __name__ == "__main__":
    wp = SetWallpaper()
    try:
        listen()
    except KeyboardInterrupt:
        if config.set_back:
            print(Fore.YELLOW + Style.BRIGHT +  "setting wallpaper back to default...")
            wp.set_back()

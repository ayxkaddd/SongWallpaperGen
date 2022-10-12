import ctypes

import src.main.config as config

class SetWallpaper:

    def __init__(self):
        self.setwallpaper()

    def setwallpaper(self):
        full_path = f"{config.full_path}/spotify_wallpaper/src/resources/temp/tempBG.bmp"
        ctypes.windll.user32.SystemParametersInfoW(20, 0, full_path, 0)

    def set_back(self):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{config.wallpaper_path}", 0)

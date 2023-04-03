import sys
sys.path.insert(0, '...')

import ctypes
import config

class SetWallpaper:

    def setwallpaper(self):
        full_path = fr"{config.full_path}\src\resources\temp\tempBG.bmp"
        ctypes.windll.user32.SystemParametersInfoW(20, 0, full_path, 0)


    def set_back(self):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{config.wallpaper_path}", 0)

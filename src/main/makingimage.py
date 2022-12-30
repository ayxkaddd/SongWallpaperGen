from colorama import init, Fore
from PIL import Image, ImageDraw, ImageFont

import src.main.config as config

init(autoreset=True)


class MakeImage:

    def __init__(self, song, bg_path="default"):
        self.song = song
        self.bg_path = f"{config.full_path}/spotify_wallpaper/src/resources/background_test.png"
        self.makeimage()


    def makeimage(self, layer_path=fr"{config.full_path}/spotify_wallpaper/src/resources/temp_layers/temp_layer.png"):
        full_bg_path = fr"{config.full_path}/spotify_wallpaper/src/resources/temp/tempBG.bmp"
        bg = Image.open(fr"{self.bg_path}")
        layer = Image.open(fr"{layer_path}")
        x = 980
        y = 1250
        AREA = (1650, 110)
        PINK = (255, 0, 255)
        FNT = ImageFont.truetype("comicbd.ttf", 50)

        bg.paste(layer, AREA)
        first_text = ImageDraw.Draw(bg)
        first_text.text((x, y-100), "HIS ASS IS LISTENING", font=FNT, fill=PINK)
        track_text = ImageDraw.Draw(bg)
        # bg.save(full_bg_path)
        song_len = len(self.song) * 10
        widht = 2630 / 2
        x = (widht-song_len) - song_len / 2
        track_text.text((x, y), f"{self.song}", font=FNT, fill=PINK)
        bg.save(fr"{full_bg_path}")

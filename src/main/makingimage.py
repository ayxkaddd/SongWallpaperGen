import os
from PIL import Image, ImageDraw, ImageFont

import src.main.config as config

class MakeImage:

    def __init__(self, song, bg_path="default"):
        self.song = song
        self.bg_path = f"{config.full_path}/spotify_wallpaper/src/resources/background_test.png"
        self.makeimage()


    def makeimage(self, layer_path=f"{config.full_path}/spotify_wallpaper/src/resources/temp_layers/temp_layer.png"):
        try:
            bg = Image.open(self.bg_path)
            layer = Image.open(layer_path)
            area = (1650, 110)
            PINK = (255, 0, 255)
            fnt = ImageFont.truetype("comicbd.ttf", 50)
            x = 950
            y = 1250

            bg.paste(layer, area)
            first_text = ImageDraw.Draw(bg)
            first_text.text((x, y-100), "HIS ASS IS LISTENING", font=fnt, fill=PINK)
            track_text = ImageDraw.Draw(bg)
            song_len = len(self.song) * 10

            widht = 2560 / 2
            x = (widht-song_len) - song_len / 2
            track_text.text((x, y), f"{self.song}", font=fnt, fill=PINK)
            full_bg_path = f"{config.full_path}/spotify_wallpaper/src/resources/temp/tempBG.bmp"
            bg.save(f"{full_bg_path}")
        except Exception as e:
            print(e)

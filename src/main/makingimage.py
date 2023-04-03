import sys
sys.path.insert(0, '...')
import config

from PIL import Image, ImageDraw, ImageFont


class MakeImage:

    def __init__(self, song, bg_path=fr"{config.full_path}\src\resources\background_test.png"):
        self.song = song
        self.bg_path = bg_path
        self.makeimage()


    def makeimage(self):
        try:
            layer_path=fr"{config.full_path}\src\resources\temp_layers\temp_layer.png"
            full_bg_path = fr"{config.full_path}\src\resources\temp\tempBG.bmp"
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
            song_len = FNT.getsize(self.song)[0] + len(self.song) * 5
            widht = 2630
            x = (widht - song_len) / 2
            track_text.text((x, y), f"{self.song}", font=FNT, fill=PINK)
            bg.save(fr"{full_bg_path}")
        except Exception as e:
            print(e)

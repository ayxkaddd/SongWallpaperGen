from PIL import Image, ImageDraw, ImageFont

import src.main.config as config

class MakeImage:

    def __init__(self, song, bg_path="default"):
        self.song = song
        self.bg_path = f"{config.full_path}/spotify_wallpaper/src/resources/background.png"
        self.makeimage()


    def makeimage(self, layer_path=f"{config.full_path}/spotify_wallpaper/src/resources/temp_layers/temp_layer.png"):
        try:
            bg = Image.open(self.bg_path)
            layer = Image.open(layer_path)
            area = (1650, 110)
            PINK = (255, 0, 255)
            fnt = ImageFont.truetype("comicbd.ttf", 50)
            x = 950

            bg.paste(layer, area)
            first_text = ImageDraw.Draw(bg)
            first_text.text((x, 1250-100), "HIS ASS IS LISTENING:", font=fnt, fill=PINK)
            track_text = ImageDraw.Draw(bg)
            song_len = len(self.song)
            if song_len < 15:
                print("[0]")
                x = x + (song_len * 10) + 40
                print(x)
            elif song_len >= 20 and song_len < 25:
                print("[1]")
                x = x + (song_len * 2) - 30
            elif song_len >= 25 and song_len < 30:
                print("[2]")
                x = x - (song_len) + 30
            elif song_len >= 30 and song_len < 40:
                print("[3]")
                x = x - (song_len * 4) + 30
                print(x)
            elif song_len >= 40 and song_len < 50:
                print("[4]")
                x = x - (song_len * 7)
            elif song_len >= 50 and song_len < 60:
                print("[5]")
                x = x - (song_len * 5)
            elif song_len >= 60:
                x = x - (song_len * 6)
            else:
                print("[6]")
                print(song_len)
                x = (x + (song_len)) + 50
                print(x)
                
            track_text.text((x, 1250), f"{self.song}", font=fnt, fill=PINK)
            bg.save(f"{config.full_path}/spotify_wallpaper/src/resources/temp/tempBG.bmp")

        except Exception as e:
            print(e)

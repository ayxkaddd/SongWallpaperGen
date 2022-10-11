from PIL import Image

import config

class MakeImage:

    def __init__(self, bg_path="default"):
        self.bg_path = f"{config.full_path}/spotify_wallpaper/src/resources/background.png"
        self.makeimage()


    def makeimage(self, layer_path=f"{config.full_path}/spotify_wallpaper/src/resources/temp_layers/temp_layer.png"):
        try:
            bg = Image.open(self.bg_path)
            layer = Image.open(layer_path)

            area = (1650, 110)

            bg.paste(layer, area)
            bg.save(f"{config.full_path}/spotify_wallpaper/src/resources/temp/tempBG.bmp")
        except Exception as e:
            print(e)

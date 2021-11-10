import io

from PIL import Image

class ImageTriggers:
    def __init__(self):
        pass

    def getTrigger(self, img):
        trigger = 0
        image = Image.open(io.BytesIO(img))
        if image.getpixel((294, 520)) == (64, 42, 25, 255):
            return 1 # тригер на конец боя
        if image.getpixel((529, 950)) == (7, 71, 144, 255):
            return 2 # тригер на бой
        if image.getpixel((530, 944)) == (64, 76, 95, 255):
            return 3 # тригер на меню
        if image.getpixel((280, 500)) == (66, 66, 66, 255):
            return 4 # тригер на меню
        return trigger

import io

from PIL import Image
from loguru import logger


class ImageTriggers:
    def __init__(self):
        self.index2X2 = False
        self.image = None
        self.imageCheakEnglishLanguage = Image.open('imageTrigger/EnglishLanguage.png')

    def _cheakEnglishLanguage(self):
        pass

    def _getNumeberCrown(self):
        if self.image.getpixel((401, 462)) == (200, 111, 22, 255) or self.image.getpixel((401, 462)) == (49, 54, 54, 255):
            return 3
        if self.image.getpixel((270, 448)) == (253, 162, 65, 255) or self.image.getpixel((270, 448)) == (63, 66, 65, 255):
            return 2
        if self.image.getpixel((150, 453)) == (210, 116, 24, 255) or self.image.getpixel((150, 453)) == (52, 55, 55, 255):
            return 1
        return 0

    def _getTriggerOpenChest(self):
        Chests = [
                self.image.crop((109, 833, 114, 838)),
                self.image.crop((243, 833, 248, 838)),
                self.image.crop((376, 833, 381, 838)),
                self.image.crop((508, 833, 513, 838)),
                ]

        sumPixelChests = []
        for image in Chests:
            width, height = image.size
            sumPixel = [0, 0, 0]

            for x in range(0, width):
                for y in range(0, height):
                    pixel = image.getpixel((x, y))
                    sumPixel[0] += pixel[0]
                    sumPixel[1] += pixel[1]
                    sumPixel[2] += pixel[2]

            sumPixelChests.append(sumPixel)

        meanPixels = []
        for sumPixelChest in sumPixelChests:
            meanPixel = [sumPixelChest[0]/25, sumPixelChest[1]/25, sumPixelChest[2]/25]
            meanPixels.append(meanPixel)

        index = 0
        for meanPixel in meanPixels:
            index += 1
            if meanPixel[0] == 255.0:
                if meanPixel[1] >= 229.0 and meanPixel[2] <= 255.0:
                    if meanPixel[2] >= 84.0 and meanPixel[2] <= 112.1:
                        return index

    def _getTriggerOpenedChest(self):
        chestsPixel = [
            self.image.getpixel((52, 701)),
            self.image.getpixel((192, 718)),
            self.image.getpixel((318, 701)),
            self.image.getpixel((452, 701)),
        ]

        index = 0
        for pixel in chestsPixel:
            index += 1
            if pixel == (255, 255, 255, 255):
                return index

    def _getTextError(self):
        i = self.image.crop((40, 370, 495, 540))
        return 'TEXT ERROR'

    def _getElixir(self):
        arrayPixel = self.image.crop((184, 937, 516, 938))
        sumPixel = 0

        if self.image.getpixel((519, 940)) != (2, 25, 88, 255):
            return 10

        for index in range(330):
            pixel = arrayPixel.getpixel((index, 0))
            if pixel == (210, 34, 216, 255):
                sumPixel += 1

        error = 1 if self != 0 else 0
        return round(sumPixel / 37) + error


    def getTrigger(self, img):
        self.image = Image.open(io.BytesIO(img))

        if self.image.getpixel((40, 790)) == (255, 255, 255, 255):  # тригер на облачко

            if self.image.getpixel((529, 950)) == (7, 71, 144, 255):  # тригер нижнию часть экрана
                return (100, self._getElixir())  # тригер на бой

            if self.image.getpixel((300, 840)) == (104, 187, 255, 255):  # тригер на кнопку выйти
                if self.index2X2:
                    self.index2X2 = False
                    logger.info(self._getNumeberCrown())
                    return (121, None)  # тригер на закрытие чата в после боя 2х2
                else:
                    self.index2X2 = True
                    return (124, None)  # тригер на конец боя 1х1

        if self.image.getpixel((526, 951)) == (52, 66, 83, 255):  # тригер нижнию часть экрана при игре 2х2
            if self.index2X2:
                self.index2X2 = False
                logger.info(self._getNumeberCrown())
                return (122, None)  # тригер на закрытие чата в после боя 2х2
            else:
                self.index2X2 = True
                return (124, None)  # тригер на конец боя 2х2

        if self.image.getpixel((40, 790)) == (255, 255, 255, 255):
            return (124, None)

        self.index2X2 = False

        if self.image.getpixel((530, 944)) == (64, 76, 95, 255):  # пиксель на кропку эвента если она не активка
            if self.image.getpixel((272, 893)) == (216, 234, 246, 255):  # пиксель на кропку эвента если она не активка
                if self.image.getpixel((435, 876)) == (48, 185, 71, 255):
                    pass
                    # return (201, None)  # тригер на отправку запроса карт

                if self._getTriggerOpenChest():
                    return (220 + self._getTriggerOpenChest(), None)

                if self._getTriggerOpenedChest():
                    return (230 + self._getTriggerOpenedChest(), None)

                return (200, None)  # тригер на меню

        if self.image.getpixel((267, 431)) == (255, 200, 88, 255):  # пиксель всплывающего окна лимита
            return (250, None)  # тригер на лимит наград

        if self.image.getpixel((442, 906)) == (154, 205, 255, 255):
            return (300, None)  # тригер на пиксель экрана поиска боя

        if self.image.getpixel((14, 945)) == (24, 113, 216, 255):
            return (301, None)  # тригер на пиксель экрана загрузки

        if self.image.getpixel((280, 500)) == (66, 66, 66, 255):  # пиксель всплывающего окна
            if self.image.getpixel((285, 495)) == (66, 66, 66, 255):
                return (400, self._getTextError())  # тригер на потерю соединения либо подключения другого устройства

        return (0, None)  # В случае если не нашел тригеров


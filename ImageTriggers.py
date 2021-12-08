import io

from PIL import Image
from loguru import logger


class ImageTriggers:
    def __init__(self):
        self.image = None

    def _getChests(self):
        i = self.image.crop((30, 688, 532, 729))
        pass

    def _getNumeberCrown(self):
        if self.image.getpixel((401, 462)) == (200, 111, 22, 255):
            return 3
        if self.image.getpixel((270, 448)) == (253, 162, 65, 255):
            return 2
        if self.image.getpixel((150, 453)) == (210, 116, 24, 255):
            return 1
        return 0

    def _getTriggerOpenChest(self):
        Chests = [
                self.image.crop((109, 833, 114, 838)),
                self.image.crop((243, 833, 248, 838)),
                self.image.crop((376, 833, 381, 838)),
                self.image.crop((508, 833, 513, 838)),
                ]

    def getTextError(self):
        i = self.image.crop((40, 370, 495, 540))

    def getTrigger(self, img):
        self.image = Image.open(io.BytesIO(img))
        if self.image.getpixel((40, 790)) == (255, 255, 255, 255):  # тригер на облачко
            if self.image.getpixel((529, 950)) == (7, 71, 144, 255):  # тригер нижнию часть экрана
                return 100  # тригер на бой + элкксир
            if self.image.getpixel((300, 840)) == (104, 187, 255, 255):  # тригер на кнопку выйти
                logger.info(self._getNumeberCrown())
                return 121  # тригер на конец боя 1х1
        if self.image.getpixel((508, 38)) == (242, 43, 39, 255):
            return 123  # тригер на закрытие чата в после боя 2х2
        if self.image.getpixel((526, 951)) == (52, 66, 83, 255):  # тригер нижнию часть экрана при игре 2х2
            logger.info(self._getNumeberCrown())
            return 122  # тригер на конец боя 2х2
        if self.image.getpixel((40, 790)) == (255, 255, 255, 255):
            return 124 # тригер на облачко

        if self.image.getpixel((530, 944)) == (64, 76, 95, 255):  # пиксель на кропку эвента если она не активка
            if self.image.getpixel((272, 893)) == (216, 234, 246, 255):  # пиксель на кропку эвента если она не активка
                if self.image.getpixel((435, 876)) == (48, 185, 71, 255):
                    return 201  # тригер на отправку запроса карт
                return 200  # тригер на меню

        if self.image.getpixel((442, 906)) == (154, 205, 255, 255):
            return 300  # тригер на пиксель экрана поиска боя
        if self.image.getpixel((14, 945)) == (24, 113, 216, 255):
            return 301  # тригер на пиксель экрана загрузки

        if self.image.getpixel((280, 500)) == (66, 66, 66, 255):  # пиксель всплывающего окна
            if self.image.getpixel((285, 495)) == (66, 66, 66, 255):
                return 400  # тригер на потерю соединения либо подключения другого устройства

        if self.image.getpixel((267, 431)) == (255, 200, 88, 255):  # пиксель всплывающего окна лимита
            return 500  # тригер на лимит наград

        return 0  # В случае если не нашел тригеров
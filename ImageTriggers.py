import io

import neural_networks

from PIL import Image
from loguru import logger

recognitionCard = neural_networks.CardInBatlle()
recognitionElixir = neural_networks.ElixirInBatlle()

class ImageTriggers:
    def __init__(self, open_chest, requested_card):
        self.index2X2 = False
        self.image = None
        self.open_chest = open_chest
        self.requested_card = requested_card
        self.m = []

    def _cheakTimeInBatlle(self):
        i = self.image.crop((450, 0, 538, 53))

    def _getNumeberCrown(self):
        if self.image.getpixel((401, 462))[0:3] == (200, 111, 22) or self.image.getpixel((401, 462)) == (49, 54, 54, 255):
            return 3
        if self.image.getpixel((270, 448))[0:3] == (253, 162, 65) or self.image.getpixel((270, 448)) == (63, 66, 65, 255):
            return 2
        if self.image.getpixel((150, 453))[0:3] == (210, 116, 24) or self.image.getpixel((150, 453)) == (52, 55, 55, 255):
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

        indexChest = 0
        for meanPixel in meanPixels:
            indexChest += 1
            if meanPixel[0] == 255.0:
                if meanPixel[1] >= 229.0 and meanPixel[2] <= 255.0:
                    if meanPixel[2] >= 84.0 and meanPixel[2] <= 112.1:
                        return indexChest

    def _getTriggerOpenedChest(self):
        chestsPixel = [
            self.image.getpixel((52, 701)),
            self.image.getpixel((192, 718)),
            self.image.getpixel((318, 701)),
            self.image.getpixel((452, 701)),
        ]

        indexChest = 0
        for pixel in chestsPixel:
            indexChest += 1
            if pixel[0:3] == (255, 255, 255):
                return indexChest

    def _getTextError(self):
        i = self.image.crop((40, 370, 495, 540))
        return "Text Error"

    def _getCardsInBatlle(self):
        imageCards = [
            self.image.crop((142, 815, 194, 871)),
            self.image.crop((244, 815, 296, 871)),
            self.image.crop((342, 815, 394, 871)),
            self.image.crop((447, 815, 499, 871)),
        ]

        cards = []
        for card in imageCards:
            card = card.resize((26, 28))
            card = recognitionCard.predict(card)
            cards.append(card)

        return cards

    def _getElixir(self):
        elixir = self.image.crop((142, 912, 182, 940))
        elixir = elixir.resize((20, 14))
        return recognitionElixir.predict(elixir)

    def _get_tower_health(self):
        tower_healths = [
                self.image.crop((247, 16, 322, 34)),
                self.image.crop((104, 131, 153, 151)),
                self.image.crop((389, 131, 436, 151)),
                self.image.crop((273, 726, 323, 742)),
                self.image.crop((104, 590, 145, 606)),
                self.image.crop((386, 590, 430, 606)),
                ]

    def x(self):
        slot = [self.image.getpixel((92, 815))[0:3] == (28, 109, 161),
                self.image.getpixel((185, 815))[0:3] == (36, 125, 172),
                self.image.getpixel((345, 815))[0:3] == (36, 125, 172),
                self.image.getpixel((434, 815))[0:3] ==(30, 110, 162),
                ]

        return slot

    def x2(self):
        slot = [
            self.image.getpixel((113, 784))[0:3] == (202, 144, 18), self.image.getpixel((252, 784))[0:3] == (204, 148, 20),
            self.image.getpixel((382, 784))[0:3] == (204, 146, 20), self.image.getpixel((516, 784))[0:3] == (204, 148, 20),
        ]


        return slot

    def getTrigger(self, img):
        self.image = Image.open(io.BytesIO(img))

        if self.image.size == (960, 540):
            return 500, None
        elif self.image.size != (540, 960):
            return 501, None

        if self.image.getpixel((40, 790))[0:3] == (255, 255, 255):  # тригер на облачко

            if self.image.getpixel((529, 950))[0:3] == (7, 71, 144):  # тригер нижнию часть экрана
                return 100, self._getElixir(), self._getCardsInBatlle()  # тригер на бой

            if self.image.getpixel((300, 840))[0:3] == (104, 187, 255):  # тригер на кнопку выйти
                if self.index2X2:
                    self.index2X2 = False
                    logger.info(self._getNumeberCrown())
                    return 121, self._getNumeberCrown()  # тригер на закрытие чата в после боя 2х2
                else:
                    self.index2X2 = True
                    return 124, None  # тригер на конец боя 1х1

        if self.image.getpixel((526, 951))[0:3] == (52, 66, 83):  # тригер нижнию часть экрана при игре 2х2
            if self.index2X2:
                self.index2X2 = False
                logger.info(self._getNumeberCrown())
                return 122, self._getNumeberCrown()  # тригер на закрытие чата в после боя 2х2
            else:
                self.index2X2 = True
                return 124, None  # тригер на конец боя 2х2

        if self.image.getpixel((40, 790))[0:3] == (255, 255, 255):
            return 124, None

        self.index2X2 = False

        if self.image.getpixel((17, 922))[0:3] == (78, 115, 149):
            if self.image.getpixel((63, 830))[0:3] == (255, 255, 255):
                return 237, None

        if self.image.getpixel((530, 944))[0:3] == (64, 76, 95):  # пиксель на кропку эвента если она не активка

            if self.image.getpixel((473, 716))[0:3] == (191, 194, 201):
                return 260, None

            if self.image.getpixel((62, 70))[0:3] == (228, 220, 229):
                return 211, self.x2()

            if self.image.getpixel((501, 812))[0:3] == (76, 172, 255):
                return 212, None

            if self.image.getpixel((63, 877))[0:3] == (236, 8, 56):
                return 236, None

            if self.image.getpixel((272, 893))[0:3] == (216, 234, 246) or self.image.getpixel((272, 893))[0:3] == (216, 234, 245):  # пиксель на кропку батл если она открыта
                if self.image.getpixel((433, 887))[0:3] == (48, 184, 69) and self.requested_card:
                    return 210, None  # тригер на отправку запроса карт
                if self.image.getpixel((433, 887))[0:3] == (236, 8, 56) and self.requested_card:
                    return 211, None # триггер на сообщение в чате

                if self._getTriggerOpenChest() and self.open_chest:
                    return 220 + self._getTriggerOpenChest(), None

                if self._getTriggerOpenedChest() and self.open_chest:
                    return 230 + self._getTriggerOpenedChest(), None

                if self.image.getpixel((264, 193))[0:3] == (152, 75, 7) and self.open_chest:
                    return 235, None

                return 200, self.x()  # тригер на меню

        if self.image.getpixel((47, 539))[0:3] == (7, 49, 74) or self.image.getpixel((47, 539))[0:3] == (8, 55, 83):
            return 225, None

        if self.image.getpixel((273, 122))[0:3] == (51, 203, 254):
            return 226, None

        if self.image.getpixel((267, 431))[0:3] == (255, 200, 88):  # пиксель всплывающего окна лимита
            return 250, None  # тригер на лимит наград

        if self.image.getpixel((30, 924))[0:3] == (73, 86, 108):
            if self.image.getpixel((271, 930))[0:3] == (78, 175, 255):
                if self.image.getpixel((271, 930))[0:3] == (78, 175, 255):
                    arrayPixel = self.image.crop((404, 340, 405, 800))
                    for index in range(450):
                        pixel = arrayPixel.getpixel((0, index))[0:3]
                        if pixel == (248, 253, 248) or pixel == (152, 184, 155) or pixel == (248, 253, 249):
                            return 280, 404, index + 350

                    arrayPixel = self.image.crop((137, 340, 138, 800))
                    for index in range(450):
                        pixel = arrayPixel.getpixel((0, index))[0:3]
                        if pixel == (248, 253, 248) or pixel == (152, 184, 155) or pixel == (248, 253, 249):
                            return 280, 137, index + 350

                    arrayPixel = self.image.crop((200, 340, 201, 800))
                    for index in range(450):
                        pixel = arrayPixel.getpixel((0, index))[0:3]
                        if pixel[0] >= 107 and pixel[0] <= 148 and pixel[1] >= 233 and pixel[1] <= 255 and pixel[2] >= 117 and pixel[2] <= 156:
                            return 280, 200, index + 350

                    arrayPixel = self.image.crop((400, 340, 401, 800))
                    for index in range(450):
                        pixel = arrayPixel.getpixel((0, index))[0:3]
                        if pixel[0] >= 107 and pixel[0] <= 148 and pixel[1] >= 233 and pixel[1] <= 255 and pixel[2] >= 117 and pixel[2] <= 156:
                            return 280, 400, index + 350

        if self.image.getpixel((107, 152))[0:3] == (242, 247, 249):
            for i in range(4):
                arrayPixel = self.image.crop((90 + 120 * i, 300, 91 + 120 * i, 850))
                for index in range(530):
                    pixel = arrayPixel.getpixel((0, index))[0:3]
                    if pixel == (255, 203, 85):
                        return 281, 90 + 120 * i, index + 320

        if self.image.getpixel((500, 150))[0:3] == (97, 104, 124):
            if self.image.getpixel((500, 236))[0:3] == (179, 211, 234):
                return 219, None

        if self.image.getpixel((442, 906))[0:3] == (154, 205, 255):
            return 300, None  # тригер на пиксель экрана поиска боя

        if self.image.getpixel((14, 945))[0:3] == (24, 113, 216):
            return 301, None  # тригер на пиксель экрана загрузки

        if self.image.getpixel((280, 500))[0:3] == (66, 66, 66):  # пиксель всплывающего окна
            if self.image.getpixel((285, 495))[0:3] == (66, 66, 66):
                return 400, self._getTextError()  # тригер на потерю соединения либо подключения другого устройства

        return 0, None  # В случае если не нашел тригеров

    def getTriggerDEBUG(self, img):
        self.image = Image.open(io.BytesIO(img))

        if self.image.size == (960, 540):
            return ((500, None),)
        elif self.image.size != (540, 960):
            return ((501, None),)

        return(
            (100, self.image.getpixel((529, 950)), self.image.getpixel((529, 950))[0:3] == (7, 71, 144)),
            (121, self.image.getpixel((300, 840)), self.image.getpixel((300, 840))[0:3] == (104, 187, 255)),
            (124, self.image.getpixel((40, 790)), self.image.getpixel((40, 790))[0:3] == (255, 255, 255)),
            (200, self.image.getpixel((530, 944)), self.image.getpixel((530, 944))[0:3] == (64, 76, 95)),
            (200, self.image.getpixel((272, 893)), self.image.getpixel((272, 893))[0:3] == (216, 234, 245)),
            (200, self.image.getpixel((272, 893)), self.image.getpixel((272, 893))[0:3] == (216, 234, 246)),
            (210, self.image.getpixel((435, 876)), self.image.getpixel((435, 876))[0:3] == (48, 185, 71)),
            (211, self.image.getpixel((435, 876)), self.image.getpixel((435, 876))[0:3] == (236, 8, 56)),
            (212, self.image.getpixel((501, 812)), self.image.getpixel((501, 812))[0:3] == (76, 172, 255)),
            (219, self.image.getpixel((500, 150)), self.image.getpixel((500, 150))[0:3] == (97, 104, 124)),
            (225, self.image.getpixel((47, 539)), self.image.getpixel((47, 539))[0:3] == (8, 55, 83)),
            (225, self.image.getpixel((47, 539)), self.image.getpixel((47, 539))[0:3] == (7, 49, 74)),
            (226, self.image.getpixel((273, 122)), self.image.getpixel((273, 122))[0:3] == (51, 203, 254)),
            (235, self.image.getpixel((264, 193)), self.image.getpixel((264, 193))[0:3] == (152, 75, 7)),
            (236, self.image.getpixel((63, 877)), self.image.getpixel((63, 877))[0:3] == (236, 8, 56)),
            (237, self.image.getpixel((17, 922)), self.image.getpixel((17, 922))[0:3] == (78, 115, 149)),
            (250, self.image.getpixel((267, 431)), self.image.getpixel((267, 431))[0:3] == (255, 200, 88)),
            (260, self.image.getpixel((473, 716)), self.image.getpixel((473, 716))[0:3] == (191, 194, 201)),
            (300, self.image.getpixel((442, 906)), self.image.getpixel((442, 906))[0:3] == (154, 205, 255)),
            (301, self.image.getpixel((14, 945)), self.image.getpixel((14, 945))[0:3] == (24, 113, 216)),
            (400, self.image.getpixel((280, 500)), self.image.getpixel((280, 500))[0:3] == (66, 66, 66)),
            self.image.size,
            self.getTrigger(img),
        )
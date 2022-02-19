from time import sleep

from ADB_server import ADB_server

from loguru import logger


class Bot:
    def __init__(self, port):
        logger.debug(f'Bot().__init__({port})')
        self.ADB = ADB_server(port=port)

    def runBattleMode(self, mode):
        logger.debug(f'Bot.runBattleMode {mode}')
        self.ADB.click(400, 630)
        sleep(0.5)
        if mode == 'mode_1':
            self.ADB.click(420, 396)
        elif mode == 'mode_2':
            self.ADB.click(420, 644)
        elif mode == '2X2':
            self.ADB.swipe(250, 800, 250, 297)
            self.ADB.click(405, 408)

    def runBattleGlobal(self):
        logger.debug('Bot.runBattleGlobal')
        self.ADB.click(180, 630)

    def runBattleEvent(self):
        logger.debug('Bot.runBattleEvent')
        self.ADB.click(280, 720)

    def rewardLimit(self):
        logger.debug('Bot.rewardLimit')
        self.ADB.click(276, 600)

    def skipLimit(self):
        logger.debug('Bot.skipLimit')
        self.ADB.click(482, 316)
        sleep(1)
        self.ADB.click(280, 900)

    def getRewardChest(self, number):
        logger.debug(f'Bot.getRewardChest {number}')
        self.ADB.click(-25 + number * 120, 780)

    def openChest(self, number):
        logger.debug(f'Bot.openChest {number}')
        self.ADB.click(-25 + number * 120, 780)
        sleep(0.5)
        self.ADB.click(276, 625)

    def returnHome(self):
        logger.debug('Bot.returnHome')
        self.ADB.click(500, 920)
        sleep(0.5)
        self.ADB.click(220, 920)
        sleep(0.5)

    def goToClanChat(self):
        logger.debug('Bot.goToClanChat')
        self.ADB.click(371, 911)

    def openCloseClanChat(self):
        logger.debug('Bot.openCloseClanChat')
        self.ADB.click(490, 61)

    def requestCard(self, id_card):
        logger.debug('Bot.requestCard')
        self.ADB.click(70, 805)
        number = int(id_card)
        line = number // 4
        slide = line // 3
        line = (number // 4) % 4
        _number = number % 4
        if slide == 0:
            if _number == 0:
                self.ADB.click(80, 350 + 170 * line)
            if _number == 1:
                self.ADB.click(210, 350 + 170 * line)
            if _number == 2:
                self.ADB.click(330, 350 + 170 * line)
            if _number == 3:
                self.ADB.click(450, 350 + 170 * line)
            return

        for i in range(slide):
            self.swipeRequestCard()
            sleep(2)
        sleep(3)
        if slide == 4:
            if _number == 0:
                self.ADB.click(80, 450 + 170 * line)
            if _number == 1:
                self.ADB.click(210, 450 + 170 * line)
            if _number == 2:
                self.ADB.click(330, 450 + 170 * line)
            if _number == 3:
                self.ADB.click(450, 450 + 170 * line)

        else:
            if _number == 0:
                self.ADB.click(80, 350 + 170 * line)
            if _number == 1:
                self.ADB.click(210, 350 + 170 * line)
            if _number == 2:
                self.ADB.click(330, 350 + 170 * line)
            if _number == 3:
                self.ADB.click(450, 350 + 170 * line)


    def swipeRequestCard(self):
        logger.debug('Bot.swipeRequestCard')
        self.ADB.swipe(250, 800, 250, 297)
        sleep(0.5)

    def goToEvents(self):
        logger.debug('Bot.goToEvents')
        self.ADB.click(520, 930)

    def goToDeck(self):
        logger.debug('Bot.goToDeck')
        self.ADB.click(168, 930)

    def goToShop(self):
        logger.debug('Bot.goToShop')
        self.ADB.click(80, 930)

    def placingCard1X1(self, x, y):
        logger.debug(f'Bot.placingCard1X1 x = {x}, y = {y}')
        self.ADB.click(x, y)

    def placingCard2X2(self, x, y):
        logger.debug(f'Bot.placingCard2X2 x = {x}, y = {y}')
        self.ADB.click(x, y)

    def exitBatle2X2(self):
        logger.debug('Bot.exitBatle2X2')
        self.ADB.click(74, 910)

    def exitBatle1X1(self):
        logger.debug('Bot.exitBatle1X1')
        self.ADB.click(270, 840)

    def selectCard(self, number):
        logger.debug('Bot.selectCard')
        self.ADB.click(170 + number * 100, 850)

    def setEnglishLanguage(self):
        logger.debug('Bot.setEnglishLanguage')
        self.ADB.click(500, 100)
        sleep(0.5)
        self.ADB.click(325, 470)
        sleep(0.5)
        self.ADB.click(160, 570)
        sleep(0.5)
        self.ADB.click(275, 235)
        sleep(0.5)
        self.ADB.click(370, 590)

    def reboot(self):
        logger.debug('Bot.reboot')
        self.ADB.closeCR()
        sleep(2)
        self.ADB.openCR()

    def openCR(self):
        logger.debug('Bot.openCR')
        self.ADB.openCR()

    def closeCR(self):
        logger.debug('Bot.closeCR')
        self.ADB.closeCR()

    def getScreen(self):
        logger.debug('Bot.getScreen')
        return self.ADB.getScreen()

    def changeAccount(self, number, total_accounts):
        logger.debug(f'Bot.changeAccount {number}, {total_accounts}')
        sleep(3)
        self.ADB.click(500, 90)
        sleep(3)
        self.ADB.click(250, 575)
        sleep(3)
        for i in range((total_accounts // 3) + 1):
            self.ADB.swipe(250,398 , 250, 860)
            sleep(3)
        number = int(number)
        total_accounts = int(total_accounts)
        slide = number // 3
        _number = number % 3
        if slide == 0:
            if _number == 0:
                self.ADB.click(250, 552)
            if _number == 1:
                self.ADB.click(250, 690)
            if _number == 2:
                self.ADB.click(250, 834)
            return
        if not (number % 3 == 2):
            if number == total_accounts - 1 or number == total_accounts - 2:
                if number == total_accounts - 1:
                    _number = 2
                if number == total_accounts - 2:
                    _number = 1
        for i in range(slide):
            self.ADB.swipe(250, 860, 250, 398)
            sleep(3)
        if _number == 0:
            self.ADB.click(250, 552)
        if _number == 1:
            self.ADB.click(250, 690)
        if _number == 2:
            self.ADB.click(250, 834)

    def open_pass_royale(self):
        self.ADB.click(264, 193)

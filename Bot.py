from time import sleep

from ADB_server import ADB_server

from loguru import logger


class Bot:
    def __init__(self, port):
        logger.debug('Bot().__init__()')
        self.ADB = ADB_server(port=port)

    def runBattleMode(self, mode=2):
        logger.debug(f'Bot.runBattleMode {mode}')
        self.ADB.click(400, 630)
        sleep(0.5)
        if mode == 'mode_1':
            self.ADB.click(420, 400)
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

    def requestCard(self):
        logger.debug('Bot.requestCard')
        self.ADB.click(70, 805)

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
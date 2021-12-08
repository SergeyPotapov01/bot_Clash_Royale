from random import randint

from ADB_server import ADB_server


class Bot:
    def __init__(self):
        self.ADB = ADB_server()
        self._inGame = False
        self._inBattle = False
        self._battleMode = None
        self._timeOpenChest = None

    def runBattleMode(self, mode=1):
        self.ADB.click(400, 630)
        if mode == 1:
            self.ADB.click(420, 400)
        else:
            self.ADB.click(420, 640)

    def runBattleGlobal(self):
        self.ADB.click(180, 630)

    def runBattleEvent(self):
        self.ADB.click(280, 720)

    def rewardLimit(self):
        self.ADB.click(276, 600)

    def openChest(self, number):
        self.ADB.click(75 + number * 120, 780)
        self.ADB.click(276, 625)

    def returnHome(self):
        self.ADB.click(500, 920)
        self.ADB.click(220, 920)

    def goToClanChat(self):
        self.ADB.click(371, 911)

    def openCloseClanChat(self):
        self.ADB.click(490, 61)

    def requestCard(self):
        self.ADB.click(70, 805)

    def swipeRequestCard(self):
        self.ADB.swipe(250, 800, 250, 297)

    def goToEvents(self):
        self.ADB.click(520, 930)

    def goToDeck(self):
        self.ADB.click(168, 930)

    def goToShop(self):
        self.ADB.click(80, 930)

    def placingCard1X1(self, x=randint(270, 340), y=randint(545, 730)):
        self.ADB.click(x, y)

    def placingCard2X2(self, x=randint(150, 380), y=randint(570, 735)):
        self.ADB.click(x, y)

    def exitBatle2X2(self):
        self.ADB.click(74, 910)

    def closeChatBatle2X2(self):
        self.ADB.click(509, 30)

    def exitBatle1X1(self):
        self.ADB.click(270, 840)

    def selectCard(self, number):
        self.ADB.click(170 + number * 100, 850)

    def setEnglishLanguage(self):
        self.ADB.click(500, 100)
        self.ADB.click(325, 470)
        self.ADB.click(160, 570)
        self.ADB.click(275, 235)
        self.ADB.click(370, 590)

    def reboot(self):
        self.ADB.closeCR()
        self.ADB.openCR()

    def openCR(self):
        self.ADB.openCR()

    def closeCR(self):
        self.ADB.closeCR()

    def getScreen(self):
        return self.ADB.getScreen()

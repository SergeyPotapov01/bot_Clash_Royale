from ADB_server import ADB_server


class Bot:
    def __init__(self):
        self.ADB = ADB_server()
        self._inGame = False
        self._inBattle = False
        self._battleMode = None
        self._timeOpenChest = None

    def _runBattleMode(self, mode):
        self.ADB.click(400, 630)
        if mode == 1:
            self.ADB.click(420, 400)
        else:
            self.ADB.click(420, 640)

    def _runBattleGlobal(self):
        self.ADB.click(180, 630)

    def openChest(self, number):
        self.ADB.click(75 + number * 120, 780)
        self.ADB.click(276, 625)

    def returnHome(self):
        self.ADB.click(500, 920)
        self.ADB.click(220, 920)

    def setEnglishLanguage(self):
        self.ADB.click(500, 100)
        self.ADB.click(325, 470)
        self.ADB.click(160, 570)
        self.ADB.click(275, 235)
        self.ADB.click(370, 590)

    def _placingCard1X1(self):
        self.ADB.click(275, 720)

    def _placingCard2X2(self):
        self.ADB.click(285, 726)

    def exitBatle2X2(self):
        self.ADB.click(74, 910)

    def exitBatle1X1(self):
        self.ADB.click(270, 840)

    def _selectCard(self, number):
        self.ADB.click(170 + number * 100, 850)
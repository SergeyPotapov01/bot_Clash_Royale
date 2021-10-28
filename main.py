import time

from ADB_server import ADB_server


__version__ = '0.0.2'

ADB_server = ADB_server()

class Bot:
    def __init__(self):
        self.ADB = ADB_server
        self._inGame = False
        self._inBattle = False
        self._battleMode = None

    def battle2X2(self):
        self.ADB.click(460, 560)
        time.sleep(1)
        self.ADB.click(480, 580)

    def battleGlobal(self):
        self.ADB.click(260, 560)

    def selectCard(self, number):
        self.ADB.click(200 + number * 90, 770)

    def main(self):
        while True:
            q = input('1. Battle Global\n 2. Battle 2X2\n 3. Exit')


import time
from random import randint
import threading

from Bot import Bot
from ImageTriggers import ImageTriggers

class strategics:
    def __init__(self):
        self.bot = Bot()
        self.bot.openCR()
        self.triggers = ImageTriggers()
        self.index = 0
        self.cycleStart = False
        self.thread = None

    def cycleStarted(self):
        self.cycleStart = True

    def cycleStoped(self):
        self.cycleStart = False

    def main(self, combatMode=1):
        if self.bot.ADB.cheakInstallCR() == False:
            self.cycleStart = False
            print(1234123)
        if self.bot.ADB.cheakRunCR() == False:
            self.bot.openCR()

        while self.cycleStart:
            t = time.time()
            image = self.bot.getScreen()
            trigger = self.triggers.getTrigger(image)
            if self.index == 30:
                self.bot.returnHome()
                self.bot.reboot()
                self.index = 0
            if self.index == 10:
                self.bot.returnHome()
            if trigger == 0:
                self.index += 1
                time.sleep(1)
                continue
            elif trigger == 100:
                self.bot.selectCard(randint(0, 3))
                self.bot.placingCard1X1()
            elif trigger == 121:
                self.bot.exitBatle1X1()
                time.sleep(3)
            elif trigger == 122:
                self.bot.exitBatle2X2()
                time.sleep(3)
            elif trigger == 123:
                self.bot.closeChatBatle2X2()
            elif trigger == 124:
                self.bot.ADB.click(400, 420)

            elif trigger == 200:
                if combatMode == 0:
                    self.bot.runBattleGlobal()
                else:
                    self.bot.runBattleMode(combatMode)
                time.sleep(2)
            elif trigger == 400:
                time.sleep(120)
                self.bot.exitBatle1X1()
            elif trigger == 500:
                self.bot.rewardLimit()
            self.index = 0
            print(trigger, time.time() - t)

    def startFarm(self):
        self.cycleStart = True
        self.thread = threading.Thread(target=self.main).start()

    def stopFarm(self):
        self.cycleStart = False

if __name__ == '__main__':
    x = strategics()
    x.main()

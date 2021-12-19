import time
from random import randint

from Bot import Bot
from ImageTriggers import ImageTriggers


class Strategics:
    def __init__(self, port=5555):
        self.bot = Bot(port=port)
        self.triggers = ImageTriggers()
        self.index = 0
        self.cycleStart = False

    def cycleStarted(self):
        self.cycleStart = True

    def cycleStoped(self):
        self.cycleStart = False

    def main(self, combatMode=2):

        if self.bot.ADB.cheakInstallCR() == False:
            self.cycleStart = False

        if self.bot.ADB.cheakRunCR() == False:
            self.bot.openCR()

        indexBatle = 0
        while self.cycleStart:
            t = time.time()
            image = self.bot.getScreen()
            triggers = self.triggers.getTrigger(image)
            trigger = triggers[0]

            if self.index == 30:
                self.bot.returnHome()
                self.bot.reboot()
                self.index = 0

            if self.index == 10:
                self.bot.returnHome()

            if trigger == 0:
                self.index += 1
                print('Не найден триггер')
                time.sleep(1)
                continue

            elif trigger == 100:
                if triggers[1] < 4:
                    print('МАЛО ЭЛИКА')
                    continue
                self.bot.selectCard(randint(0, 3))
                self.bot.placingCard1X1(randint(275, 475), randint(426, 700))

            elif trigger == 121:
                indexBatle += 1
                self.bot.exitBatle1X1()
                if indexBatle == 10:
                    self.bot.reboot()
                    indexBatle = 0
                time.sleep(3)

            elif trigger == 122:
                self.bot.exitBatle2X2()
                indexBatle += 1
                if indexBatle == 10:
                    self.bot.reboot()
                    indexBatle = 0
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
                time.sleep(1)

            elif trigger > 220 and trigger < 225:
                self.bot.getRewardChest(trigger - 220)

            elif trigger > 230 and trigger < 235:
                self.bot.openChest(trigger - 230)

            elif trigger == 250:
                self.bot.rewardLimit()

            elif trigger == 270:
                self.index += 1
                if self.index >= 5:
                    self.bot.setEnglishLanguage()
                else:
                    self.bot.returnHome()
                    time.sleep(2)
                    continue

            elif trigger == 400:
                time.sleep(120)
                self.bot.exitBatle1X1()

            self.index = 0
            print(triggers, time.time() - t)

    def startFarm(self):
        self.cycleStart = True
        self.main()

    def stopFarm(self):
        self.cycleStart = False
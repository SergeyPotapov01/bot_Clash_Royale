import time
from random import randint

from Bot import Bot
from ImageTriggers import ImageTriggers

from loguru import  logger


class Strategics:
    def __init__(self, batlleMode, port='5555'):
        self.bot = Bot(port=port)
        self.triggers = ImageTriggers()
        self.index = 0
        self.cycleStart = False
        self.batlleMode = batlleMode

    def cycleStarted(self):
        self.cycleStart = True

    def cycleStoped(self):
        self.cycleStart = False

    def main(self):

        if self.bot.ADB.cheakInstallCR() == False:
            self.cycleStart = False

        if self.bot.ADB.cheakRunCR() == False:
            self.bot.openCR()

        indexBatle = 0
        t = time.time()
        while self.cycleStart:
            image = self.bot.getScreen()
            triggers = self.triggers.getTrigger(image)
            trigger = triggers[0]
            logger.debug(str(triggers) + ' ' + str(time.time() - t))

            if self.index == 30:
                self.bot.returnHome()
                self.bot.reboot()
                self.index = 0

            if self.index == 10:
                self.bot.returnHome()

            if trigger == 0:
                self.index += 1
                logger.debug('Не найден триггер')
                time.sleep(1)
                continue

            elif trigger == 100:
                if 'Golem' in triggers[2]:
                    self.bot.selectCard(triggers[2].index('Golem'))
                    if triggers[1] >= 8:
                        self.bot.placingCard1X1(275, 700)
                    else:
                        time.sleep((8 - triggers[1]) * 2)
                        image = self.bot.getScreen()
                        if self.triggers.getTrigger(image)[0] != 100:
                            continue
                        self.bot.placingCard1X1(275, 700)
                    time.sleep(9)
                    if 'Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Witch'))
                        self.bot.placingCard1X1(275, 700)
                    elif 'Night_Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Night_Witch'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        self.bot.selectCard(triggers[2].index('Golem'))
                        self.bot.placingCard1X1(275, 700)
                    time.sleep(9)
                    image = self.bot.getScreen()
                    if self.triggers.getTrigger(image)[0] != 100:
                        continue
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(475, 550)
                    time.sleep(9)
                    image = self.bot.getScreen()
                    if self.triggers.getTrigger(image)[0] != 100:
                        continue
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(390, 450)
                    continue

                if 'Hog_Rider' in triggers[2]:
                    self.bot.selectCard(triggers[2].index('Hog_Rider'))
                    if triggers[1] >= 4:
                        self.bot.placingCard1X1(475, 426)
                    else:
                        time.sleep((4 - triggers[1]) * 2)
                        self.bot.placingCard1X1(475, 426)

                if 'Cannon' in triggers[2]:
                    self.bot.selectCard(triggers[2].index('Cannon'))
                    if triggers[1] >= 4:
                        self.bot.placingCard1X1(275, 600)
                    else:
                        time.sleep((4 - triggers[1]) * 2)
                        self.bot.placingCard1X1(275, 600)
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

            elif trigger == 124:
                self.bot.ADB.click(400, 420)

            elif trigger == 200:
                if self.batlleMode == 'global':
                    self.bot.runBattleGlobal()
                else:
                    self.bot.runBattleMode(self.batlleMode)
                time.sleep(1)

            elif trigger > 220 and trigger < 225:
                self.bot.getRewardChest(trigger - 220)

            elif trigger == 225:
                self.bot.returnHome()
                time.sleep(0.5)

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
            time.sleep(0.3)
            t = time.time()

    def startFarm(self):
        self.cycleStart = True
        self.main()

    def stopFarm(self):
        self.cycleStart = False
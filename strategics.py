import time
from random import randint

from Bot import Bot
from ImageTriggers import ImageTriggers

from loguru import logger


class Strategics:
    def __init__(self, batlle_mode, open_chest, requested_card, port, changed_account, number_account, total_accounts, connection_to_parent):
        self.bot = Bot(port=port)
        self.triggers = ImageTriggers(open_chest, requested_card)
        self.index = 0
        self.cycleStart = True
        self.batlle_mode = batlle_mode
        self.number_account = number_account
        self.changed_account = changed_account
        self.total_accounts = total_accounts
        self.connection_to_parent = connection_to_parent

    def main(self):
        if self.bot.ADB.cheakInstallCR() == False:
            self.cycleStart = False

        if self.bot.ADB.cheakRunCR() == False:
            self.bot.openCR()

        index_batlle = 0
        t = time.time()
        while True:
            image = self.bot.getScreen()
            triggers = self.triggers.getTrigger(image)
            trigger = triggers[0]
            logger.debug(str(triggers) + ' ' + str(time.time() - t))
            self.connection_to_parent._textBrowser_3 = f'{triggers}\n' + self.connection_to_parent._textBrowser_3
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
                    if triggers[1] >= 8:
                        self.bot.selectCard(triggers[2].index('Golem'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        time.sleep(8 - triggers[1])
                        self.bot.placingCard1X1(275, 700)
                    time.sleep(7)
                    if 'Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Witch'))
                        self.bot.placingCard1X1(275, 700)
                    elif 'Night_Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Night_Witch'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        self.bot.selectCard(triggers[2].index('Golem'))
                        self.bot.placingCard1X1(275, 700)
                    time.sleep(5)
                    image = self.bot.getScreen()
                    if self.triggers.getTrigger(image)[0] != 100:
                        continue
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(475, 550)
                    time.sleep(6)
                    image = self.bot.getScreen()
                    if self.triggers.getTrigger(image)[0] != 100:
                        continue
                    self.bot.selectCard(randint(0, 3))
                    self.bot.placingCard1X1(390, 450)
                    continue

                if 'Goblin_Gang' in triggers[2]:
                    self.bot.selectCard(triggers[2].index('Goblin_Gang'))
                    if triggers[1] >= 3:
                        self.bot.placingCard1X1(260, 700)
                    else:
                        continue

                if 'Princess' in triggers[2]:
                    self.bot.selectCard(triggers[2].index('Princess'))
                    if triggers[1] >= 3:
                        self.bot.placingCard1X1(260, 700)
                    else:
                        continue

                if 'Hog_Rider' in triggers[2]:
                    self.bot.selectCard(triggers[2].index('Hog_Rider'))
                    if triggers[1] >= 4:
                        self.bot.placingCard1X1(475, 426)
                    else:
                        continue

                if 'Cannon' in triggers[2]:
                    self.bot.selectCard(triggers[2].index('Cannon'))
                    if triggers[1] >= 4:
                        self.bot.placingCard1X1(250, 515)
                    else:
                        continue

                if triggers[1] <= 4:
                    continue

                self.bot.selectCard(randint(0, 3))
                self.bot.placingCard1X1(randint(275, 475), randint(426, 700))

            elif trigger == 121:
                index_batlle += 1
                self.bot.exitBatle1X1()
                self.connection_to_parent.totall_batlles += 1
                self.connection_to_parent.got_crowns += triggers[1]
                self.connection_to_parent._textBrowser_2 = f'{triggers[1]}' + self.connection_to_parent._textBrowser_2
                self.connection_to_parent._textBrowser_3 = f'{triggers}\n'

                if index_batlle == 10:
                    self.bot.reboot()
                    index_batlle = 0
                time.sleep(3)

            elif trigger == 122:
                self.bot.exitBatle2X2()
                index_batlle += 1
                self.connection_to_parent.totall_batlles += 1
                self.connection_to_parent.got_crowns += triggers[1]
                self.connection_to_parent._textBrowser_2 = f'{triggers[1]}' + self.connection_to_parent._textBrowser_2
                self.connection_to_parent._textBrowser_3 = f'{triggers}\n'
                if index_batlle == 10:
                    self.bot.reboot()
                    index_batlle = 0
                time.sleep(3)

            elif trigger == 124:
                self.bot.ADB.click(400, 420)

            elif trigger == 200:
                if self.batlle_mode == 'global':
                    self.bot.runBattleGlobal()
                if self.batlle_mode == 'disabled':
                    self.increasing_account_number()
                    self.bot.changeAccount(self.number_account, self.total_accounts)
                    self.connection_to_parent.number_account = self.number_account
                else:
                    self.bot.runBattleMode(self.batlle_mode)
                time.sleep(1)

            elif trigger == 210:
                self.bot.goToClanChat()
                image = self.bot.getScreen()
                triggers = self.triggers.getTrigger(image)
                trigger = triggers[0]
                if trigger != 212:
                    self.bot.goToClanChat()
                self.bot.requestCard(id_card)


            elif trigger == 211:
                self.bot.goToClanChat()
                image = self.bot.getScreen()
                triggers = self.triggers.getTrigger(image)
                trigger = triggers[0]
                if trigger != 212:
                    self.bot.goToClanChat()
                if not 'ДОНАТ КАРТ':
                    pass # Тут будет ебанутый алгоритм для доната карт потом придумаю
                self.bot.returnHome()

            elif trigger > 220 and trigger < 225:
                self.bot.getRewardChest(trigger - 220)

            elif trigger == 225:
                self.bot.returnHome()
                time.sleep(0.5)

            elif trigger > 230 and trigger < 235:
                self.bot.openChest(trigger - 230)

            elif trigger == 250:
                if self.changed_account:
                    self.increasing_account_number()
                    self.bot.returnHome()
                    self.bot.changeAccount(self.number_account, self.total_accounts)
                    self.connection_to_parent.number_account = self.number_account
                else:
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
            t = time.time()

    def increasing_account_number(self):
        if self.number_account == self.total_accounts:
            self.number_account = 0
        else:
            self.number_account += 1

    def startFarm(self):
        self.cycleStart = True
        self.main()

    def stopFarm(self):
        self.cycleStart = False
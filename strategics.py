import time
from random import randint, choice

from Bot import Bot
from ImageTriggers import ImageTriggers

from loguru import logger


class Strategics:
    def __init__(self, batlle_mode, open_chest, requested_card, port, changed_account, number_account, total_accounts, id_card, connection_to_parent):
        self.bot = Bot(port=port)
        self.triggers = ImageTriggers(open_chest, requested_card)
        self.index = 0
        self.cycleStart = True
        self.batlle_mode = batlle_mode
        self.number_account = number_account
        self.changed_account = changed_account
        self.total_accounts = total_accounts
        self.connection_to_parent = connection_to_parent
        self.request_card = requested_card
        self.id_card = id_card

    def main(self):
        if self.bot.ADB.cheakInstallCR() == False:
            self.cycleStart = False

        if self.bot.ADB.cheakRunCR() == False:
            self.bot.openCR()

        slowdown_in_menu = True

        index_batlle = 0
        t = time.time()
        while self.cycleStart:
            image = self.bot.getScreen()
            triggers = self.triggers.getTrigger(image)
            trigger = triggers[0]
            logger.debug(str(triggers) + ' ' + str(time.time() - t))
            self.connection_to_parent._textBrowser_3 = f'{triggers}\n' + self.connection_to_parent._textBrowser_3
            if self.index == 50:
                self.bot.returnHome()
                self.bot.reboot()
                self.index = 0

            if self.index % 5 == 0:
                self.bot.returnHome()

            if trigger == 0:
                self.index += 1
                logger.debug('Не найден триггер')
                time.sleep(1)
                continue

            elif trigger == 100:

                if 'Goblin_Barrel' in triggers[2]:
                    if triggers[1] >= 3:
                        self.bot.selectCard(triggers[2].index('Goblin_Barrel'))
                        self.bot.placingCard1X1(choice((410, 105)), 202)
                    else:
                        continue

                if 'Goblin_Drill' in triggers[2]:
                    if triggers[1] >= 3:
                        self.bot.selectCard(triggers[2].index('Goblin_Drill'))
                        self.bot.placingCard1X1(choice((410, 105)), 256)
                    else:
                        continue

                if 'Balloon' in triggers[2]:
                    if triggers[1] >= 6:
                        self.bot.selectCard(triggers[2].index('Balloon'))
                        self.bot.placingCard1X1(choice((410, 105)), 202)
                    else:
                        continue

                if 'Skeleton_Barrel' in triggers[2]:
                    if triggers[1] >= 4:
                        self.bot.selectCard(triggers[2].index('Skeleton_Barrel'))
                        self.bot.placingCard1X1(choice((410, 105)), 202)
                    else:
                        continue

                if 'Three_Musketeers' in triggers[2]:
                    if triggers[1] >= 9:
                        self.bot.selectCard(triggers[2].index('Three_Musketeers'))
                        self.bot.placingCard1X1(723, 723)
                    else:
                        continue

                if 'Zappies' in triggers[2]:
                    if triggers[1] >= 4:
                        self.bot.selectCard(triggers[2].index('Zappies'))
                        self.bot.placingCard1X1(723, 723)
                    else:
                        continue

                if 'Ram_Rider' in triggers[2]:
                    if triggers[1] >= 6:
                        self.bot.selectCard(triggers[2].index('Ram_Rider'))
                        self.bot.placingCard1X1(choice((410, 105)), 202)
                    else:
                        continue

                if 'Prince' in triggers[2]:
                    if triggers[1] >= 6:
                        self.bot.selectCard(triggers[2].index('Prince'))
                        self.bot.placingCard1X1(choice((410, 105)), 202)
                    else:
                        continue

                if 'Dark_Prince' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Dark_Prince'))
                        self.bot.placingCard1X1(choice((410, 105)), 202)
                    else:
                        continue

                if 'Royal_Hogs' in triggers[2]:
                    if triggers[1] >= 6:
                        self.bot.selectCard(triggers[2].index('Royal_Hogs'))
                        self.bot.placingCard1X1(choice((410, 268, 105)), 202)
                    else:
                        continue

                if 'Golem' in triggers[2]:
                    if triggers[1] >= 8:
                        self.bot.selectCard(triggers[2].index('Golem'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        continue
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

                if 'Giant' in triggers[2]:
                    if triggers[1] >= 6:
                        self.bot.selectCard(triggers[2].index('Giant'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        continue
                    time.sleep(7)
                    if 'Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Witch'))
                        self.bot.placingCard1X1(275, 700)
                    elif 'Night_Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Night_Witch'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        self.bot.selectCard(triggers[2].index('Giant'))
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

                if 'Goblin_Giant' in triggers[2]:
                    if triggers[1] >= 7:
                        self.bot.selectCard(triggers[2].index('Goblin_Giant'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        continue
                    time.sleep(7)
                    if 'Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Witch'))
                        self.bot.placingCard1X1(275, 700)
                    elif 'Night_Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Night_Witch'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        self.bot.selectCard(triggers[2].index('Goblin_Giant'))
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

                if 'Lava_Hound' in triggers[2]:
                    if triggers[1] >= 8:
                        self.bot.selectCard(triggers[2].index('Lava_Hound'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        continue
                    time.sleep(7)
                    if 'Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Witch'))
                        self.bot.placingCard1X1(275, 700)
                    elif 'Night_Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Night_Witch'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        self.bot.selectCard(triggers[2].index('Lava_Hound'))
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

                if 'Electro_Giant' in triggers[2]:
                    if triggers[1] >= 8:
                        self.bot.selectCard(triggers[2].index('Electro_Giant'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        continue
                    time.sleep(7)
                    if 'Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Witch'))
                        self.bot.placingCard1X1(275, 700)
                    elif 'Night_Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Night_Witch'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        self.bot.selectCard(triggers[2].index('Electro_Giant'))
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

                if 'Elixir_Golem' in triggers[2]:
                    if triggers[1] >= 7:
                        self.bot.selectCard(triggers[2].index('Elixir_Golem'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        continue
                    time.sleep(4)
                    if 'Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Witch'))
                        self.bot.placingCard1X1(275, 700)
                    elif 'Night_Witch' in triggers[2]:
                        self.bot.selectCard(triggers[2].index('Night_Witch'))
                        self.bot.placingCard1X1(275, 700)
                    else:
                        self.bot.selectCard(triggers[2].index('Elixir_Golem'))
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
                    if triggers[1] >= 3:
                        self.bot.selectCard(triggers[2].index('Princess'))
                        self.bot.placingCard1X1(260, 700)
                    else:
                        continue

                if 'Hog_Rider' in triggers[2]:
                    if triggers[1] >= 4:
                        self.bot.selectCard(triggers[2].index('Hog_Rider'))
                        self.bot.placingCard1X1(choice((410, 105)), 202)
                    else:
                        continue

                if 'Cannon' in triggers[2]:
                    if triggers[1] >= 4:
                        self.bot.selectCard(triggers[2].index('Cannon'))
                        self.bot.placingCard1X1(250, 515)
                    else:
                        continue

                if 'Goblin_Hut' in triggers[2]:
                    if triggers[1] >= 4:
                        self.bot.selectCard(triggers[2].index('Goblin_Hut'))
                        self.bot.placingCard1X1(250, 515)
                    else:
                        continue

                if 'Goblin_Cage' in triggers[2]:
                    if triggers[1] >= 4:
                        self.bot.selectCard(triggers[2].index('Goblin_Cage'))
                        self.bot.placingCard1X1(250, 515)
                    else:
                        continue

                if 'Barbarian_Hut' in triggers[2]:
                    if triggers[1] >= 4:
                        self.bot.selectCard(triggers[2].index('Barbarian_Hut'))
                        self.bot.placingCard1X1(250, 515)
                    else:
                        continue

                if 'Furnace' in triggers[2]:
                    if triggers[1] >= 4:
                        self.bot.selectCard(triggers[2].index('Furnace'))
                        self.bot.placingCard1X1(250, 515)
                    else:
                        continue

                if 'Bomb_Tower' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Bomb_Tower'))
                        self.bot.placingCard1X1(250, 515)
                    else:
                        continue

                if 'Tesla' in triggers[2]:
                    if triggers[1] >= 5:
                        self.bot.selectCard(triggers[2].index('Tesla'))
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
                time.sleep(1)

            elif trigger == 200:
                if slowdown_in_menu:
                    slowdown_in_menu = False
                    time.sleep(3)
                    continue
                slowdown_in_menu = True

                if self.batlle_mode == 'global':
                    self.bot.runBattleGlobal()
                elif self.batlle_mode == 'disabled':
                    self.increasing_account_number()
                    self.bot.changeAccount(self.number_account, self.total_accounts)
                    self.connection_to_parent.number_account = self.number_account
                else:
                    self.bot.runBattleMode(self.batlle_mode)
                time.sleep(1)

            elif trigger == 210:
                self.bot.goToClanChat()
                time.sleep(2)
                image = self.bot.getScreen()
                triggers = self.triggers.getTrigger(image)
                time.sleep(2)
                trigger = triggers[0]
                if trigger != 212:
                    self.bot.goToClanChat()
                    time.sleep(2)
                self.bot.requestCard(self.id_card)

            elif trigger == 211:
                self.bot.goToClanChat()
                time.sleep(2)
                image = self.bot.getScreen()
                triggers = self.triggers.getTrigger(image)
                trigger = triggers[0]
                time.sleep(2)
                if trigger != 212:
                    self.bot.goToClanChat()
                    time.sleep(2)
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

                    if self.batlle_mode == 'global':
                        self.bot.skipLimit()
                    else:
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
        self.number_account += 1
        if self.number_account == self.total_accounts:
            self.number_account = 0

    def startFarm(self):
        self.cycleStart = True
        self.main()

    def stopFarm(self):
        self.cycleStart = False
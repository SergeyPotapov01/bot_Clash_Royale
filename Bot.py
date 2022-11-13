from time import sleep

import subprocess
import random

from ADB_server import ADB_server

from loguru import logger


class Bot:
    def __init__(self, port, android):
        logger.debug(f'Bot().__init__({port})')
        self.ADB = ADB_server(port=port)
        self.android = android
        self.port = port

    def runBattleMode(self, mode):
        logger.debug(f'Bot.runBattleMode {mode}')
        self.ADB.click(500, 100)
        sleep(0.5)
        self.ADB.click(300, 320)
        sleep(0.5)
        if mode == 'mode_1':
            self.ADB.click(420, 396)
        elif mode == 'mode_2':
            self.ADB.click(420, 644)
        elif mode == '2X2':
            self.ADB.swipe(250, 800, 250, 297)
            self.ADB.click(405, 408)
        sleep(1)

    def runBattleGlobal(self):
        logger.debug('Bot.runBattleGlobal')
        self.ADB.click(180, 630)
        sleep(1)

    def runBattleEvent(self):
        logger.debug('Bot.runBattleEvent')
        self.ADB.click(280, 720)
        sleep(1)

    def rewardLimit(self):
        logger.debug('Bot.rewardLimit')
        self.ADB.click(276, 600)
        sleep(1)

    def skipLimit(self):
        logger.debug('Bot.skipLimit')
        self.ADB.click(482, 316)
        sleep(1)
        self.ADB.click(280, 900)
        sleep(1)

    def getRewardChest(self, number):
        logger.debug(f'Bot.getRewardChest {number}')
        self.ADB.click(-25 + number * 120, 780)
        sleep(1)

    def openChest(self, number):
        logger.debug(f'Bot.openChest {number}')
        self.ADB.click(-25 + number * 120, 780)
        sleep(1)

    def openChest_2(self, flag):
        logger.debug(f'Bot.openChest {flag}')
        if flag:
            self.ADB.click(470, 240)
            sleep(1)
            self.ADB.click(460, 157)
            sleep(1)
            self.ADB.click(270, 670)
            sleep(1)
        else:
            self.ADB.click(276, 625)
            sleep(1)

    def returnHome(self):
        logger.debug('Bot.returnHome')
        self.ADB.click(500, 920)
        sleep(1)
        self.ADB.click(220, 920)
        sleep(1)

    def goToClanChat(self):
        logger.debug('Bot.goToClanChat')
        self.ADB.click(371, 911)
        sleep(1)

    def openCloseClanChat(self):
        logger.debug('Bot.openCloseClanChat')
        self.ADB.click(490, 61)
        sleep(1)

    def requestCard(self, id_card):
        sleep(3)
        self.ADB.click(70, 805)
        sleep(3)
        number = int(id_card)
        line = number // 4
        slide = line // 3
        line = (number // 3) % 4
        _number = number % 4
        logger.debug(f'Bot.requestCard {id_card}, {line}, {slide}, {_number}')
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
            sleep(2)


    def swipeRequestCard(self):
        logger.debug('Bot.swipeRequestCard')
        self.ADB.swipe(250, 800, 250, 297)
        sleep(1)

    def goToEvents(self):
        logger.debug('Bot.goToEvents')
        self.ADB.click(520, 930)
        sleep(1)

    def goToDeck(self):
        logger.debug('Bot.goToDeck')
        self.ADB.click(168, 930)
        sleep(1)

    def goToShop(self):
        logger.debug('Bot.goToShop')
        self.ADB.click(80, 930)
        sleep(1)

    def placingCard1X1(self, x, y):
        logger.debug(f'Bot.placingCard1X1 x = {x}, y = {y}')
        self.ADB.click(x, y)

    def placingCard2X2(self, x, y):
        logger.debug(f'Bot.placingCard2X2 x = {x}, y = {y}')
        self.ADB.click(x, y)

    def exitBatle2X2(self):
        logger.debug('Bot.exitBatle2X2')
        self.ADB.click(74, 910)
        sleep(1)

    def exitBatle1X1(self):
        logger.debug('Bot.exitBatle1X1')
        self.ADB.click(270, 840)
        sleep(1)

    def selectCard(self, number):
        logger.debug('Bot.selectCard')
        self.ADB.click(170 + number * 100, 850)

    def setEnglishLanguage(self):
        logger.debug('Bot.setEnglishLanguage')
        sleep(3)
        self.ADB.click(500, 100)
        sleep(1)
        self.ADB.click(325, 470)
        sleep(1)
        self.ADB.click(160, 570)
        sleep(1)
        self.ADB.click(275, 235)
        sleep(1)
        self.ADB.click(370, 590)
        sleep(1)

    def reboot(self):
        logger.debug('Bot.reboot')
        self.ADB.closeCR()
        sleep(2)
        self.ADB.openCR()
        sleep(1)

    def openCR(self):
        logger.debug('Bot.openCR')
        self.ADB.openCR()
        sleep(1)

    def closeCR(self):
        logger.debug('Bot.closeCR')
        self.ADB.closeCR()
        sleep(1)

    def getScreen(self):
        logger.debug('Bot.getScreen')
        return self.ADB.getScreen()

    def changeAccount(self, number, total_accounts):
        logger.debug(f'Bot.changeAccount {number}, {total_accounts}')
        sleep(3)
        self.ADB.click(500, 90)
        sleep(3)
        self.ADB.click(250, 630)
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
        sleep(1)

    def open_pass_royale(self):
        logger.debug('Bot.open_pass_royale')
        self.ADB.click(420, 200)
        sleep(1)

    def choose_reward(self, choose):
        logger.debug(f'Bot.choose_reward {choose}')
        self.ADB.click(157 + (choose * 223), 269)
        sleep(1)

    def swipe_shop(self):
        logger.debug('Bot.swipe_shop')
        self.ADB.swipe(250, 860, 250, 100)
        sleep(3)

    def get_shop_reward(self):
        logger.debug('Bot.get_shop_reward')
        for i in range(3):
            self.ADB.swipe(250, 80, 250, 850)
            sleep(3)
        self.ADB.click(88, 350)
        sleep(2)
        self.ADB.click(270, 600)
        sleep(1)
        self.ADB.click(270, 650)
        sleep(1)

    def swipe_clan_war(self):
        logger.debug('Bot.swipe_clan_war')
        self.ADB.swipe(250, 300, 250, 450)
        sleep(3)

    def go_batlle_clan_war(self, combat):
        logger.debug('Bot.go_batlle_clan_war')
        if combat == 0:
            self.ADB.click(472, 720)
        elif combat == 1:
            self.ADB.click(472, 690)
        sleep(2)
        self.ADB.click(350, 630)
        sleep(1)

    def get_reward_clan_war(self):
        logger.debug('Bot.get_reward_clan_war')
        self.ADB.click(280, 630)
        sleep(1)

    def close_statistics_clan_war(self):
        logger.debug('Bot.close_statistics_clan_war')
        self.ADB.click(280, 570)
        sleep(1)
        self.ADB.click(268, 800)
        sleep(1)

    def swipe_clan_war_2(self):
        logger.debug('Bot.swipe_clan_war_2')
        self.ADB.swipe(250, 500, 250, 850)
        sleep(3)

    def sale_reward(self):
        logger.debug('Bot.sale_reward')
        self.ADB.click(337, 644)
        sleep(3)

    def change_deck(self, number: int):
        logger.debug('Bot.change_deck')
        self.ADB.click(157 + number * 57, 224)
        sleep(3)

    def send_emotion(self, number: int, random_=4):
        if random.randint(0, random_) == random_:
            logger.debug('Bot.send_emotion')
            self.ADB.click(51, 800)
            sleep(0.5)
            self.ADB.click(140 + 95 * number, 730)

    def get_reward_masteries(self):
        logger.debug('Bot.get_reward_masteries')
        self.ADB.click(342, 707)
        sleep(4)
        self.ADB.click(100, 280)

    def get_reward_masteries_2(self, number):
        logger.debug('Bot.get_reward_masteries_2')
        if number == 291:
            self.ADB.click(261, 705)
        elif number == 292:
            self.ADB.click(292, 498)
        elif number == 293:
            self.ADB.click(265, 625)
        elif number == 294:
            self.ADB.click(300, 707)
            pass
        sleep(4)
        self.ADB.click(350, 640)

    def close_reward_masteries(self):
        logger.debug('Bot.close_reward_masteries')
        self.ADB.click(486, 133)
        sleep(4)
        self.ADB.click(482, 161)
        sleep(4)

    def reboot_android(self):
        self.ADB.reboot()
        sleep(5)
        subprocess.Popen(self.android)
        while True:
            try:
                self.ADB = ADB_server(port=self.port)
                self.ADB.cheakInstallCR()
                sleep(5)
                print(1)
                self.openCR()
                break
            except:
                sleep(5)
        print(2)

    def random_placing_card(self):
        logger.debug('Bot.random_placing_card')
        self.selectCard(random.randint(0,3))
        self.ADB.click(random.randint(195, 345), random.randint(485, 610))

from Bot import Bot
from ImageTriggers import ImageTriggers

import time
from random import randint

from loguru import logger

logger.add('log/CrownFarm.log', format='{time} {level} {message}',
           level='INFO', rotation='1 week', compression='zip')

__version__ = '0.0.4'

if __name__ == '__main__':
    bot = Bot()
    bot.openCR()
    triggers = ImageTriggers()
    index = 0
    while True:
        t = time.time()
        image = bot.getScreen()
        trigger = triggers.getTrigger(image)

        if index == 30:
            bot.returnHome()
            bot.reboot()
            index = 0

        if index == 10:
            bot.returnHome()

        print(trigger, index)

        if trigger == 0:
            print(t - time.time())
            index += 1
            time.sleep(1)
            continue
        elif trigger == 121:
            bot.exitBatle1X1()
            time.sleep(3)
        elif trigger == 122:
            bot.exitBatle2X2()
            time.sleep(3)
        elif trigger == 123:
            bot.closeChatBatle2X2()
        elif trigger == 124:
            bot.ADB.click(400, 420)
        elif trigger <= 111 and trigger >= 100:
            bot._selectCard(randint(0, 3))
            bot._placingCard1X1()
        elif trigger == 200:
            bot._runBattleGlobal()
            time.sleep(3)
        elif trigger == 400:
            time.sleep(120)
            bot.exitBatle1X1()
        elif trigger == 500:
            bot.rewardLimit()

        index = 0
        print(t - time.time())

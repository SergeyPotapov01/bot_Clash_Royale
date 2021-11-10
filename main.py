from Bot import Bot
from ImageTriggers import ImageTriggers

import time
from random import randint

__version__ = '0.0.3'

if __name__ == '__main__':
    bot = Bot()
    triggers = ImageTriggers()
    while True:
        t = time.time()
        image = bot.getScreen()
        trigger = triggers.getTrigger(image)
        print(trigger)
        if trigger == 1:
            bot.exitBatle1X1()
        elif trigger == 2:
            bot._selectCard(randint(0, 3))
            bot._placingCard1X1()
        elif trigger == 3:
            bot._runBattleGlobal()
        elif trigger == 4:
            time.sleep(120)
            bot.exitBatle1X1()
        print(time.time() - t)

import sys
import json

from gui import Ui_MainWindow

from loguru import logger
from PyQt5 import QtWidgets


DEBUG = False

logger.add('log/CrownFarm.log', format='{time:YYYY-MM-DD HH:mm:ss} {level} {message}',
           level='INFO', rotation='1 week', compression='zip')
if DEBUG:
    logger.add('log/DEBUG.log', format='{time:HH:mm:ss} {level} {message}',
                level='DEBUG', rotation='1 week', compression='zip')

__version__ = '0.3.1'


try:
    with open('config/custom.json') as f:
        config = json.load(f)
except FileNotFoundError:
    with open('config/standart.json') as f:
        config = json.load(f)



if __name__ == '__main__':
    print(sys.version)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(config)
    ui.setupUi(MainWindow)
    ui.debugButton()
    ui.load_setting(config)
    MainWindow.show()
    sys.exit(app.exec_())
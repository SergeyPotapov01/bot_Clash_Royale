import sys

from gui import Ui_MainWindow

from loguru import logger
from PyQt5 import QtWidgets

import strategics, threading


DEBUG = False

logger.add('log/CrownFarm.log', format='{time:YYYY-MM-DD HH:mm:ss} {level} {message}',
           level='INFO', rotation='1 week', compression='zip')
if DEBUG:
    logger.add('log/DEBUG.log', format='{time:HH:mm:ss} {level} {message}',
                level='DEBUG', rotation='1 week', compression='zip')

__version__ = '0.2.7'

if __name__ == '__main__':
    print(sys.version)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.debugButton()
    ui.currentTextComboBox_change_language('English')
    MainWindow.show()
    sys.exit(app.exec_())
import sys

from gui import Ui_MainWindow

from loguru import logger
from PyQt5 import QtWidgets, QtGui

logger.add('log/CrownFarm.log', format='{time} {level} {message}',
           level='INFO', rotation='1 week', compression='zip')

__version__ = '0.1.1'


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.debugButton()
    MainWindow.show()
    sys.exit(app.exec_())

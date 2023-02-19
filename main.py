import sys
import json
from loguru import logger
from PyQt5 import QtWidgets

from gui import Ui_MainWindow


DEBUG = True

logger.add(
    "log/CrownFarm.log",
    format="{time:YYYY-MM-DD HH:mm:ss} {level} {message}",
    level="INFO",
    rotation="2 days",
    compression="zip",
)

if DEBUG:
    logger.add(
        "log/DEBUG.log",
        format="{time:HH:mm:ss} {level} {message}",
        level="DEBUG",
        rotation="2 days",
        compression="zip",
    )

__version__ = "0.3.17"

# set logger to INFO
#logger.remove()
#logger.add(sys.stderr, level="INFO")

try:
    with open("config/custom.json") as f:
        config = json.load(f)
except FileNotFoundError:
    with open("config/standart.json") as f:
        config = json.load(f)


if __name__ == "__main__":
    print(sys.version)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(config)
    ui.setupUi(MainWindow)
    ui.debugButton()
    ui.load_setting(config)
    MainWindow.show()
    sys.exit(app.exec_())

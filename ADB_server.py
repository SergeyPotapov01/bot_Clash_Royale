import os

from ppadb.client import Client as AdbClient


class ADB_server:
    def __init__(self, port: str = '5555'):
        os.system(r'"adb\adb kill-server"')
        os.system(r'"adb\adb start-server"')
        os.system(fr'"adb\adb connect 127.0.0.1:{port}"')
        client = AdbClient(host="127.0.0.1", port=5037)
        self.devices = client.devices()
        self.device = self.devices[0]

    def cheakInstallCR(self):
        packages = self.device.shell('pm list packages').split('\r\n')
        for package in packages:
            if package == 'package:com.supercell.clashroyale':
                return True
        return False

    def cheakRunCR(self):
        if self.device.get_pid('com.supercell.clashroyale'):
            return True
        return False

    def openCR(self):
        self.device.shell('monkey -p com.supercell.clashroyale -v 15')

    def closeCR(self):
        self.device.shell('am force-stop com.supercell.clashroyale')

    def click(self, x: int, y: int):
        self.device.shell(f'input tap {str(x)} {(str(y))}')

    def swipe(self, x1: int, y1: int, x2: int, y2: int):
        self.device.shell(f'input swipe {str(x1)} {(str(y1))} {str(x2)} {(str(y2))} 2000')

    def getScreen(self):
        return self.device.screencap()


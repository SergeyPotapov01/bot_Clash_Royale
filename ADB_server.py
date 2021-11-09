import os

from ppadb.client import Client as AdbClient

class ADB_server:
    def __init__(self):
        os.system(r'"C:\Program Files (x86)\Nox\bin\adb.exe start-server"')
        os.system(r'"C:\Program Files (x86)\Nox\bin\adb.exe connect 127.0.0.1:62001"')
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

    def getScreen(self):
        return self.device.screencap()

if __name__ == '__main__':
    pass
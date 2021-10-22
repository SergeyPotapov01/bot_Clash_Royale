import os
import time

from ppadb.client import Client as AdbClient


__version__ = '0.0.1'

class ADB_server:
    def __init__(self):
        #os.system(r'"C:\Program Files (x86)\Nox\bin\Nox.exe"')
        os.system(r'"ADB\adb.exe start-server"')
        os.system(r'"ADB\adb.exe connect 127.0.0.1:62001"')
        client = AdbClient(host="127.0.0.1", port=5037)
        self.device = client.devices()[0]

    def _cheakCR(self):
        packages = self.device.shell('pm list packages').split('\r\n')
        for package in packages:
            if package == 'package:com.supercell.clashroyale':
                return True
        return False

    def _openCR(self):
        self.device.shell('monkey -p com.supercell.clashroyale -v 15')

    def _closeCR(self):
        self.device.shell('am force-stop com.supercell.clashroyale')

    def battle2X2(self):
        self.device.shell('input tap 460 560')
        time.sleep(2)
        self.device.shell('input tap 480 580')
        time.sleep(1)
        # тут могла выскочить иконка на лимит наград, надо ее подтвердить
        while True:
            pass # тут логика боя, надо продумывать

    def battleGlobal(self):
        self.device.shell('input tap 260 560')
        time.sleep(1)
        # тут могла выскочить иконка на лимит наград, надо ее подтвердить
        while True:
            pass # тут логика боя, надо продумывать

if __name__ == '__main__':
    z = ADB_server()
    z._closeCR()
    print(z._cheakCR())
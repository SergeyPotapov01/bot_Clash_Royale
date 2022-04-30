import os, time

from ppadb.client import Client as AdbClient
from loguru import logger


class ADB_server:
    def __init__(self, port):
        logger.debug(f'ADB_server().__init__({port})')
        os.system(r'"adb\adb kill-server"')
        os.system(r'"adb\adb start-server"')
        time.sleep(2)
        os.system(fr'"adb\adb connect 127.0.0.1:{port}"')
        time.sleep(2)
        client = AdbClient(host="127.0.0.1", port=5037)
        devices = client.devices()
        self.device = devices[0]

    def cheakInstallCR(self):
        logger.debug('cheakInstallCR')
        packages = self.device.shell('pm list packages').split('\r\n')[0].split('\n')
        for package in packages:
            if package == 'package:com.supercell.clashroyale':
                logger.debug('cheakInstallCR -> True')
                return True
        logger.debug('cheakInstallCR -> False')
        return False

    def cheakRunCR(self):
        logger.debug('cheakRunCR')
        if self.device.get_pid('com.supercell.clashroyale'):
            logger.debug('cheakRunCR -> True')
            return True
        logger.debug('cheakRunCR -> False')
        return False

    def openCR(self):
        logger.debug('openCR')
        self.device.shell('monkey -p com.supercell.clashroyale -v 15')

    def closeCR(self):
        logger.debug('closeCR')
        self.device.shell('am force-stop com.supercell.clashroyale')

    def click(self, x: int, y: int):
        logger.debug(f'ADB_server.click x = {x} y = {y}')
        self.device.shell(f'input tap {str(x)} {(str(y))}')

    def swipe(self, x1: int, y1: int, x2: int, y2: int):
        logger.debug(f'ADB_server.swipe x1 = {x1} y1 = {y1} x2 = {x2} y2 = {y2}')
        self.device.shell(f'input swipe {str(x1)} {(str(y1))} {str(x2)} {(str(y2))} 2000')

    def getScreen(self):
        logger.debug('ADB_server.getScreen')
        return self.device.screencap()

    def add_client(self, port):
        os.system(fr'"adb\adb connect 127.0.0.1:{port}"')
        self.devices = self.client.devices()
        device = self.devices[-1]
        return device

    def reboot(self):
        self.device.shell('reboot')


class ADB_client:
    def __init__(self, port: int):
        self.device = self.add_client(port)

    def cheakInstallCR(self):
        logger.debug('cheakInstallCR')
        packages = self.device.shell('pm list packages').split('\r\n')[0].split('\n')
        for package in packages:
            if package == 'package:com.supercell.clashroyale':
                logger.debug('cheakInstallCR -> True')
                return True
        logger.debug('cheakInstallCR -> False')
        return False

    def cheakRunCR(self):
        logger.debug('cheakRunCR')
        if self.device.get_pid('com.supercell.clashroyale'):
            logger.debug('cheakRunCR -> True')
            return True
        logger.debug('cheakRunCR -> False')
        return False

    def openCR(self):
        logger.debug('openCR')
        self.device.shell('monkey -p com.supercell.clashroyale -v 15')

    def closeCR(self):
        logger.debug('closeCR')
        self.device.shell('am force-stop com.supercell.clashroyale')

    def click(self, x: int, y: int):
        logger.debug(f'ADB_server.click x = {x} y = {y}')
        self.device.shell(f'input tap {str(x)} {(str(y))}')

    def swipe(self, x1: int, y1: int, x2: int, y2: int):
        logger.debug(f'ADB_server.swipe x1 = {x1} y1 = {y1} x2 = {x2} y2 = {y2}')
        self.device.shell(f'input swipe {str(x1)} {(str(y1))} {str(x2)} {(str(y2))} 2000')

    def getScreen(self):
        logger.debug('ADB_server.getScreen')
        return self.device.screencap()

    def add_client(self, port):
        pass

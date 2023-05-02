import subprocess

import numpy as np
from PIL import Image
import io


from clashroyalebuildabot.data.constants import SCREENSHOT_WIDTH, SCREENSHOT_HEIGHT
import ADB_server

ADB = ADB_server.ADB_server(port='5555')


class Screen:
    def d__init__(self):
        # Physical size: 720x1280 -> self.width = 720, self.height = 1280
        try:
            window_size = subprocess.check_output(['adb', 'shell', 'wm', 'size'])
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"command '{e.cmd}' return with error (code {e.returncode}): {e.output}")
        window_size = window_size.decode('ascii').replace('Physical size: ', '')
        self.width, self.height = [int(i) for i in window_size.split('x')]

    @staticmethod
    def click(x, y):
        """
        Click at the given (x, y) coordinate
        """
        ADB.click(str(x), str(y))

    def take_screenshot(self):
        """
        Take a screenshot of the emulator
        """
        screenshot_bytes = ADB.getScreen()
        screenshot = Image.open(io.BytesIO(screenshot_bytes)).convert('RGB')
        screenshot = screenshot.convert('RGB').resize((SCREENSHOT_WIDTH, SCREENSHOT_HEIGHT), Image.BILINEAR)
        return screenshot


def main():
    cls = Screen()
    screenshot = cls.take_screenshot()
    #screenshot.save('screen.jpg')


if __name__ == '__main__':
    main()

import subprocess
import time

class ADBUtils:
    adb_path = r'C:\platform-tools\adb.exe'

    def enter_text_via_adb(self, text):
        time.sleep(2)
        command = f'{self.adb_path} shell input text {text}'
        subprocess.run(command, shell=True)

    def click_by_coordinates(self, x, y):
        command = f'{self.adb_path} shell input tap {x} {y}'
        subprocess.run(command, shell=True)

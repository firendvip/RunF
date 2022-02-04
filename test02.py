import time

import pyautogui
import keyboard

class RunF():
    def run_f(self):
        while 1:
            pyautogui.press('f')
            # 实操过程，f键会按的很快，短按v小概率无法断开，长按v(0.5秒以上)可以解决
            if keyboard.is_pressed('v'):
                break

    def run_w(self):
        while 1:
            pyautogui.keyDown('w')

            # pyautogui.click(button='right')
            time.sleep(1)
            if keyboard.is_pressed('s'):
                break

    def run_space(self):
        while 1:
            pyautogui.press('space')
            if keyboard.is_pressed('s'):
                break

if __name__ == '__main__':
    go_F = RunF()
    keyboard.add_hotkey('alt+f', go_F.run_f)
    keyboard.add_hotkey('alt+w', go_F.run_w)
    keyboard.add_hotkey('alt+space', go_F.run_space)
    keyboard.wait()
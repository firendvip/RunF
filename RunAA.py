import threading
import time
import pyautogui
import keyboard

# global f_thread, w_thread

class RunA():
    """按f,v断开，实操需按>0.5秒v更稳定断开"""

    def run_f(self):
        while 1:
            pyautogui.press('f')
            if keyboard.is_pressed('v') or keyboard.is_pressed('t'):
                break

    def run_w(self):
        """ 向前走，冲刺，走 """
        while 1:

            pyautogui.keyDown('w')
            pyautogui.click(button='right')
            time.sleep(1.3)
            if keyboard.is_pressed('space') or keyboard.is_pressed('t'):
                pyautogui.keyUp('w')
                break

    def run_space(self):
        """ 向前跳/快速爬山 """
        while 1:
            pyautogui.keyDown('w')
            pyautogui.press('space')
            if keyboard.is_pressed('z') or keyboard.is_pressed('t'):
                pyautogui.keyUp('w')
                break

    def key_f(self):
        """创建按f线程"""
        f_thread = threading.Thread(target=self.run_f, daemon=True)
        f_thread.start()

    def key_w(self):
        """创建按向前走+冲刺线程/赶路"""
        w_thread = threading.Thread(target=self.run_w, daemon=True)
        w_thread.start()

    def key_space(self):
        '''向前跳/快速爬山线程'''
        space_thread = threading.Thread(target=self.run_space, daemon=True)
        space_thread.start()

    def th_w(self):
        keyboard.add_hotkey('alt+w', self.key_w)
        keyboard.wait()


    def th_f(self):
        keyboard.add_hotkey('alt+f', self.key_f)
        keyboard.wait()

    def th_space(self):
        keyboard.add_hotkey('alt+space', self.key_space)
        keyboard.wait()


if __name__ == '__main__':
    go_a = RunA()

    th_WW = threading.Thread(target=go_a.th_w, daemon=True)
    th_WW.start()

    th_FF = threading.Thread(target=go_a.th_f, daemon=True)
    th_FF .start()

    th_SS = threading.Thread(target=go_a.th_space, daemon=True)
    th_SS.start()



    # 等待，不让程序直接结束
    keyboard.wait()


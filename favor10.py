import time
import pyautogui
import ys_fx

# while True:

class Favor:

    def hg10(self):
        """ 10次好感"""
        global count1
        # global count2
        pyautogui.keyDown('w')
        pyautogui.mouseDown(button='right')

        time.sleep(10)
        pyautogui.keyUp('w')
        pyautogui.mouseUp(button='right')
        time.sleep(1)
        pyautogui.press('m')  # 按m调出地图

        ys_fx.mouse_click(ys_fx.path_hgcs)  # 点击绿色传送点
        ys_fx.mouse_click(ys_fx.p_kdmd)  # 点击口袋锚点
        ys_fx.mouse_click(ys_fx.path_TY_CS)  # 点击传送

        if ys_fx.find_p(ys_fx.p_haogan, n=15): # 找到好感图片点esc
            pyautogui.press('esc')
            count1 += 1
            # print('找到好感图片，任务100%成功')
        else:
            ys_fx.key_press(ys_fx.path_RW_jm, 'esc', m=0.5)  # 如果找到人物头像，在人物界面
            # count2 += 1
            # print('未找到图片，大概率成功')

        ys_fx.mouse_click(ys_fx.p_tcyy)   # 点击退出游戏
        ys_fx.mouse_click(ys_fx.path_DJ_icon)  # 点击确定退出游戏按钮
        ys_fx.mouse_click(ys_fx.p_jryx, n=120)  # 回到进入游戏界面，点击进入游戏

# print('100%%成功次数:%d' % count1)
# print('大概率成功次数:%d' % count2)

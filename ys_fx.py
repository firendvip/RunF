import time
import keyboard
import pyautogui

# import random
path_shushu = './youyongpc/shushu.png'
Ficon = './youyongpc/f_icon.png'  # F按钮
path_TY_CS = './youyongpc/TY_CS.png'  # 通用传送按钮
path_dqsw = './youyongpc/dqsw.png'  # 稻妻声望
path_hgcs = './youyongpc/hgcs.png'  # 好感传送点
p_kdmd = './youyongpc/kdmd.png'  # 口袋锚点
path_RW_jm = './youyongpc/RW_jm.png'  # 人物左上角图标（派萌）
p_tcyy = './youyongpc/tcyy.png'  # 退出游戏
path_DJ_icon = './youyongpc/DJ_icon.png'  # 黄色圆圈确认按钮
p_jryx = './youyongpc/jryx.png'  # 进入游戏
p_Xicon = './youyongpc/Xicon.png'  # 关闭x按钮
p_hshx = './youyongpc/hshx.png'  # 黄色横线，下一个按空格
p_swz = './youyongpc/swz.png'  # 守望者突发任务
p_haogan = './youyongpc/haogan.png'
p_kjfr = './youyongpc/kjfr.png'
p_xq = './youyongpc/xq.png'
p_qh = './youyongpc/qh.png'

p_tfrw = './youyongpc/tufa.png'
p_sjwc = './youyongpc/sjwc.png'  # 突发任务完成后的绿色方块

# =================================================
p_md = './youyongpc/md_swjl.png'
p_1 = './youyongpc/1.png'
p_2 = './youyongpc/2.png'
p_3 = './youyongpc/3.png'
p_4 = './youyongpc/4.png'
p_5 = './youyongpc/5.png'
p_6 = './youyongpc/6.png'
p_7 = './youyongpc/7.png'
p_8 = './youyongpc/8.png'
p_9 = './youyongpc/9.png'
p_10 = './youyongpc/10.png'
p_11 = './youyongpc/11.png'


# ==================================================

# 循环找图并单击

def mouse_click(path, area= None, num=0.7, n=20 ):
    """ 循环找图并单击 """

    s = time.perf_counter()  # 获取系统当前时间
    while True:
        xy = pyautogui.locateCenterOnScreen(path, region = area, confidence=num)
        s1 = time.perf_counter()

        # 判断xy不为None，则说明找到了图，然后进行后续操作，操作完断开
        if xy is not None:
            x, y = xy
            pyautogui.moveTo(x, y)
            pyautogui.click()
            # print(path, '点击成功')
            break

        # 超时未找到图断开
        if s1 - s > n:
            # print('超过%d秒未找到图片停止找图' % n)
            break

        if keyboard.is_pressed('t'):
            # print('已断开')
            break








# 找图并按键
def key_press(path, key=None, n=30, num=0.7, m=0.5):
    """
    :param path: 图片地址
    :param key: 键盘按键
    :param n: 超时时间
    :param num: 模糊成都 0-1，一般未0.9
    :return: 按键执行，和是否成功日志
    :param m: 找到图片后的停留时间，实操发现找到图片，过快按键，无法触发交互。
    """
    s = time.perf_counter()
    while True:
        xy = pyautogui.locateCenterOnScreen(path, confidence=num)
        s1 = time.perf_counter()
        if xy is not None:
            # print(path, '找到图片')
            time.sleep(m)
            pyautogui.press(key)
            # print(key, '按键成功')
            break

        if s1 - s > n:
            # print('超过%d秒未找到图片' % n)
            break

        if keyboard.is_pressed('t'):
            break


# 找图 找到返回1 未找到返回0
def find_p(path, n=30, num=0.7):
    s = time.perf_counter()
    while True:
        xy = pyautogui.locateCenterOnScreen(path, confidence=num)
        s1 = time.perf_counter()
        if xy is not None:
            # print(path, '找到图片')
            # break
            return True

        if s1 - s > n:
            # print('超过%d秒未找到图片' % n)
            return False
            # break

        if keyboard.is_pressed('t'):
            break


# 拖动
def drag_to(path, x, y, t=0.5):
    mouse_click(path)
    pyautogui.drag(x, y, t, button='left')

# 长按某个按键
def keyDoUp(s_key, s_time):
    pyautogui.keyDown(s_key)
    time.sleep(s_time)
    pyautogui.keyUp(s_key)

# 人物跑
def keyRand(r_key, r_time):
    pyautogui.keyDown(r_key)
    time.sleep(0.5)
    pyautogui.mouseDown(button='right')
    time.sleep(r_time)
    pyautogui.keyUp(r_key)
    pyautogui.mouseUp(button='right')


def cjyx():
    """ 退出游戏重进 """
    key_press(path_RW_jm, 'esc', m=0.5)  # 如果找到人物头像，在人物界面
    mouse_click(p_tcyy)  # 点击退出游戏
    mouse_click(path_DJ_icon)  # 点击确定退出游戏按钮
    mouse_click(p_jryx, n=120)  # 回到进入游戏界面，点击进入游戏


# 传回锚点
def back_md():
    pyautogui.press('m')  # 按m调出地图
    mouse_click(path_hgcs)  # 点击绿色传送点
    mouse_click(p_kdmd)  # 点击口袋锚点
    mouse_click(path_TY_CS)  # 点击传送




# 长按摸个键然后放开
def long_press(key,l_time):
    pyautogui.keyDown(key)
    time.sleep(l_time)
    pyautogui.keyUp(key)


def run_w(w_time):
    """ 向前跑 """
    pyautogui.keyDown('w')
    pyautogui.mouseDown(button='right')
    time.sleep(w_time)
    pyautogui.mouseUp(button='right')
    pyautogui.keyUp('w')

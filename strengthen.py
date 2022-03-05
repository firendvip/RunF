import win32con
import win32gui
import win32print
import ys_fx


class QH():
    def get_real_resolution(self):
        """获取真实的分辨率"""
        global w, h ,w1,h1
        # 获取主屏句柄
        hDC = win32gui.GetDC(0)
        # 横向分辨率  # GetDeviceCaps(句柄，指定返回参数类型)
        w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
        # 纵向分辨率
        h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
        # 获取屏幕中间点坐标
        w1 = int(w/2)
        h1 = int(h/2)

    def qh(self):
        """切为4个区域提高识别效率"""
        ys_fx.mouse_click(ys_fx.p_kjfr,area=(w1,h1,w,h))
        ys_fx.mouse_click(ys_fx.path_DJ_icon,area=(w1,h1,w,h))
        ys_fx.mouse_click(ys_fx.p_xq, area=(0,0,w1,h1))
        ys_fx.mouse_click(ys_fx.p_qh, area=(0,0,w1,h1))

if __name__ == '__main__':
    test = QH()
    test.get_real_resolution()
    test.qh()
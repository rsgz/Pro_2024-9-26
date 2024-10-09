import pyautogui
import pygetwindow as gw
import time

# pip install pyautogui -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install pygetwindow -i https://pypi.tuna.tsinghua.edu.cn/simple

def activate_window_under_mouse():
    while True:
        # 获取当前鼠标位置
        x, y = pyautogui.position()

        # 获取鼠标下方的窗口
        window_under_mouse = gw.getWindowsAt(x, y)[0] if gw.getWindowsAt(x, y) else None

        # 如果存在窗口并且它不是当前活动窗口，则激活它
        if window_under_mouse and window_under_mouse != gw.getActiveWindow():
            try:
                window_under_mouse.activate()
            except:
                pass  # 如果无法激活窗口，则忽略异常
        time.sleep(0.1)


activate_window_under_mouse()

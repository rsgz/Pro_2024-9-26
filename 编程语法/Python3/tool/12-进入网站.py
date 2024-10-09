import pyautogui
import time
from pynput import keyboard

# pip install pyautogui -i https://pypi.tuna.tsinghua.edu.cn/simple
# pip install pynput -i https://pypi.tuna.tsinghua.edu.cn/simple



def s():
    # pyautogui.hotkey('ctrl', 'c')
    # time.sleep(0.1)
    pyautogui.click(1982, 16)
    time.sleep(0.1)
    pyautogui.rightClick()
    time.sleep(0.1)
    pyautogui.click(2077, 366)  # 关闭其他标签

    pyautogui.click(2352, 102)
    time.sleep(0.1)
    pyautogui.hotkey('alt', 'd')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

s()
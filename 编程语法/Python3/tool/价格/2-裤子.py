from tool.find_pic import find_pic_click_center_keep
import pyautogui
import keyboard,time
r"""

pip install keyboard -i https://mirrors.aliyun.com/pypi/simple
pyautogui.hotkey('space')
pyautogui.hotkey('alt', 'd')
pyautogui.click(1982, 16)
pyautogui.rightClick()
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'v')
pyautogui.click(x=click_point[0], y=click_point[1], duration=0.1)
keyboard.write('Hello, World!', delay=0)
"""


small = r"D:\0-code\tool\价格\img\2\1-分类.png"
find_pic_click_center_keep(small=small, jieshu_tezheng=None, info='1', xiangsidu=0.98)
small = r"D:\0-code\tool\价格\img\2\2-下装.png"
find_pic_click_center_keep(small=small, jieshu_tezheng=None, info='1', xiangsidu=0.98)

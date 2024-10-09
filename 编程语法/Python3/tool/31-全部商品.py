import pyautogui,time
from find_pic import find_pic_click_center_keep
import keyboard

r"""
pip install keyboard -i https://mirrors.aliyun.com/pypi/simple
D:\0-code\tool\dc\img\quan_bu_shang_pin
"""

def a(s):
    return r"D:\0-code\tool\dc\img\quan_bu_shang_pin\d{}.png".format(s)

find_pic_click_center_keep(small=a(1), jieshu_tezheng=None, info='1', xiangsidu=0.98)
time.sleep(0.5)
find_pic_click_center_keep(small=a(2), jieshu_tezheng=None, info='2', xiangsidu=0.98)
time.sleep(0.5)
find_pic_click_center_keep(small=a(3), jieshu_tezheng=None, info='3', xiangsidu=0.98)
time.sleep(0.5)
find_pic_click_center_keep(small=a(4), jieshu_tezheng=None, info='4', xiangsidu=0.98)
time.sleep(0.5)
find_pic_click_center_keep(small=a(5), jieshu_tezheng=None, info='5', xiangsidu=0.98)
# pyautogui.hotkey('space')
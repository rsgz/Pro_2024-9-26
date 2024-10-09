import pyautogui
from find_pic import find_pic_click_center_keep
import keyboard

r"""
pip install keyboard -i https://mirrors.aliyun.com/pypi/simple
"""



def callback(e):
    if e.name == 'esc':
        return 'stop'

small=r"D:\Backup\Downloads\b3.jpg"
n=0
while 1:
    find_pic_click_center_keep(small=small, jieshu_tezheng=None, info='上传', xiangsidu=0.5)
    pyautogui.hotkey('space')
    n+=1
    if n>20:
        break
    if keyboard.on_press(callback)=='stop':
        break
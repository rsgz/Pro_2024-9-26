import cv2, pyautogui
from find_pic import find_pic_click_center_pianyixy_keep
import time

path = r"D:\Backup\Downloads\1-click\意外停止"
p = lambda pic:"{}\\".format(path)+str(pic)+".png"

# while 1:
#     time.sleep(0.1)
#     find_pic_click_center_keep(small=p(1), jieshu_tezheng=None, info='1', xiangsidu=0.90)


while 1:
    find_pic_click_center_pianyixy_keep(small=p(2), pianliangxy=(150+30+50+60+10,0), jieshu_tezheng=None, info=None, xiangsidu=0.9, time_sleep=0.1)
    time.sleep(0.05)
    pyautogui.press('space')
    time.sleep(0.05)
    pyautogui.moveTo(1, 1)  # 移动
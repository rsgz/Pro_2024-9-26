import cv2, pyautogui
from find_pic import find_pic_click_center_pianyixy_keep
import time

path = r"D:\Backup\Downloads\1-click\数据错误"
p = lambda pic:"{}\\".format(path)+str(pic)+".png"

# while 1:
#     time.sleep(0.1)
#     find_pic_click_center_keep(small=p(1), jieshu_tezheng=None, info='1', xiangsidu=0.90)


while 1:
    find_pic_click_center_pianyixy_keep(small=p(1), pianliangxy=(92,65), jieshu_tezheng=None, info=None, xiangsidu=0.85,time_sleep=0.1)
    time.sleep(0.05)
    pyautogui.moveTo(1, 1)  # 移动
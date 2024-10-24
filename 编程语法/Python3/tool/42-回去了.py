from find_pic import find_pic_click_center_keep
import time

p = lambda pic:r"D:\Backup\Downloads\1-click\回去了\\"+str(pic)+".png"

time.sleep(0.1)
find_pic_click_center_keep(small=p(1), jieshu_tezheng=None, info='1', xiangsidu=0.98)
time.sleep(0.1)
find_pic_click_center_keep(small=p(2 ), jieshu_tezheng=None, info='1', xiangsidu=0.98)
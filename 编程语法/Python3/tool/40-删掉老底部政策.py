from find_pic import find_pic_click_center_keep
import time

p = lambda pic:r"D:\Backup\Downloads\1-click\shanchu_底部政策\\"+str(pic)+".png"

# 清空底部政策
find_pic_click_center_keep(small=p(1), jieshu_tezheng=None, info='1', xiangsidu=0.98)
time.sleep(0.5)
find_pic_click_center_keep(small=p(2), jieshu_tezheng=None, info='1', xiangsidu=0.98)
time.sleep(0.5)
find_pic_click_center_keep(small=p(2.1), jieshu_tezheng=None, info='1', xiangsidu=0.98)
time.sleep(0.5)
find_pic_click_center_keep(small=p(3), jieshu_tezheng=None, info='1', xiangsidu=0.98)
time.sleep(1.2)
# 文章管理
find_pic_click_center_keep(small=p(4), jieshu_tezheng=None, info='1', xiangsidu=0.98)
time.sleep(0.5)
find_pic_click_center_keep(small=p(5), jieshu_tezheng=None, info='1', xiangsidu=0.98)
time.sleep(0.5)
find_pic_click_center_keep(small=p(6), jieshu_tezheng=None, info='1', xiangsidu=0.98)
time.sleep(0.5)
find_pic_click_center_keep(small=p(2.1), jieshu_tezheng=None, info='1', xiangsidu=0.98)
time.sleep(1.8)
find_pic_click_center_keep(small=p(7), jieshu_tezheng=None, info='1', xiangsidu=0.98)
time.sleep(0.5)
find_pic_click_center_keep(small=p(8), jieshu_tezheng=None, info='1', xiangsidu=0.98)
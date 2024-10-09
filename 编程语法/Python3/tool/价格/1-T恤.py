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


# small = r"D:\0-code\tool\价格\img\1-请选择.png"
# find_pic_click_center_keep(small=small, jieshu_tezheng=None, info='1', xiangsidu=0.98)
# small = r"D:\0-code\tool\价格\img\2-女装.png"
# find_pic_click_center_keep(small=small, jieshu_tezheng=None, info='1', xiangsidu=0.98)
#
# small = r"D:\0-code\tool\价格\img\3-上装.png"
# find_pic_click_center_keep(small=small, jieshu_tezheng=None, info='1', xiangsidu=0.98)
# small = r"D:\0-code\tool\价格\img\4-T恤.png"
# find_pic_click_center_keep(small=small, jieshu_tezheng=None, info='1', xiangsidu=0.98)
small = r"D:\0-code\tool\价格\img\12-泳装.png"
find_pic_click_center_keep(small=small, jieshu_tezheng=None, info='1', xiangsidu=0.98)

small = r"D:\0-code\tool\价格\img\5-随机修改价格.png"
find_pic_click_center_keep(small=small, jieshu_tezheng=None, info='1', xiangsidu=0.98)
small = r"D:\0-code\tool\价格\img\6-浮动下限.png"
find_pic_click_center_keep(small=small, jieshu_tezheng=None, info='1', xiangsidu=0.98)
keyboard.write('80', delay=0)

# small = r"D:\0-code\tool\价格\img\11-空白.png"
# find_pic_click_center_keep(small=small, jieshu_tezheng=None, info='1', xiangsidu=0.98)

small = r"D:\0-code\tool\价格\img\7-浮动上限.png"
find_pic_click_center_keep(small=small, jieshu_tezheng=None, info='1', xiangsidu=0.98)

keyboard.write('120', delay=0)
small = r"D:\0-code\tool\价格\img\8-修改售价.png"
find_pic_click_center_keep(small=small, jieshu_tezheng=None, info='1', xiangsidu=0.98)
small = r"D:\0-code\tool\价格\img\9-确定.png"
find_pic_click_center_keep(small=small, jieshu_tezheng=None, info='1', xiangsidu=0.98)
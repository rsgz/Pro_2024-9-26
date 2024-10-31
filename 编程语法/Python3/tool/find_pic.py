import cv2, pyautogui
import numpy
import numpy as np
import re
import PIL.ImageGrab
import time
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import win32api, win32con

r'''
pip install pyautogui -i https://mirrors.aliyun.com/pypi/simple
pyautogui.click(x=p2[0], y=p2[1], duration=0.1)  # 点击
pyautogui.moveTo(click_point[0], click_point[1])  # 移动
pyautogui.hotkey('win', 'v')
pyautogui.sleep(1)
pyautogui.press('enter')
pyautogui.press('space')
pyautogui.press('down')
pyautogui.typewrite("11111")
pyautogui.typewrite()  # 避免使用
pyautogui.click(100, 100)
pyautogui.click(2352, 102)
pyautogui.rightClick()
pyautogui.press('enter')
pyautogui.hotkey('alt', 'd')
pyautogui.hotkey('ctrl', 'v', interval = 0.15)

import pyperclip
pyperclip.copy('sometext')
pyperclip.paste()
'''

s = time.sleep


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(r"函数 {} 执行时间：{} 秒".format(func.__name__,execution_time))
        return result
    return wrapper


# 判断是否是中文路径
def is_contain_chinese(path):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    match = pattern.search(path)
    return match is not None


# 读取中文路径 灰度图 0
def image_read_from_chinese_path(image_file_name, mode):
    r"""
    mode 0 灰度图
    mode 1 彩色图
    mode -1 保留其原始通道和深度信息
    """
    if is_contain_chinese(path=image_file_name):
        image_numpy_data = cv2.imdecode(np.fromfile(image_file_name, dtype=np.uint8), mode)
        return image_numpy_data
    else:
        return cv2.imread(image_file_name, mode)


# 截图函数
def gdiScreenCapture():
    screen = PIL.ImageGrab.grab()  # 使用PIL进行屏幕截图
    img_bgr = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)  # 转换为BGRA格式
    # img_bgr = img_bgra[:, :, :3]  # 提取BGR通道
    return img_bgr


# 截图函数
def jietu_save(save_path):
    screen = PIL.ImageGrab.grab()  # 使用PIL进行屏幕截图
    screen.save(save_path)


# 截图函数
def jietu_return():
    return PIL.ImageGrab.grab()  # 使用PIL进行屏幕截图


def add_text_logo():
    pass


# 截屏并且添加文字logo
def jiepin_add_text_logo_save(text, font_chicun=50, loc=(0, 0), draw_color=(255, 255, 255), save_path=""):
    # 设置字体，如果没有，也可以不设置
    # font_chicun = 50
    font = ImageFont.truetype("C:\Windows\Fonts\Deng.ttf", font_chicun)

    # 打开底版图片
    im1 = jietu_return()

    # 在图片上添加文字 1
    draw = ImageDraw.Draw(im1)
    draw_content = text
    # color = (255, 255, 255)
    # draw_color = (255, 255, 255)
    # draw_loc = (0, 0)
    draw.text(loc, draw_content, draw_color, font=font)
    # 保存
    im1.save(save_path)


# 框出&保存
@timer
def find_rectangle_save(small, big):
    # 读入图片 big1.png是背景大图;  small.png是需要寻找的小图（格式.jpg .png都行）
    if isinstance(big, numpy.ndarray):
        print("图片数组")
        img3 = big
        img = cv2.cvtColor(big, cv2.COLOR_BGR2GRAY)  # 图像灰度化
    else:
        print("是图片")
        img = cv2.imread(big, 0)  # 0 读入灰度图  大图
        img3 = cv2.imread(big, 1)  # 1 读入彩色图  大图

    # template = cv2.imread(small, 0)  # 小图
    template = image_read_from_chinese_path(image_file_name=small, mode=0)  # 小图
    w, h = template.shape[::-1]  # 高宽转成  宽高

    method = cv2.TM_CCOEFF_NORMED
    # 应用模板算法，返回一系列指标
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 从res中挑选最优指标

    if max_val < 0.98:
        return
    else:
        print("相似度:", max_val)

    # 注意 TM_SQDIFF 或者 TM_SQDIFF_NORMED 算法使用最小值为最优
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 显示图片
    cv2.rectangle(img3, top_left, bottom_right, (0, 0, 255), 1)  # 画出矩形框
    cv2.imwrite('1.png', img3, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


# 框出&展示
@timer
def find_rectangle_show(small, big):
    # 读入图片 big1.png是背景大图;  small.png是需要寻找的小图（格式.jpg .png都行）
    if isinstance(big, numpy.ndarray):
        img3 = big
        img = cv2.cvtColor(big, cv2.COLOR_BGR2GRAY)  # 图像灰度化
    else:
        print("是图片")
        img = cv2.imread(big, 0)  # 0 读入灰度图  大图
        img3 = cv2.imread(big, 1)  # 1 读入彩色图  大图

    # template = cv2.imread(small, 0)  # 小图
    template = image_read_from_chinese_path(image_file_name=small, mode=0)  # 小图
    w, h = template.shape[::-1]  # 高宽转成  宽高

    method = cv2.TM_CCOEFF_NORMED
    # 应用模板算法，返回一系列指标
    res = cv2.matchTemplate(img, template, method)
    # print("res",res)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 从res中挑选最优指标
    # print("min_val, max_val, min_loc, max_loc",min_val, max_val, min_loc, max_loc)
    if max_val < 0.98:
        return
    else:
        print("相似度:", max_val)

    # 注意 TM_SQDIFF 或者 TM_SQDIFF_NORMED 算法使用最小值为最优
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 显示图片
    cv2.rectangle(img3, top_left, bottom_right, (0, 0, 255), 1)  # 画出矩形框
    cv2.namedWindow("show", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("show", img3)
    cv2.waitKey(0)
    click_point = tuple((x + y) / 2 for x, y in zip(top_left, bottom_right))
    return click_point


# 移动
@timer
def find_pic_move_center(small, big, xiangsidu=0.98):
    # 读入图片 big1.png是背景大图;  small.png是需要寻找的小图（格式.jpg .png都行）
    if isinstance(big, numpy.ndarray):
        print("图片数组")
        img3 = big
        img = cv2.cvtColor(big, cv2.COLOR_BGR2GRAY)  # 图像灰度化
    else:
        print("是图片")
        img = cv2.imread(big, 0)  # 0 读入灰度图  大图
        img3 = cv2.imread(big, 1)  # 1 读入彩色图  大图

    # template = cv2.imread(small, 0)  # 小图
    template = image_read_from_chinese_path(image_file_name=small, mode=0)  # 小图
    w, h = template.shape[::-1]  # 高宽转成  宽高

    method = cv2.TM_CCOEFF_NORMED
    # 应用模板算法，返回一系列指标
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 从res中挑选最优指标

    if max_val < xiangsidu:
        return
    else:
        print("相似度:", max_val)

    # 注意 TM_SQDIFF 或者 TM_SQDIFF_NORMED 算法使用最小值为最优
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 中心点
    click_point = tuple((x + y) / 2 for x, y in zip(top_left, bottom_right))
    pyautogui.moveTo(click_point[0], click_point[1])  # 移动
    # pyautogui.click(x=click_point[0], y=click_point[1], duration=0.1)  # 点击

    # print(click_point,type(click_point))
    return click_point

# 点击
@timer
def find_pic_click_center(small, big, xiangsidu=0.98, info=None):
    if info:
        print(info)
    # 读入图片 big1.png是背景大图;  small.png是需要寻找的小图（格式.jpg .png都行）
    if isinstance(big, numpy.ndarray):
        print("图片数组", end="")
        img3 = big
        img = cv2.cvtColor(big, cv2.COLOR_BGR2GRAY)  # 图像灰度化
    else:
        print("是图片", end="")
        img = cv2.imread(big, 0)  # 0 读入灰度图  大图
        img3 = cv2.imread(big, 1)  # 1 读入彩色图  大图

    # template = cv2.imread(small, 0)  # 小图
    template = image_read_from_chinese_path(image_file_name=small, mode=0)  # 小图
    w, h = template.shape[::-1]  # 高宽转成  宽高

    method = cv2.TM_CCOEFF_NORMED
    # 应用模板算法，返回一系列指标
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 从res中挑选最优指标

    if max_val < xiangsidu:
        return
    else:
        print("相似度:", max_val)

    # 注意 TM_SQDIFF 或者 TM_SQDIFF_NORMED 算法使用最小值为最优
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 中心点
    click_point = tuple((x + y) / 2 for x, y in zip(top_left, bottom_right))
    # pyautogui.moveTo(click_point[0], click_point[1])  # 移动
    pyautogui.click(x=click_point[0], y=click_point[1], duration=0.1)  # 点击

    # print(click_point, type(click_point))
    return click_point

# 找图且偏移
@timer
def find_pic_move_xy(small, big, pianliangxy,xiangsidu=0.98):
    # from find_pic import find_pic_click_center_keep,gdiScreenCapture,find_pic_move_xy
    # find_pic_move_xy(small=p(1), big=gdiScreenCapture(), pianliangxy=(92,-68),xiangsidu=0.90)
    # print("find_pic_move_xy")
    # 读入图片 big1.png是背景大图;  small.png是需要寻找的小图（格式.jpg .png都行）
    if isinstance(big, numpy.ndarray):
        print("图片数组")
        img3 = big
        img = cv2.cvtColor(big, cv2.COLOR_BGR2GRAY)  # 图像灰度化
    else:
        print("是图片")
        img = cv2.imread(big, 0)  # 0 读入灰度图  大图
        img3 = cv2.imread(big, 1)  # 1 读入彩色图  大图

    # template = cv2.imread(small, 0)  # 小图
    template = image_read_from_chinese_path(image_file_name=small, mode=0)  # 小图
    w, h = template.shape[::-1]  # 高宽转成  宽高

    method = cv2.TM_CCOEFF_NORMED
    # 应用模板算法，返回一系列指标
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 从res中挑选最优指标

    if max_val < xiangsidu:
        print("找不到图片 建议调整  降低相似度")
        return
    else:
        print("相似度:", max_val)

    # 注意 TM_SQDIFF 或者 TM_SQDIFF_NORMED 算法使用最小值为最优
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 中心点
    click_point = tuple((x + y) / 2 for x, y in zip(top_left, bottom_right))
    center_p = tuple((x + y) / 2 for x, y in zip(top_left, bottom_right))
    # 中心点 不用了  直接用我指定的点
    click_point = (center_p[0]+pianliangxy[0],center_p[1]+pianliangxy[1])
    pyautogui.moveTo(click_point[0], click_point[1])  # 移动
    # pyautogui.click(x=click_point[0], y=click_point[1], duration=0.1)  # 点击

    print(click_point,type(click_point))
    return click_point

# 持久当前范围寻找
@timer
def find_pic_click_center_keep(small, jieshu_tezheng=None, info=None, xiangsidu=0.98):
    r"""
    只能当前屏幕 持久寻找
    """
    while 1:
        try:
            p2 = find_pic_click_center(small=small, big=gdiScreenCapture(), xiangsidu=xiangsidu)
            if info:
                print(info)
            # p2 = find_rectangle_show(small = shop, big=gdiScreenCapture())
            if p2:
                return p2  # click_point
            elif jieshu_tezheng:
                if find_have(small=jieshu_tezheng):
                    return 1
        except:
            pass

# 持久当前范围寻找 + 点击偏移量
@timer
def find_pic_click_center_pianyixy_keep(small, pianliangxy, jieshu_tezheng=None, info=None, xiangsidu=0.98,time_sleep=0.01):
    r"""
    只能当前屏幕 持久寻找  可以添加偏移量
    期望 点击之后 能回到原来位置
    from find_pic import find_pic_click_center_keep,gdiScreenCapture,find_pic_move_xy
    find_pic_move_xy(small=p(1), big=gdiScreenCapture(), pianliangxy=(92,-68),xiangsidu=0.90)
    find_pic_click_center_pianyixy_keep(small="001.png", pianliangxy=(92,-68), jieshu_tezheng=None, info=None, xiangsidu=0.98)
    find_pic_click_center_pianyixy_keep(small=p(1), pianliangxy=(120,0), jieshu_tezheng=None, info=None, xiangsidu=0.90,time_sleep=0.01)
    """
    while 1:
        time.sleep(time_sleep)
        try:
            p2 = find_pic_move_xy(small=small, big=gdiScreenCapture(), pianliangxy=(pianliangxy[0],-pianliangxy[1]),xiangsidu=xiangsidu)
            if info:
                print(info)
            # p2 = find_rectangle_show(small = shop, big=gdiScreenCapture())
            if p2:
                pyautogui.click(x=p2[0], y=p2[1], duration=0.1)  # 点击
                return p2  # click_point
            elif jieshu_tezheng:
                if find_have(small=jieshu_tezheng):
                    return 1
        except:
            pass

# 持久当前范围寻找 + 点击偏移量+回到原来位置
@timer
def find_pic_click_center_pianyixy_keep_back(small, pianliangxy, jieshu_tezheng=None, info=None, xiangsidu=0.98,time_sleep=0.01):
    r"""
    只能当前屏幕 持久寻找  可以添加偏移量
    期望 点击之后 能回到原来位置
    from find_pic import find_pic_click_center_keep,gdiScreenCapture,find_pic_move_xy
    find_pic_move_xy(small=p(1), big=gdiScreenCapture(), pianliangxy=(92,-68),xiangsidu=0.90)
    find_pic_click_center_pianyixy_keep(small="001.png", pianliangxy=(92,-68), jieshu_tezheng=None, info=None, xiangsidu=0.98)
    find_pic_click_center_pianyixy_keep(small=p(1), pianliangxy=(120,0), jieshu_tezheng=None, info=None, xiangsidu=0.90,time_sleep=0.01)
    """
    while 1:
        try:
            p2 = find_pic_move_xy(small=small, big=gdiScreenCapture(), pianliangxy=(pianliangxy[0],-pianliangxy[1]),xiangsidu=xiangsidu)
            if info:
                print(info)
            # p2 = find_rectangle_show(small = shop, big=gdiScreenCapture())
            if p2:
                pyautogui.click(x=p2[0], y=p2[1], duration=0.1)  # 点击
                return p2  # click_point
            elif jieshu_tezheng:
                if find_have(small=jieshu_tezheng):
                    return 1
        except:
            pass

        time.sleep(time_sleep)

# 如果找到目标
@timer
def find_have(small):
    r"""
    只能当前屏幕 持久寻找
    """

    def find(small, big):
        # 读入图片 big1.png是背景大图;  small.png是需要寻找的小图（格式.jpg .png都行）
        if isinstance(big, numpy.ndarray):
            print("图片数组")
            img3 = big
            img = cv2.cvtColor(big, cv2.COLOR_BGR2GRAY)  # 图像灰度化
        else:
            print("是图片")
            img = cv2.imread(big, 0)  # 0 读入灰度图  大图
            img3 = cv2.imread(big, 1)  # 1 读入彩色图  大图

        # template = cv2.imread(small, 0)  # 小图
        template = image_read_from_chinese_path(image_file_name=small, mode=0)  # 小图
        w, h = template.shape[::-1]  # 高宽转成  宽高

        method = cv2.TM_CCOEFF_NORMED
        # 应用模板算法，返回一系列指标
        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 从res中挑选最优指标

        if max_val < 0.98:
            return
        else:
            print("相似度:", max_val)

        # 注意 TM_SQDIFF 或者 TM_SQDIFF_NORMED 算法使用最小值为最优
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        # 中心点
        click_point = tuple((x + y) / 2 for x, y in zip(top_left, bottom_right))
        # pyautogui.moveTo(click_point[0], click_point[1])  # 移动
        # pyautogui.click(x=click_point[0], y=click_point[1], duration=0.1)  # 点击

        # print(click_point,type(click_point))
        return click_point

    while 1:
        try:
            p2 = find(small=small, big=gdiScreenCapture())
            if p2:
                return p2  # click_point
        except:
            pass


@timer
def find_have_one(small, xiangsidu=0.98):
    r"""
    只能当前屏幕 持久寻找
    """

    def find(small, big):
        # 读入图片 big1.png是背景大图;  small.png是需要寻找的小图（格式.jpg .png都行）
        if isinstance(big, numpy.ndarray):
            print("图片数组")
            img3 = big
            img = cv2.cvtColor(big, cv2.COLOR_BGR2GRAY)  # 图像灰度化
        else:
            print("是图片")
            img = cv2.imread(big, 0)  # 0 读入灰度图  大图
            img3 = cv2.imread(big, 1)  # 1 读入彩色图  大图

        # template = cv2.imread(small, 0)  # 小图
        template = image_read_from_chinese_path(image_file_name=small, mode=0)  # 小图
        w, h = template.shape[::-1]  # 高宽转成  宽高

        method = cv2.TM_CCOEFF_NORMED
        # 应用模板算法，返回一系列指标
        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 从res中挑选最优指标

        if max_val < xiangsidu:
            return
        else:
            print("相似度:", max_val)

        # 注意 TM_SQDIFF 或者 TM_SQDIFF_NORMED 算法使用最小值为最优
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        # 中心点
        click_point = tuple((x + y) / 2 for x, y in zip(top_left, bottom_right))
        return click_point

    try:
        p2 = find(small=small, big=gdiScreenCapture())
        if p2:
            return p2  # click_point
    except:
        print("寻找失败")


if __name__ == '__main__':
    small = "img_1.png"
    big = "img_2.png"
    # find_rectangle_save(small, big)  # 执行时间：0.18550801277160645 秒
    # find_rectangle_show(small, big)  # 执行时间：0.18550801277160645 秒
    # find_pic_click_center(small, big)  # 执行时间：0.12166190147399902 秒
    im1 = r"D:\0-code\rust_pro\rust_pro_git\编程语法\Python3\tool\dc\img\kucun\001.png"
    find_pic_click_center_keep(small=im1, jieshu_tezheng=None, info='1', xiangsidu=0.98)

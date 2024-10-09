from PIL import Image, ImageChops
import shutil, os, time
j=os.path.join


# 单张切图
def qietu(input_pic, output_pic):
    r"""
    去除图片边框
    input_pic: 输入图片路径 带文件名
    output_pic: 输出图片路径 不带文件名
    """
    print('正在切图：---> {}'.format(input_pic))
    imgIn = Image.open(input_pic)
    bg = Image.new(imgIn.mode, imgIn.size, imgIn.getpixel((0, 0)))
    diff = ImageChops.difference(imgIn, bg)

    # diff=ImageChops.add(diff,diff, 2.0,-10) # 可选，会去的更干净，副作用是误伤
    # 返回左上角和右下角的坐标 (left, upper, right, lower)
    bbox = diff.getbbox()
    if bbox:
        imgIn.crop(bbox).save(output_pic, quality=100, subsampling=0)
    else:
        shutil.copyfile(input_pic, output_pic)

def qie_tu_s(fu,new):
    # fu = r"C:\Users\Administrator\Desktop\pic\夹克\夹克 png"
    # new = r"C:\Users\Administrator\Desktop\pic\夹克\夹克切图"
    os.chdir(fu)
    pic_l = os.listdir(fu)
    for i,im in enumerate(pic_l):
        qietu(input_pic=im, output_pic=j(new,str(i)+'.png'))
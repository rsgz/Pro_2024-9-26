from PIL import Image, ImageChops
import shutil, os, time,random
import ffmpy
from multiprocessing import Pool

r"""
pip install ffmpy -i https://mirrors.aliyun.com/pypi/simple
"""


j=os.path.join

# 初始化
def chushihua(base_dir, dalei):
    os.chdir(base_dir)
    mulu_s = ["0-{} 原图".format(dalei), "1-{}-转格式jpg".format(dalei), "2-{} 抠图--png".format(dalei), "3-{} 切图".format(
        dalei), "4-{} h680".format(dalei), "5-{} 拼图".format(dalei)]
    for mu in mulu_s:
        if not os.path.exists(mu):
            print("创建了{}".format(mu))
            os.makedirs(mu)
        else:
            print(mu,"已经存在了!!!")



def format_pic(pic, geshi):
    r"""
    format_pic(pic=pic, geshi='jpg')
    """
    old_pic = pic

    if geshi not in old_pic and "Thumbs.db" not in old_pic and ".ini" not in old_pic:
        try:
            print("old ",old_pic)
            new_pic = os.path.splitext(old_pic)[0] + '.' + geshi
            print('new ',new_pic)
            ffmpeg_path=r"D:\58-ffmpeg\ffmpeg-5.0.1-essentials_build\bin\ffmpeg.exe"
            ff = ffmpy.FFmpeg(executable=ffmpeg_path,inputs={old_pic: None}, outputs={new_pic: None})
            ff.run()
            fu=os.path.dirname(old_pic)
            fu2=j(fu,"1-{}-转格式jpg".format(dalei))
            save_j = j(fu2,os.path.basename(new_pic))
            shutil.move(new_pic,save_j)
        except Exception as e:
            print(e,old_pic)


def start_multi(path, geshi):
    pic_all = []
    for dirpath, dirnames, filenames in os.walk(path):
        for pic in filenames:
            pic_all.append(os.path.join(dirpath, pic))
            # print(pic)

    pool = Pool(processes=12)
    for pic in pic_all:
            pool.apply_async(format_pic, args=(pic, geshi),)
    pool.close()
    pool.join()

def move_pic1(path, dalei):
    for dirpath, dirnames, filenames in os.walk(path):
        for pic in filenames:
            old_pic=os.path.join(dirpath, pic)
            if '.jpg' in old_pic:
                shutil.move(old_pic,old_pic.replace("0-{} 原图".format(dalei),"1-{}-转格式jpg".format(dalei)))

# 1 转格式
def zhuan_ge_shi(base_dir):
    # base_dir = r"C:\Users\Administrator\Desktop\pic\夹克"
    os.chdir(base_dir)

    zi = os.listdir(base_dir)
    print(zi)
    m1 = j(base_dir,zi[0])  # 0-夹克 原图
    m2 = j(base_dir,zi[1])  # 1-夹克 转格式--jpg

    pics = os.listdir(m1)
    for pic in pics:
        if pic.split('.')[1]=='jpg':
            shutil.move(j(m1,pic),j(m2,pic))
        else:
            os.system('magick {} {}'.format(j(m1,pic),j(m2,pic.split('.')[0]+'jpg')))
    # 所有的图片格式 --> jpg
    # os.system('magick *.* -format jpg {}/%03d.jpg'.format(m2))

# 2 去背景
def qu_bei_jing(base_dir):
    from transparent_background import Remover
    remover = Remover()
    zi = os.listdir(base_dir)
    m2 = j(base_dir, zi[1])  # 1-夹克 转格式--jpg
    m3 = j(base_dir, zi[2])  # 2-夹克 抠图--png
    os.chdir(m2)
    pic_l = os.listdir(m2)
    for i,im in enumerate(pic_l):
        try:
            img = Image.open(im).convert('RGB')
            out = remover.process(img)
            if not os.path.exists(m3):
                os.makedirs(m3)
            print(r"{}-->{}处理中".format(i+1,im))
            r = r'{}'.format(im.replace('jpg', 'png'))
            out.save(os.path.join(m3,r))
        except:
            print(im,'抠不出来!')

# 3 单张切图
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

# 4 多张切图
def qie_tu_s(base_dir):
    # fu = r"C:\Users\Administrator\Desktop\pic\夹克\夹克 png"
    # new = r"C:\Users\Administrator\Desktop\pic\夹克\夹克切图"
    zi = os.listdir(base_dir)
    m3 = j(base_dir, zi[2])  # 2-夹克 抠图--png
    m4 = j(base_dir, zi[3])  # 3-夹克 切图
    os.chdir(m3)
    pic_l = os.listdir(m3)
    for i,im in enumerate(pic_l):
        qietu(input_pic=im, output_pic=j(m4, str(i)+'_{}.png'.format(time.strftime("%H_%M_%S", time.localtime()))))

# 5 尺寸放大 h680
def h680(base_dir):
    # fu = r"C:\Users\Administrator\Desktop\pic\夹克\3-夹克切图"
    # new = r"C:\Users\Administrator\Desktop\pic\夹克\4-夹克 h680"
    zi = os.listdir(base_dir)
    m4 = j(base_dir, zi[3])  # 3-夹克 切图
    m5 = j(base_dir, zi[4])  # 4-夹克 h680
    fu = m4
    new = m5

    if not os.path.exists(new):
        os.makedirs(new)

    os.chdir(fu)
    pic_l = os.listdir(fu)
    for i, im in enumerate(pic_l):
        print('正在调整尺寸：---> {}'.format(im))
        imgIn = Image.open(im)
        width, height = imgIn.size
        ratio = 680 / height

        new_height = 680
        new_width = int(width * ratio) + 1

        # if new_width > width:
        #     new_width = width
        #     new_height = int(height * (width / new_width))

        imgOut = imgIn.resize((new_width, new_height), Image.LANCZOS)
        imgOut.save(os.path.join(new, im), quality=100, subsampling=0)

# 6 拼图
def pintu(bg,img1,img2,img3,jieguo,save_png_short):
    r"""
    img1 = r"C:\Users\Administrator\Desktop\pic\夹克\4-夹克 h680\10.png"
    img2 = r"C:\Users\Administrator\Desktop\pic\夹克\4-夹克 h680\8.png"
    img3 = r"C:\Users\Administrator\Desktop\pic\夹克\4-夹克 h680\9.png"
    jieguo = r"C:\Users\Administrator\Desktop\pic\夹克\5-夹克 拼图"
    save_png_short= r"001.png"  # 1580 680
    """
    bg_img = Image.open(bg)
    img1 = Image.open(img1)
    img2 = Image.open(img2)
    img3 = Image.open(img3)

    bg_width, _ = bg_img.size
    img1_width, _ = img1.size
    img2_width, _ = img2.size
    img3_width, _ = img3.size

    x=int((bg_width-(img1_width+img2_width+img3_width))/4)

    position1 = (x, 0)
    position2 = (2*x+img1_width, 0)
    position3 = (3*x+img1_width+img2_width, 0)

    bg_img.paste(img1, position1, img1)
    bg_img.paste(img2, position2, img2)
    bg_img.paste(img3, position3, img3)
    output_path = j(jieguo,'{}'.format(save_png_short))

    bg_img.save(output_path)

def start_pintu(base_dir,bg):
    # base_dir = r"C:\Users\Administrator\Desktop\pic\夹克"
    # bg = r"C:\Users\Administrator\Desktop\pic\0-首页图\01.png"
    zi = os.listdir(base_dir)
    m5 = j(base_dir, zi[4])  # 4-夹克 h680
    m6 = j(base_dir, zi[5])  # 5-夹克 拼图  存放结果

    os.chdir(j(base_dir,m5)) # 进入h680
    pics = os.listdir(m5)
    for pic in pics:
        img1,img2,img3= random.sample(pics, 3)
        print(pic,"已经合成!")
        pintu(bg=bg, img1=img1,img2=img2,img3=img3,jieguo=m6,save_png_short=pic)

# 7 清空多余图片


if __name__ == '__main__':
    dalei = "外套"
    base_dir = r"E:\pic\1-外套"
    # bg = r"C:\Users\Administrator\Desktop\pic\0-首页图\000.png"
    bg = r"D:\Backup\Downloads\012.png"  #1580 680

    # chushihua(base_dir,dalei)
    # move_pic1(path=j(base_dir,r"0-{} 原图".format(dalei)), dalei=dalei)
    # zhuan_ge_shi(base_dir)

    # qu_bei_jing(base_dir)
    # qie_tu_s(base_dir)
    # h680(base_dir)
    start_pintu(base_dir, bg)
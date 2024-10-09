from PIL import Image, ImageChops
import shutil, os, time
j=os.path.join

base_dir = r"C:\Users\Administrator\Desktop\pic\夹克"
jieguo = r"C:\Users\Administrator\Desktop\pic\夹克\5-夹克 拼图"
bg = r"C:\Users\Administrator\Desktop\pic\0-首页图\01.png"
h680 = r"C:\Users\Administrator\Desktop\pic\夹克\4-夹克 h680"

def pintu(img1,img2,img3,save_png_short):
    r"""
    img1 = r"C:\Users\Administrator\Desktop\pic\夹克\4-夹克 h680\10.png"
    img2 = r"C:\Users\Administrator\Desktop\pic\夹克\4-夹克 h680\8.png"
    img3 = r"C:\Users\Administrator\Desktop\pic\夹克\4-夹克 h680\9.png"
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
    output_path = j(jieguo,'{}.png'.format(save_png_short))

    bg_img.save(output_path)


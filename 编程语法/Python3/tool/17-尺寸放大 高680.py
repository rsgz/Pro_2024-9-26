from PIL import Image, ImageChops
import shutil, os, time
j=os.path.join

fu = r"C:\Users\Administrator\Desktop\pic\夹克\3-夹克切图"
new = r"C:\Users\Administrator\Desktop\pic\夹克\4-夹克 h680"

if not os.path.exists(new):
    os.makedirs(new)

os.chdir(fu)
pic_l = os.listdir(fu)
for i,im in enumerate(pic_l):
    print('正在调整尺寸：---> {}'.format(im))
    imgIn = Image.open(im)
    width, height = imgIn.size
    ratio = 680 / height

    new_height = 680
    new_width = int(width * ratio)+1

    # if new_width > width:
    #     new_width = width
    #     new_height = int(height * (width / new_width))

    imgOut = imgIn.resize((new_width, new_height), Image.LANCZOS)
    imgOut.save(os.path.join(new, im), quality=100, subsampling=0)

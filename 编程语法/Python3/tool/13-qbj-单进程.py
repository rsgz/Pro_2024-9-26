from transparent_background import Remover
from PIL import Image
import os

remover = Remover()
fu = r"C:\Users\Administrator\Desktop\pic\夹克\output_"
new = r"C:\Users\Administrator\Desktop\pic\new_jiake"
os.chdir(fu)
pic_l = os.listdir(fu)
for i,im in enumerate(pic_l):
    img = Image.open(im).convert('RGB')
    out = remover.process(img)
    if not os.path.exists(new):
        os.makedirs(new)
    print(r"{}-->{}处理中".format(i+1,im))
    zi = r'{}'.format(im.replace('jpg', 'png'))
    out.save(os.path.join(new,zi))
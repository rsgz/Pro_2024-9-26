from transparent_background import Remover
from PIL import Image
import os
import multiprocessing



remover = Remover()
pool = multiprocessing.Pool(processes=os.cpu_count())

fu = r"C:\Users\Administrator\Desktop\pic\紧身裤"
new = r"C:\Users\Administrator\Desktop\pic\new"
os.chdir(fu)
pic_l = os.listdir(fu)

def process_image(image_name):
    img = Image.open(image_name).convert('RGB')
    out = remover.process(img)
    if not os.path.exists(new):
        os.makedirs(new)
    zi = r"{}".format(image_name.replace('jpg', 'png'))
    out.save(os.path.join(new, zi))


for i, im in enumerate():
    pool.imap(process_image, pic_l)
    print(r"{}-->{}处理中".format(i+1,im))

pool.close()
pool.join()



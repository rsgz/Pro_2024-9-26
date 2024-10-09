import os
import ffmpy
from multiprocessing import Pool

r"""
pip install ffmpy -i https://mirrors.aliyun.com/pypi/simple
"""

def format_pic(pic, geshi):
    r"""
    format_pic(pic=pic, geshi='jpg')
    """
    old_pic = pic
    if geshi not in old_pic and "Thumbs.db" not in old_pic and ".ini" not in old_pic:
        new_pic = os.path.splitext(old_pic)[0] + '.' + geshi
        ff = ffmpy.FFmpeg(inputs={old_pic: None}, outputs={new_pic: None})
        ff.run()

    if geshi not in old_pic:
        os.remove(old_pic)



def start_multi(path, geshi):
    pic_all = []
    for dirpath, dirnames, filenames in os.walk(path):
        for pic in filenames:
            pic_all.append(os.path.join(dirpath, pic))
            print(pic)

    pool = Pool(processes=12)
    for pic in pic_all:
            pool.apply_async(format_pic, args=(pic, geshi),)
    pool.close()
    pool.join()

if __name__ == '__main__':
    import time
    start = time.time()
    d = input("请输入你的路径:")
    geshi = input("请输入你想转换的目标图片格式:")
    # start_multi(path=d, geshi='jpg')
    start_multi(path=d, geshi=geshi)
    end = time.time()
    print("消耗了：", end-start, '秒!!!')
    os.startfile(d)
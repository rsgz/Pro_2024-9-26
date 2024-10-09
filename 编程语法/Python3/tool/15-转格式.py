import os
j=os.path.join


def zhuan_ge_shi(base_dir):
    # base_dir = r"C:\Users\Administrator\Desktop\pic\夹克"
    os.chdir(base_dir)

    zi = os.listdir(base_dir)
    print(zi)
    m1 = j(base_dir,zi[0])
    m2 = j(base_dir,zi[1])
    os.chdir(m1)  # 0-夹克 原图magick *.* -format jpg "{}"\%03d.jpg
    # zi[1]  # 1-夹克 转格式--jpg

    # 所有的图片格式 --> jpg
    os.system("magick *.* -format jpg {}\%03d.jpg".format(m2))


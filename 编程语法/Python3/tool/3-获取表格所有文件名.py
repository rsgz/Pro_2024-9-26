r"""
python获取这个路径下面 所有表格的文件名
C:\Users\Administrator\Desktop\爬取结果\1-谷歌 总爬取
最简洁的文件名
"""

import os

# 定义目录路径
# dir_path = input("请输入你的父目录:")
dir_path = r"C:\Users\Administrator\Desktop\爬取结果\2-类目"

# 获取目录下所有文件名
try:
    file_names = os.listdir(dir_path)
    for f in file_names:
        print(f.replace('.csv',''))
except:
    print('提供的路径不存在，请检查路径是否正确。')
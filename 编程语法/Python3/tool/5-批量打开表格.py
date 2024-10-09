import os

j = os.path.join
dir_path = input("请输入父目录:")


# 获取目录下所有文件名
try:
    for b in os.listdir(dir_path):
        biao = j(dir_path,b)
        print(b)
        # os.system(biao)
except:
    print('提供的路径不存在，请检查路径是否正确。')
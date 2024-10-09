import os

os.chdir(r"C:\Users\Administrator\Desktop\爬取结果\3-爬取类目商品 版本记录\2024.8.2\女士夹克-jackets")

for i,f in enumerate(os.listdir('.')):
    os.rename(f,str(i+1)+"-"+f)
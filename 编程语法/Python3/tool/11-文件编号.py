import os

os.chdir(r"E:\share\1")

for i,f in enumerate(os.listdir('.')):
    os.rename(f,str(i+1)+"-"+f)
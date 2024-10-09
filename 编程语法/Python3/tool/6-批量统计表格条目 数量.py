r"""
openpyxy模块
pip install openpyxl -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
"""
import pandas as pd
import os
from openpyxl import load_workbook

work_dir = r"C:\Users\Administrator\Desktop\爬取结果\2-品类-表格分类"
os.chdir(work_dir)

for i,f in enumerate(os.listdir('.')):
    print(i+1, f.replace('.xlsx',''))

# filename = 'your_table.xlsx'
# df = pd.read_excel(filename, usecols='A')

# 对于CSV文件
filename = 'your_table.csv'
df = pd.read_csv(filename)

# 获取A列的行数（不包括表头）
row_count = df['A'].count()

print(f"A列有 {row_count} 行数据。")

import pandas as pd
import os
from pathlib import Path
j = os.path.join

# 设置文件夹路径
fu = r'C:\Users\Administrator\Desktop\data\xlsx'
excel_files = [file for file in os.listdir(fu) if file.endswith('.xlsx')]

# 初始化一个空的 DataFrame 用于存储所有 A 列的数据
all_a_columns = []

# 遍历每个 Excel 文件
for file in excel_files:
    # 读取 Excel 文件中的第一个工作表（通常是 'Sheet1'）
    df = pd.read_excel(j(fu, file), usecols='A')  # 仅读取 A 列
    all_a_columns.append(df)

# 将所有 A 列的 DataFrame 合并成一个 DataFrame
merged_a_columns = pd.concat(all_a_columns, ignore_index=True)

# 去除重复的行
merged_a_columns_unique = merged_a_columns.drop_duplicates()

# 将合并后的 A 列数据保存到一个新的 Excel 文件中
output_file = Path(fu) / '0-merged_excel.xlsx'
merged_a_columns_unique.to_excel(output_file, index=False)

import pandas as pd
import os

r"""
代码没有运行测试 但是应该是可以的
"""

# 设置文件夹路径
fu = r'C:\Users\Administrator\Desktop\数据\黑冰爬取'

# 列出所有以.csv结尾的文件
excel_files = [file for file in os.listdir(fu) if file.endswith('.csv')]

# 创建一个空的列表来存储所有数据框架
all_dataframes = []

# 遍历每个CSV文件
for file in excel_files:
    # 读取CSV文件到数据框架
    df = pd.read_csv(os.path.join(fu, file))
    # 添加数据框架到列表中
    all_dataframes.append(df)

# 将所有数据框架合并为一个
merged_dataframe = pd.concat(all_dataframes, ignore_index=True)

# 过滤包含NA/NaN值的行
merged_dataframe = merged_dataframe.dropna(subset=['Domain'])

# 过滤包含特定URL模式的行
filtered_dataframe = merged_dataframe[merged_dataframe['Domain'].str.contains('.myshopify.com')]

# 去重并保存
filtered_dataframe_unique = filtered_dataframe.drop_duplicates(subset=['Domain'])

# 保存合并后的数据框架到Excel文件
filtered_dataframe_unique.to_excel(os.path.join(fu, '1-merged_excel.xlsx'), index=False)

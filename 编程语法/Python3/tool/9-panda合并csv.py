import pandas as pd
import os
j = os.path.join

fu = r'C:\Users\Administrator\Desktop\数据\黑冰爬取'
excel_files = [file for file in os.listdir(fu) if file.endswith('.csv')]

all_dataframes = []

for file in excel_files:
    df = pd.read_csv(j(fu,file))
    all_dataframes.append(df)

merged_dataframe = pd.concat(all_dataframes, ignore_index=True)
merged_dataframe = merged_dataframe.dropna(subset=['Domain'])  # 移除包含NA/NaN值的行
# filtered_dataframe = merged_dataframe[merged_dataframe['Domain'].str.startswith('http')]
filtered_dataframe = merged_dataframe[merged_dataframe['Domain'].str.contains('.myshopify.com')]
filtered_dataframe_unique = filtered_dataframe.drop_duplicates(subset=['Domain'])  # 去重
# print(merged_dataframe)
filtered_dataframe_unique.to_excel(j(fu, '0-merged_excel.xlsx'), index=False)
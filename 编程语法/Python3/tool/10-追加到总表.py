import os
import pandas as pd

r"""
xinbiao Domain 那一列的值和 zongbiao的Domain进行对比，如果zongbiao已经存在这个值，就不用追加进去了，不存在的值都追加到zongbiao，只要追加Domain那一列
"""


zongbiao = r"C:\Users\Administrator\Desktop\爬取结果\00-网址汇总\myshopify.com-all.xlsx"
xinbiao = r"C:\Users\Administrator\Desktop\爬取结果\1 myshopify.com网站爬取记录\myshopify.com -2024-8-5\0-merged_excel.xlsx"

df_zongbiao = pd.read_excel(zongbiao, sheet_name='Sheet1')
df_xinbiao = pd.read_excel(xinbiao, sheet_name='Sheet1')
new_domains = df_xinbiao[~df_xinbiao['Domain'].isin(df_zongbiao['Domain'])]  # 找出xinbiao中不在zongbiao中的Domain
new_domains = new_domains[['Domain']]  # 只保留Domain列
updated_zongbiao = pd.concat([df_zongbiao, new_domains], ignore_index=True)  # 将新的Domain追加到zongbiao
result = r"C:\Users\Administrator\Desktop\爬取结果\00-网址汇总\myshopify.com-all2.xlsx"
updated_zongbiao.to_excel(result, index=False)


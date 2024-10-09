import numpy as np

file_path=r"C:\Users\Administrator\Desktop\rust_url2.txt"
url_txt = r"C:\Users\Administrator\Desktop\rust_url3.txt"

# file_path=r"C:\Users\Administrator\Desktop\数据\0-男.txt"
# url_txt = r"C:\Users\Administrator\Desktop\002.txt"
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        websites = file.read().splitlines()
except Exception as e:
    print(e)

# 去重
unique_lst = np.unique(websites)
filtered_lst = [url for url in unique_lst if '/collections/' in url ]

# 保存结果  覆盖
with open(url_txt, 'w', encoding='utf-8') as file:
    for url in filtered_lst:
        file.write(url + '\n')
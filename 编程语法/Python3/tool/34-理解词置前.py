from urllib.parse import urlparse
import numpy as np


# 获取链接尾部
def extract_last_part(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    parts = path.strip('/').split('/')
    # print(path.strip('/'))
    return parts[-1] if parts else None

file_path=r"C:\Users\Administrator\Desktop\rust_url3.txt"
url_txt = r"C:\Users\Administrator\Desktop\rust_url4.txt"
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        websites = file.read().splitlines()
except Exception as e:
    print(e)

# 去重
# unique_lst = np.unique(websites)
# filtered_lst = [url for url in unique_lst if '/collections/' in url ]

# 保存结果  覆盖
with open(url_txt, 'w', encoding='utf-8') as file:
    for href in websites:
        file.write(r"{}:{}".format(extract_last_part(href).replace('-', ' '), href))
        file.write('\n')
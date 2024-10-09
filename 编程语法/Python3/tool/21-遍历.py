from selenium_rsgz import creat_google_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
import numpy as np
from urllib.parse import urlparse

port = input("指定端口:")


# 获取链接尾部
def extract_last_part(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    parts = path.strip('/').split('/')
    # print(path.strip('/'))
    return parts[-1] if parts else None

import time

# websites=[
# "https://goodgoodgolf.myshopify.com",
# "https://americas-thrift-supply.myshopify.com",
# "https://made-blanks.myshopify.com",
# "https://eastsidegolf.myshopify.com",
# "http://staud-clothing.myshopify.com",
# "https://team-kennedy-24.myshopify.com",
# "https://a7x-world.myshopify.com",
# "https://highsandlows.myshopify.com"
# ]

# 获取网址
print('1 获取网址')
file_path=r"C:\Users\Administrator\Desktop\遍历网址.txt"
file_path=input("输入遍历网址路径:")
websites=[]
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        websites = file.read().splitlines()
except Exception as e:
    print(e)

print('2 遍历网址')
# 遍历网址
# Google Chrome for Testing	120.0.6099.109 (正式版本) （64 位）
IP_Port = "127.0.0.1:{}".format(port)
chromedriver = r"D:\58-chrome\chromedriver-win64\chromedriver.exe"
browser,service = creat_google_driver(IP_Port, chromedriver)
url_txt=r"C:\Users\Administrator\Desktop\url.txt"
url_txt=input("请输入保存网址路径:")
browser.implicitly_wait(10)  # 隐式等待

for i,website in enumerate(websites):
    try:
        print("进入",i+1,website)
        browser.get(website)
        a_tags = browser.find_elements(By.TAG_NAME,"a")

        # 获取网页中所有a链接  追加到url.txt  格式是  title:a链接;
        with open(url_txt, 'a+', encoding='utf-8') as file:
            for a_tag in a_tags:
                try:
                    href = a_tag.get_attribute('href')
                    if href:
                        file.write(r"{}:{}".format(extract_last_part(href).replace('-',' '),href))
                        file.write('\n')
                    r"""
                    title = a_tag.get_attribute('title')
                    if title:
                        # 如果链接有标题，则写入格式为 域名;title:a链接;
                        # file.write(r"{}:{}".format(title,href))
                        file.write(r"{}:{}".format(title,href))
                        file.write('\n')
                    else:
                        # 如果链接没有标题，则写入格式为 域名;a链接;
                        # file.write(r"{};{}".format(website,href))
                        file.write(r"{};{}".format(website,href))
                        file.write('\n')
                    """

                except:
                    pass
    except Exception as e:
        print(e)
        print("网站有问题")


# 网址去重
print('4 网址去重')
websites_result=[]
try:
    with open(url_txt, 'r', encoding='utf-8') as file:
        websites_result = file.read().splitlines()
except Exception as e:
    print(e)
# 去重
unique_lst = np.unique(websites_result)
# 去掉垃圾 网址
filtered_lst = [url for url in unique_lst if not url.startswith((':', '-:','@',' :'))]

print('5 网址已经全部写入')
# 保存结果  覆盖
with open(url_txt, 'w', encoding='utf-8') as file:
    for url in filtered_lst:
        file.write(url + '\n')

print('成功!!!!!\n'*5)
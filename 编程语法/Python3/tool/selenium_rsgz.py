from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

r"""
pip install selenium -i https://mirrors.aliyun.com/pypi/simple
"""

# 创建 google driver
def creat_google_driver(IP_Port, chromedriver):
    r"""
    这个函数 用来创建谷歌driver
    # "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9530 --no-first-run --no-default-browser-check --user-data-dir="C:\Users\Administrator\Desktop\芒果代码\改价格\user_data"
    IP_Port = "127.0.0.1:9530"
    chromedriver = "F:\python\chromedriver.exe"
    browser = creat_google_driver(IP_Port, chromedriver)
    返回 browser,service
    """
    service = Service(chromedriver)
    service.command_line_args()
    service.start()

    options = Options()
    options.add_experimental_option("debuggerAddress", IP_Port)  # 这个IP 和端口 不要改动

    browser = webdriver.Chrome(service=service, options=options)  #  service接收谷歌驱动 options接收 IP 和端口
    return browser,service

# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9530 --no-first-run --no-default-browser-check --user-data-dir="C:\Users\Administrator\Desktop\芒果代码\改价格\user_data"
if __name__ == '__main__':
    IP_Port = "127.0.0.1:9530"
    chromedriver = "F:\python\chromedriver.exe"
    browser = creat_google_driver(IP_Port, chromedriver)
    print(browser.title)
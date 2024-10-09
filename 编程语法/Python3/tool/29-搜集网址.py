from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
import os,time
from pyquery import PyQuery as pq
from fake_useragent import UserAgent
import random


r'''
pip install selenium
pip install urllib
pip install requests
pip install pyquery
pip install threading
pip install fake-useragent -i https://mirrors.aliyun.com/pypi/simple
'''

url_0 = r"C:\Users\Administrator\Desktop\url_0.txt"
keyword_0=r"C:\Users\Administrator\Desktop\keyword_0.txt"

domain_l = ['www.google.com'
                                   , 'www.google.gl'
                                   , 'www.google.com.sv'
                                   , 'www.google.hn'
                                   , 'www.google.co.cr'
                                   , 'www.google.com.jm'
                                   , 'www.google.ht'
                                   , 'www.google.com.pr'
                                   , 'www.google.vg'
                                   , 'www.google.com.ag'
                                   , 'www.google.dm'
                                   , 'www.google.com.vc'
                                   , 'www.google.tt'
                                   , 'www.google.com.ar'
                                   , 'www.google.com.br'
                                   , 'www.google.com.co'
                                   , 'www.google.co.ve'
                                   , 'www.google.com.ec'
                                   , 'www.google.com.uy'
                                   , 'www.google.no'
                                   , 'www.google.is'
                                   , 'www.google.dk'
                                   , 'www.google.lv'
                                   , 'www.google.lt'
                                   , 'www.google.ru'
                                   , 'www.google.pl'
                                   , 'www.google.sk'
                                   , 'www.google.at'
                                   , 'www.google.ie'
                                   , 'www.google.nl'
                                   , 'www.google.be'
                                   , 'www.google.fr'
                                   , 'www.google.it'
                                   , 'www.google.es'
                                   , 'www.google.ro'
                                   , 'www.google.gr'
                                   , 'www.google.ba'
                                   , 'www.google.sm'
                                   , 'www.google.com.au'
                                   , 'www.google.co.nz'
                                   , 'www.google.co.ck'
                                   , 'www.google.com.sb'
                                   , 'www.google.ws'
                                   , 'www.google.as'
                                   , 'www.google.to'
                                   , 'www.google.co.il'
                                   , 'www.google.com.sa'
                                   , 'www.google.com.eg'
                                   , 'www.google.ae'
                                   , 'www.google.com.bh'
                                   , 'www.google.jo'
                                   , 'www.google.com.ly'
                                   , 'www.google.co.ma'
                                   , 'www.google.com.et'
                                   , 'www.google.mu'
                                   , 'www.google.ci'
                                   , 'www.google.dj'
                                   , 'www.google.cd'
                                   , 'www.google.cg'
                                   , 'www.google.gm'
                                   , 'www.google.co.ke'
                                   , 'www.google.com.gi'
                                   , 'www.google.co.bw'
                                   , 'www.google.co.zm'
                                   , 'www.google.com.na'
                                   , 'www.google.co.ls'
                                   , 'www.google.sh'
                                   , 'www.google.mw'
                                # ,'www.google.cn'
                                   , 'www.google.co.kr'
                                   , 'www.google.mn'
                                   , 'www.google.co.jp'
                                   , 'www.google.com.hk'
                                   , 'www.google.com.tw'
                                   , 'www.google.com.vn'
                                   , 'www.google.com.my'
                                   , 'www.google.co.id'
                                   , 'www.google.com.pk'
                                   , 'www.google.com.bd'
                                   , 'www.google.com.np'
                                   , 'www.google.az'
                                   , 'www.google.am'
                                   , 'www.google.tm'
                                   , 'www.google.co.uz'
                                   , 'www.google.kg'
                                   , 'www.google.com.tj']

# if os.path.exists(url_0):
#     os.remove(url_0)
# else:
#     print("没有url_0.txt文件残留")

if not os.path.exists(url_0):
    with open(url_0, 'a+', encoding='utf-8') as file:
        pass

pages = int(input("请输入扫描深度（页数）:"))

uas = UserAgent()

with open(keyword_0, 'r',encoding='utf-8') as x:
    for line in x:
        word = 'site:*.myshopify.com '+ line.replace('\n', '')
        print('-'*40+'\n')
        print("搜索关键词："+word)

        domain = random.choice(domain_l)
        print('使用谷歌域名：' + domain)
        # url = 'https://www.google.com.hk/search?q=' + word + '&hl=zh&start=' + str(page) + '&safe=images'  # 英文en中文zh
        # url = 'https://'+domain+'/search?q='+word+'&hl=zh&start='+str(page)+'&safe=images'#英文en中文zh
        url = 'https://' + domain + '/search?q=' + word + '&hl=en'  # 英文en中文zh
        option = Options()
        # option.add_argument("--headless")  # 没有窗口
        option.add_argument('–disable-javascript')
        # option.add_argument('--window-size=300,200')
        option.add_argument('–no-sandbox')
        option.add_argument('--blink-settings=imagesEnabled=false')  # 不显示图片
        option.add_argument('--proxy-server=http://127.0.0.1:7890')
        # 使用随机ua，不然封ip需要人机验证
        # f = Factory.create()
        # ua = f.user_agent()
        ua = uas.random
        print('使用UA：' + ua)
        option.add_argument('--user-agent="' + ua + '"')

        driver = webdriver.Chrome(options=option)
        driver.implicitly_wait(1)  # 等待页面加载完成
        driver.get(url)

        def save_data1():
            d = pq(driver.page_source)
            myshopify_url_all = ''
            for cite in d('span[role="text"]').items():
                myshopify_url = cite.text()
                if 'myshopify.com' in myshopify_url:
                    myshopify_url_all = myshopify_url + '\n' + myshopify_url_all
            print(myshopify_url_all)

            with open(url_0, "a+", encoding="utf-8") as f2:
                f2.write(myshopify_url_all + '\n')

        def save_data2():
            d = pq(driver.page_source)
            myshopify_url_all = ''

            for cite in d('div cite').items():
                myshopify_url = cite.text()
                if 'myshopify.com' in myshopify_url:
                    myshopify_url_all = myshopify_url + '\n' + myshopify_url_all
            print(myshopify_url_all)

            with open(url_0, "a+", encoding="utf-8") as f2:
                f2.write(myshopify_url_all + '\n')

        for page in range(0, pages):
            print("正在爬取第"+str(page+1)+"页")
            x=driver.find_elements(By.CSS_SELECTOR, 'td[role="heading"]') # 下一页

            if x==[]:  # 没有下一页
                print("谷歌处于More search result模式")
                try:
                    next_button1 = driver.find_element(By.XPATH, '//span[contains(text(), "More search results")]')
                    if next_button1:
                        driver.execute_script("arguments[0].click();", next_button1)
                    else:
                        save_data1()
                        break
                except Exception as e:
                    print(e)
            else:
                print("谷歌处于 下一页 模式")  # id="botstuff"
                # spans = driver.find_elements(By.CSS_SELECTOR, 'div span')  # $('td span:contains(Next)')[0].click()
                # for span in spans:
                #     if 'Next' in span.text:
                #         save_data()
                #         print('点击了下一页')
                #         span.click()
                try:
                    save_data2()
                    next_button2 = driver.find_element(By.XPATH, '//span[contains(text(), "Next")]')
                    if next_button2:
                        driver.execute_script("arguments[0].click();", next_button2)
                    else:
                        break
                except Exception as e:
                    print(e)


        # time.sleep(3000)
        driver.quit()
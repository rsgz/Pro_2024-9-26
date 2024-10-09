import asyncio
import subprocess
import os,time
import numpy as np
import pyperclip
import clipboard
import pyautogui
from find_pic import find_pic_click_center_keep
j=os.path.join

r'''
pip install asyncio
'''

lei_fu = r'E:\爬取结果\2-类目\类目'  # 存放类目
url_txt=r"C:\Users\Administrator\Desktop\数据\0-女.txt"  # 几万网站数据
shang_pin_dir = r'E:\爬取结果\3-商品\{}'.format(time.strftime("%Y-%m-%d", time.localtime()))   # 商品文件夹


websites_result=[]
try:
    with open(url_txt, 'r', encoding='utf-8') as file:
        websites_result = file.read().splitlines()
except Exception as e:
    print(e)

bixu_l=['http']



xie=1
# include_keywords,exclude_keywords = ["手链"],["男士",'帽子','披肩']
# include_keywords,exclude_keywords = ["人字拖"],["男士",'帽子','披肩']
# include_keywords,exclude_keywords = ["女士包"],["男士",'帽子','披肩']
# include_keywords,exclude_keywords = ["雨帽"],["男士",'帽子','披肩']
# include_keywords,exclude_keywords = ["靴子"],["男士",'帽子','披肩']
# include_keywords,exclude_keywords = ["绑带"],["男士",'帽子','披肩']
# include_keywords,exclude_keywords = ["连体衣"],["男士",'帽子','披肩']
# include_keywords,exclude_keywords = ['连身衣'],["男士",'帽子','披肩']
# include_keywords,exclude_keywords = ['连体裤'],["男士",'帽子','披肩']
# include_keywords,exclude_keywords = ['连衣裤'],["男士",'帽子','披肩']
# include_keywords,exclude_keywords = ['连身裤'],["男士",'帽子','披肩']
# include_keywords,exclude_keywords = ['连体服'],["男士",'帽子','披肩']
# include_keywords,exclude_keywords = ["首饰"],["男士"]
# include_keywords,exclude_keywords = ["蜡烛"],["男士"]
# include_keywords,exclude_keywords = ["肩包"],["男士"]
# include_keywords,exclude_keywords = ["纱丽"],["男士"]
# include_keywords,exclude_keywords = ["胸衣"],["男士"]
# include_keywords,exclude_keywords = ["眼镜"],["男士"]
# include_keywords,exclude_keywords = ["皮带"],["男士"]
# include_keywords,exclude_keywords = ["浴袍"],["男士"]
# include_keywords,exclude_keywords = ["皮裤"],["男士"]
# include_keywords,exclude_keywords = ["羽绒服"],["男士"]
# include_keywords,exclude_keywords = ["连体衣"],["男士"]
# include_keywords,exclude_keywords = ["长袖上衣"],["男士"]
# include_keywords,exclude_keywords = ["开衫"],["男士"]
# include_keywords,exclude_keywords = ["休闲裤"],["男士"]
# include_keywords,exclude_keywords = ["七分袖"],["男士"]
# include_keywords,exclude_keywords = ["宽腿裤"],["男士"]
# include_keywords,exclude_keywords = ["香水"],["男士"]
# include_keywords,exclude_keywords = ["雪地服"],["男士"]
# include_keywords,exclude_keywords = ["防水袜"],["男士"]
# include_keywords,exclude_keywords = ["防水服",'防水衣'],["男士"]
# include_keywords,exclude_keywords = ['雨衣','防水衣','防雨'],["男士"]
# include_keywords,exclude_keywords = ["腰带"],["男士"]
# include_keywords,exclude_keywords = ["耳环"],["男士"]
# include_keywords,exclude_keywords = ["睡袍"],["男士"]
# include_keywords,exclude_keywords = ["民族服饰"],["男士"]
# include_keywords,exclude_keywords = ["配饰"],["男士"]
# include_keywords,exclude_keywords = ["珠宝"],["男士"]
# include_keywords,exclude_keywords = ["便帽"],["男士"]
# include_keywords,exclude_keywords = ["袜子"],["男士"]
# include_keywords,exclude_keywords = ["护甲"],["男士"]
# include_keywords,exclude_keywords = ["斗篷"],["男士"]
# include_keywords,exclude_keywords = ["斜挎包"],["男士"]
# include_keywords,exclude_keywords = ["手镯"],["男士"]
# include_keywords,exclude_keywords = ["手袋"],["男士"]
# include_keywords,exclude_keywords = ["工装裤"],["男士"]
# include_keywords,exclude_keywords = ["家居鞋"],["男士"]
# include_keywords,exclude_keywords = ["包袋"],["男士"]
# include_keywords,exclude_keywords = ["休闲鞋"],["男士"]
# include_keywords,exclude_keywords = ["乐福鞋"],["男士"]
# include_keywords,exclude_keywords = ["头饰"],["男士"]
# include_keywords,exclude_keywords = ["卫衣"],["男士"]
# include_keywords,exclude_keywords = ["背包"],["男士"]
# include_keywords,exclude_keywords = ["七分裤"],["男士"]
# include_keywords,exclude_keywords = ["家居服"],["男士"]
# include_keywords,exclude_keywords = ["紧身衣"],["男士"]
# include_keywords,exclude_keywords = ['tank','vest'],["男士",'外套','夹克']
# include_keywords,exclude_keywords = ["钱包"],["男士"]
# include_keywords,exclude_keywords = ["雨伞"],["男士"]
# include_keywords,exclude_keywords = ["大衣"],["男士"]
# include_keywords,exclude_keywords = ["高跟鞋"],["男士"]
# include_keywords,exclude_keywords = ["运动裙"],["男士"]
# include_keywords,exclude_keywords = ["牛仔裙"],["男士"]
# include_keywords,exclude_keywords = ["花裙"],["男士"]
# include_keywords,exclude_keywords = ["百褶裙"],["男士"]
# include_keywords,exclude_keywords = ["围裙"],["男士"]
# include_keywords,exclude_keywords = ["铅笔裙"],["男士"]
# include_keywords,exclude_keywords = ["丝袜"],["男士"]
# include_keywords,exclude_keywords = ["披肩"],["男士"]
# include_keywords,exclude_keywords = ["帽子"],["男士",'七分裤','打底裤']
# include_keywords,exclude_keywords = ["单肩包"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["肩包"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["太阳镜"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["平底鞋"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["工作服"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["防晒衣"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["戒指"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["针织夹克"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["睡裤"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["手提包"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["手表"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["手术服"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["手套"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["围巾"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["打底衫"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["拖鞋"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["牛仔夹克"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["滑雪服"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["泳裤"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["连体裤"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["泳装"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["运动服"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["套衫"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["泳衣"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["长袍"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["凉鞋"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["平角裤"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["摩托车夹克"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["派克大衣"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["比基尼"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["羊毛衫"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["绑腿"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["潜水服"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["羊毛大衣"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["运动鞋"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["羽绒外套"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["羽绒夹克"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["跑步鞋"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["软壳夹克"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["运动裤"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["羊毛夹克"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["飞行员夹克"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["沙滩装"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["披风"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["马球衫"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["运动衫"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["皮夹克"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["飞行员皮夹克"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["短裤"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["球衣"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["分层连衣裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["长袖连衣裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["系带连衣裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["喇叭裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["裹身裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["吊带连衣裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["短裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["短袖连衣裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["迷你连衣裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["针织连衣裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["长裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["中长连衣裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["长袍连衣裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["无袖连衣裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["紧身裤"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["胸罩"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["军裤"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["吊带裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["中长裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["半身裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["短裤裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["工装裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["裹身裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["包臀裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["迷你裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["睡衣"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["睡裙"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["风衣"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["牛仔裤"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["喇叭裤"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["长裤"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["连帽衫"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["套头衫"],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["T恤",'衬衫','T 恤'],["男士",'帽子','披肩','七分裤','打底裤','连衣裙']
# include_keywords,exclude_keywords = ["西服",'西装'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['打底裤'],["男士",'帽子']
# include_keywords,exclude_keywords = ['衬衫裙'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['blazer'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['内裤'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['工作靴'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['马裤'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['登山靴'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['婚纱'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['内衣'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['登山鞋'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['滑雪裤'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['滑雪靴'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['毛衣'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['渔夫帽'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['慢跑裤'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['帆船鞋'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['高筒袜'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['项链'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['登山靴'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['运动装'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['中筒袜'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['高跟靴'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['磨砂裤'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['工作鞋'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['锥形裤'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['健身服'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['冬靴'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['毛巾'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['发饰'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['坡跟鞋'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['棒球帽'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ['牛仔靴'],["男士",'帽子','披肩','七分裤','打底裤']
# include_keywords,exclude_keywords = ["外套"],["男士",'帽子','披肩']
# include_keywords,exclude_keywords = ["女鞋"],["男士"]
# include_keywords,exclude_keywords = ['夹克'],["男士",'vest','tank']
# include_keywords,exclude_keywords = ["夹克"],["男士"]
# include_keywords,exclude_keywords = ["连衣裙"],["男士",'帽子','披肩','七分裤','打底裤']

# include_keywords,exclude_keywords = ["裙"],["男士"]
# include_keywords,exclude_keywords = ["长袖"],["男士"]
# include_keywords,exclude_keywords = ["短袖"],["男士"]
# include_keywords,exclude_keywords = ["针织品"],["男士",'帽子','披肩']
# include_keywords,exclude_keywords = ["孕妇"],["男士",'帽子','披肩','七分裤','打底裤']

xie_url_txt=xie
# 过滤函数
def filter_data(line):
    # return all(kw in line for kw in include_keywords) and not any(ex in line for ex in exclude_keywords)
    return all(kw in line for kw in bixu_l) and any(kw in line for kw in include_keywords) and not any(ex in line for ex in exclude_keywords)

filtered_data = np.array(websites_result)[np.vectorize(filter_data)(websites_result)]

for line in filtered_data:
    print(line)

# 去除http左边的字符串
def remove_prefix(url):
    return 'http'+url.split('http')[1] if 'http' in url else url

# 应用去除前缀的函数
cleaned_data = np.array([remove_prefix(line) for line in filtered_data])



# cleaned_data = np.vectorize(remove_prefix)(filtered_data)

# print(filtered_data)
print('>>>>>>>>>>>> 一共:{} <<<<<<<<<<<<<<<'.format(len(filtered_data)))

# 类目记录
if os.path.exists(j(lei_fu,include_keywords[0]+'.txt')):
    print('{} 类目记录已经存在!'.format(include_keywords[0]+'.txt'))
else:
    with open(j(lei_fu,include_keywords[0]+'.txt'), 'a+', encoding='utf-8') as file:
        print('{} 新创建成功!'.format(include_keywords[0]+'.txt'))

# 商品文件夹  存放最终数据的文件夹
if not os.path.exists(j(shang_pin_dir,include_keywords[0])):
    os.makedirs(j(shang_pin_dir,include_keywords[0]))

# 写入类目记录
if xie:
    with open(j(lei_fu, include_keywords[0] + '.txt'), 'a+', encoding='utf-8') as file:
        for i in cleaned_data:
            file.write(i)
            file.write('\n')
print('>>>>>>>>>>>> 写入{}条新记录 <<<<<<<<<<<<<<<'.format(len(cleaned_data)))



# 获取需要保留的数据（不在filtered_data中的数据）
data_to_keep = [line for line in websites_result if line not in filtered_data]

print('>>>>>>>>>>>> {}文件只剩下{}记录 <<<<<<<<<<<<<<<'.format(os.path.basename(url_txt),len(data_to_keep)))
if xie==0:
    print('>>>>>>>>>>>> 记录 还没去除! <<<<<<<<<<<<<<<\n'.format(len(filtered_data))*5)
else:
    print('>>>>>>>>>>>> 去除了{}记录 <<<<<<<<<<<<<<<\n'.format(len(filtered_data))*5)

# 将筛选后的数据写回文件
if xie_url_txt:
    try:
        with open(url_txt, 'w', encoding='utf-8') as file:
            for line in data_to_keep:
                file.write(line + '\n')
    except Exception as e:
        print(e)

print('>>>>>>>>>>>> {}记录 已经到粘贴板可以随时复制 <<<<<<<<<<<<<<<'.format(len(cleaned_data)))
mulu = j(shang_pin_dir,include_keywords[0])
clipboard.copy(mulu)
time.sleep(0.7)
text_to_copy = '\n'.join(cleaned_data.tolist())
clipboard.copy(text_to_copy)
print('>>>>>>>>>>>> {}记录 已经到粘贴板可以随时复制 <<<<<<<<<<<<<<<'.format(len(cleaned_data)))
print(type(cleaned_data))
print(mulu)
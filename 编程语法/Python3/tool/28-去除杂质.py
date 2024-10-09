import os,time
import numpy as np
import pyperclip
import clipboard

j=os.path.join

xie_url_txt=1  # 覆盖数据吗？
# url_txt=r"C:\Users\Administrator\Desktop\数据\总数据2-2024-8-26.txt"  # 几万网站数据
url_txt=r"C:\Users\Administrator\Desktop\数据\总数据.txt"  # 几万网站数据
# url_txt=r"C:\Users\Administrator\Desktop\数据\0-女.txt"  # 几万网站数据

websites_result=[]
try:
    with open(url_txt, 'r', encoding='utf-8') as file:
        websites_result = file.read().splitlines()
except Exception as e:
    print(e)

include_keywords=[
    "政策","服务","电话","手机","号码","订单","官方","博客","无效","约翰","分类侧边","愿望清单","我们是谁","举报",
    "怎么做","什么意思","机制","欢迎来到","条款","声明","积极分子","愿景","视频","查看全部","验证方法","验证","供应商",
    '发货','送货','退换货','退货','有缺陷的','关于安装','关于我们','可访问性','账户','痤疮','杂技项目','活跃：','积极倡导',
    '积极行动主义','地址：','适应：','订阅','后付款','付款','后续','老化皮肤','协议','区域3','discord.','锦标赛','保证',
    '一起工作','工作坊','研讨会','合作','提款','最新消息','每周焦点','说明','升级','严格','商店定位器','辣味','香肠','尺码表',
    '尺码指南','按品牌','搜索','登录','首页','结果页面','零售商','补货','租用','评论','帐户','注册','租赁','代租','重定向','生产合规性',
    '隐私','预订：','联系','购物','故事','价值观','新闻：','杂志','计划','胶囊','基础知识','.jpg','.png','.jpeg','+','可擦除','礼品：',
    '礼品卡','礼券','知识产权','盟友','畅销书','电子版','条款','指南','导航','运输','输送','金额','销售：','处理','胡闹','问题','货车',
    '详细信息','详情','请求','访客','评价','诊断','词汇表','观看','职业：','美国：','给我们：','结帐','章','社论','社区','社会','申请','生活方式',
    '生态材料','生态认证','清关','案例','框架','样本','样板','核心：','查找','查塔努','姊妹网站','期刊','通话','最后机会','最后','更换','更改','更新',
    '通知','文章：','的历史','的品牌','的商店','的团队','大使','承诺','@','Instagram','facebook','tiktok','表格','准则','萨洛蒙','youtube',
    '女性：','全部系列:','全部购买:','全部特卖:','关于:','即将推出:','可持续发展','周末精选:','品牌:','商场:','商店:','礼品券:','礼物:',
    '畅销商品:','google.com','javascript:void(0)','家:','/#'
]
# 过滤函数 230294
def filter_data(line):
    return any(kw in line for kw in include_keywords)

filtered_data = np.array(websites_result)[np.vectorize(filter_data)(websites_result)]

# 获取需要保留的数据（不在filtered_data中的数据）
data_to_keep = [line for line in websites_result if line not in filtered_data]

if xie_url_txt:
    try:
        with open(url_txt, 'w', encoding='utf-8') as file:
            for line in data_to_keep:
                file.write(line + '\n')
    except Exception as e:
        print(e)
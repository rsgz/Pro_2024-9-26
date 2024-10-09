import subprocess,time

# 打开指定谷歌
def open_guge(profile = "134", port = "9530"):
    r"""
    port=9530
    Profile 134
    """
    guge = r"D:\58-chrome\chrome-win64\chrome.exe"
    user_data = r"D:\58-chrome\user01"
    open_url = r"https://www.baidu.com"
    # canshu = r'"{}" --profile-directory="Profile {}" --remote-debugging-port={} --new-window {}'.format(guge,profile,port,open_url)
    canshu = r'"{}" --user-data-dir="{}" --remote-debugging-port={} --new-window {}'.format(guge,user_data,port,open_url)
    subprocess.run(canshu, shell=True, stdout=subprocess.PIPE)

while True:
    t=time.strftime('%H:%M:%S', time.localtime(time.time()))
    # profile = input("端口默认9530 请输入指定wish配置序号:")

    print(t)
    # open_guge(profile =str(profile), port = "9530")
    open_guge(profile = "134", port = "9530")
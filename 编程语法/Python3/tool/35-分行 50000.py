r'''
这个文件就是分行操作 n个网址放一组
'''
import pandas as pd
import os
j = os.path.join
n = 20000

def read_lines_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().splitlines()


def save_links_to_excel(links, filename, start_index=0, chunk_size=n):
    # 计算应该保存的链接数量
    num_links_to_save = min(chunk_size, len(links) - start_index)

    # 获取要保存的链接片段
    links_chunk = links[start_index:start_index + num_links_to_save]

    # 创建一个 DataFrame
    df = pd.DataFrame(links_chunk, columns=['URL'])

    # 将 DataFrame 保存到 Excel 文件
    df.to_excel(filename, index=False)


def main():
    # 读取文本文件中的所有链接
    text = r"C:\Users\Administrator\Desktop\rust_url4.txt"
    links=read_lines_from_file(text)

    # 计算需要多少个 Excel 文件来保存所有链接
    num_files = len(links) // n + (1 if len(links) % n != 0 else 0)

    mu = r"C:\Users\Administrator\Desktop\all"
    if not os.path.exists(mu):
        print("创建了{}".format(mu))
        os.makedirs(mu)

    # 保存链接到多个 Excel 文件
    for i in range(num_files):
        start_index = i * n
        filename = r"C:\Users\Administrator\Desktop\all\output_{}.xlsx".format(i + 1)
        save_links_to_excel(links, filename, start_index)


if __name__ == '__main__':
    main()
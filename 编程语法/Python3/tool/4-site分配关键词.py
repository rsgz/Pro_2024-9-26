# 参数 lines_per_group 设置为 3
lines_per_group = 3

# 读取关键词文件并处理
def process_keywords(file_path, lines_per_group):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 按照指定的行数分组
    grouped_lines = [lines[i:i + lines_per_group] for i in range(0, len(lines), lines_per_group)]

    # 格式化输出
    formatted_output = []
    for group in grouped_lines:
        # 去除每行末尾的换行符并合并
        combined_lines = ' '.join(line.strip() for line in group)
        # 添加到输出列表
        # formatted_output.append(f"site:myshopify.com {combined_lines}")
        formatted_output.append(f"site:myshopify.com {','.join(line.strip() for line in group)}")

    return formatted_output

# 调用函数并打印结果
file_path = 'dc/line92.txt'
output = process_keywords(file_path, lines_per_group)
for line in output:
    print(line)

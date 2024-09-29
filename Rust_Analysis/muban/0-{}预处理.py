s = r"""
let dir_set = if let Ok(dir_set) = fs::read_dir(dir_path) {
    dir_set
} else {
    eprintln!("Failed to read directory.");
    return; // 如果读取目录失败，提前退出程序
};
"""
s = s.replace("{","{{").replace("}","}}")
lines = s.split('\n')
new_text = '\n'.join(lines[1:])  # 去除第一行
print(new_text)
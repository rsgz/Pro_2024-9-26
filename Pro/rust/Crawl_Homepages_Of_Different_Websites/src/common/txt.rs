use std::fs::File;
use std::path::Path;
use std::io::{self, BufRead, BufReader};

// 调用这个函数 直接可以获取 文本文件里面  所有行数据
/*
let file_path = r"C:\Users\Administrator\Desktop\新技术.txt";
let mut urls = match get_lines(file_path) {
    Ok(urls) => urls,
    Err(e) => {
        eprintln!("打开文件失败: {}", e);
        // return Err(e);
        Vec::new()
    }
};

dbg!(urls);
*/

pub fn get_lines<P>(filename: P) -> io::Result<Vec<String>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let mut lines = Vec::new();
    for line in reader.lines() {
        let line = line?;
        // 可以选择在这里添加对网址格式的验证
        lines.push(line);
    }

    Ok(lines)
}
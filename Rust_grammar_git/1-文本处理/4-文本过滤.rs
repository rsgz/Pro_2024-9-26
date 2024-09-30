#![allow(dead_code)]
#![allow(unused_variables)]


// use std::collections::HashSet;
// 读数据
use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::path::Path;
// 写数据
use std::fs::OpenOptions;
use std::io::Write;


fn read_lines_from_file<P>(filename: P) -> io::Result<Vec<String>>
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

fn main() {
    let file_path = r"C:\Users\Administrator\Desktop\rust_url2.txt";

    let urls = read_lines_from_file(file_path).unwrap();
    let l1 = urls.len();

    // 过滤包含 '/collections/' 的 URL
    let filtered_urls: Vec<String> = urls.into_iter()
        .filter(|url| url.contains("/collections/"))
        .collect();

    // let unique_urls: HashSet<_> = urls.into_iter().collect();  // 使用 HashSet 对 urls 去重
    let l2 = filtered_urls.len();
    

    let file_path = r"C:\Users\Administrator\Desktop\rust_url3.txt"; // 保存的文件路径
    let mut file = OpenOptions::new()
        .create(true)
        .append(true)
        .open(file_path)
        .expect("无法创建文本文件");

    for (i,k) in filtered_urls.iter().enumerate(){
        if i % 10000 == 0 { // 每1000条记录打印一次
            println!("{}-->{}",i,k);
        }
        writeln!(file, "{}", k).expect("不能将链接写入到文本文件");
    }

    println!("{}--->{}",l1,l2); // 1795365--->722789
}



/*
let file_path = r"C:\Users\Administrator\Desktop\rust_ur2.txt";
let urls = read_lines_from_file(file_path).unwrap();
已经将urls数组拿到了  现在想做元素判断 元素里面包函字符串的 '/collections/'  都保留 其他的都过滤掉
*/
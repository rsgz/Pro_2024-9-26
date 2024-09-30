#![allow(unused_imports)]
#![allow(path_statements)]
#![allow(unused_variables)]
#![allow(unused_mut)]
#![allow(unused_must_use)]

use std::fs;  // 获取目录
// use std::io;
use std::collections::HashSet;  // 去重
// 写数据
use std::fs::OpenOptions;
use std::io::Write;
// 读数据
use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::path::Path;

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

fn main(){
    let dir_path = r"C:\Users\Administrator\Desktop\data\err"; 
    let mut dir_set: fs::ReadDir = fs::read_dir(dir_path).unwrap();
    
    let mut lines = Vec::new();  // 这个就是存储 所有的文本行
    for (i,dir) in dir_set.into_iter().enumerate(){
        let mulu_file: fs::DirEntry = dir.expect("解析dir出现问题");
        let file_name = mulu_file.path().to_string_lossy().into_owned();
        println!(">>>>>> s ---> {:#?}",file_name);
        let mut urls: Vec<String> = get_lines(file_name).unwrap();
        //  一步去重
        let urls_set: HashSet<String> = urls.drain(..).collect();
        urls = urls_set.into_iter().collect();

        for line in urls {
            lines.push(line);
        }
    }

    let file_path = r"C:\Users\Administrator\Desktop\all3.txt"; // 保存的文件路径
    let mut file = OpenOptions::new()
        .create(true)
        .append(true)
        .open(file_path)
        .expect("无法创建文本文件");

    for (i,k) in lines.iter().enumerate(){
        if i % 10000 == 0 { // 每1000条记录打印一次
            println!("{}-->{}",i,k);
        }
        writeln!(file, "{}", k).expect("不能将链接写入到文本文件");
    }
}
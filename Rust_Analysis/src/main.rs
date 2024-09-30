#![allow(unused_imports)]
#![allow(path_statements)]
#![allow(unused_variables)]
#![allow(unused_mut)]
#![allow(unused_must_use)]

use std::path::PathBuf;  // 拼接路径
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

fn xin(file_path:&str)->io::Result<File>{
    let mut file = OpenOptions::new()
        .create(true)
        .append(true)
        .open(file_path)
        .expect("无法创建文本文件");
    Ok(file)
}


fn main(){
    // 这个小项目  是想实现 
    let file_path = r"C:\Users\Administrator\Desktop\data\err"; 
    let mut urls: Vec<String> = get_lines(file_path).unwrap();

    let base_dir = r"C:\Users\Administrator\Desktop\split"; // 保存的文件路径
    let mut path_save = PathBuf::new();
    path_save.push(base_dir);

    let mut fenzu = Vec::new();
    let fen_n = 20000;
    let zu = if urls.len()%fen_n==0{
        let zu = urls.len()/fen_n;
        zu
    }else{
        let zu = urls.len() as f64 /fen_n as f64;
        let zu2 = zu.ceil() as usize;
        zu2
    };

    for i in 0..zu{
        // fenzu.push((i*20000,(i+1)*20000));
        fenzu.push((i*fen_n,(i+1)*fen_n));
    }

    //  一步去重
    // let urls_set: HashSet<String> = urls.drain(..).collect();
    // urls = urls_set.into_iter().collect();
    for (i,line) in urls.iter().enumerate() {
        for xiaozu in fenzu{
            // if 20000*j<i<20000*(j+1)
            let (start, end) = xiaozu;
            if start<i && i<end{
                let path_save_i = path_save.clone();
                path_save_i.push(start.to_string());
                let file_current = xin(path_save);
                writeln!(file, "{}", k).expect("不能将链接写入到文本文件"); 
            }
        }
    }
}
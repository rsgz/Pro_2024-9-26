#![allow(unused_imports)]
#![allow(path_statements)]
#![allow(unused_variables)]

use std::fs;
use std::io;

fn main() {
    
    let dir_path: &str = r"\\PC-202407311638\share";   // 注意路径分隔符需要双斜杠
    let obj: Result<fs::ReadDir, io::Error> = fs::read_dir(dir_path);

    let dir_set = if let Ok(dir_set) = fs::read_dir(dir_path) {
        dir_set
    } else {
        eprintln!("大帅比警告:解析变量失败 xxxxxxxx ");
        return;  // 提前退出程序
    };
    println!("{:#?}",dir_set);

    for zi in dir_set{
        
    }
}
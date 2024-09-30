#![allow(unused_imports)]
#![allow(path_statements)]
#![allow(unused_variables)]
#![allow(unused_mut)]

use std::fs;
use std::io;

fn main() -> std::io::Result<()> {
    let dir_path = r"\\PC-202407311638\share"; 
    let mut dir_set: fs::ReadDir = fs::read_dir(dir_path)?;
    println!("{:#?}",dir_set);
    Ok(())
}

/*
fn main() {
    
    let dir_path: &str = r"\\PC-202407311638\share";   // 注意路径分隔符需要双斜杠
    let obj: Result<fs::ReadDir, io::Error> = fs::read_dir(dir_path);

    

    let mut dir_set = match fs::read_dir(dir_path) {
        Ok(dir_set) => {
            dir_set
        },
        Err(e) => {
            eprintln!("大帅比警告:解析变量失败 ---> {}", e);
            return ();
        }
    };
    // println!("{:#?}",dir_set);
    // for zi in dir_set{


}
*/
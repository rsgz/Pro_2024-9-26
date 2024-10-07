#![allow(unused_imports)]
#![allow(path_statements)]
#![allow(unused_variables)]
#![allow(unused_mut)]
#![allow(unused_must_use)]

use std::fs::File;
use std::path::Path;
use std::io::{self, BufRead, BufReader};
use std::fs;
// use std::io;

fn main() -> io::Result<()> {
    let dir_path: &str = r"\\PC-202407311638\share"; // 注意路径分隔符需要双斜杠
    for entry in fs::read_dir(dir_path)? { // 正确地遍历 dirset
        println!("{:?}", entry?.path().display());
    }
    Ok(())
}
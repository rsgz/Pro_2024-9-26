#![allow(unused_imports)]
#![allow(path_statements)]
#![allow(unused_variables)]
#![allow(unused_mut)]
#![allow(unused_must_use)]

use std::fs;
use std::io;

fn main(){
    let dir_path = r"\\PC-202407311638\share"; 
    let mut dir_set: fs::ReadDir = fs::read_dir(dir_path).unwrap();
    for (i,dir) in dir_set.into_iter().enumerate(){
        let mulu_file: fs::DirEntry = dir.expect("解析dir出现问题");
        let file_name = mulu_file.path().to_string_lossy().into_owned();
        println!(">>>>>> s ---> {:#?}",file_name);
    }
}
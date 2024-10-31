#![allow(unused_variables)]
#![allow(unused_mut)]  // warning: variable does not need to be mutable
#![allow(unused_assignments)]
#![allow(unused_imports)]  // warning: unused import: `std::i8`
#![allow(dead_code)]  // warning: fields `x` and `y` are never read
#![allow(path_statements)]
#![allow(unused_must_use)]

use std::fmt::Debug;  // 结构体
use std::path::PathBuf;  // 拼接路径
use std::fs;  // 获取目录
use std::collections::HashMap; // 键值对

// use std::io;
use std::collections::HashSet;  // 去重
// 写数据
use std::fs::OpenOptions;
use std::io::Write;
// 读数据
use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::path::Path;
// opencv
use opencv::{core, imgproc, prelude::*, highgui};




fn main() -> opencv::Result<()>{
    // 小图
    let img = core::Mat::imread(r"D:\Backup\Downloads\1-click\qidong\1.png", imgproc::IMREAD_GRAYSCALE)?;
    // 大图
    let template = core::Mat::imread(r"D:\Backup\Downloads\1-click\qidong\2.png", imgproc::IMREAD_GRAYSCALE)?;
    // 检查图像是否加载成功
    if img.empty()? || template.empty()? {
        panic!("无法加载图像!");
    }else{
        print!("都加载成功!");
    }

    Ok(())
}
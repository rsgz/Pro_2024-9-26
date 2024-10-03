#![allow(dead_code)]    // 函数未使用的时候 用
#![allow(unused_variables)]  // 未使用 变量
#![allow(unused_imports)]  // 导入不使用
#![allow(path_statements)]  // x;  的时候用
// #[cfg(test)]  // 未使用的模块 也可以标记一下 说明是测试的时候用
// #[derive(Debug)]  // 该属性可以应用于 结构体、枚举和联合体 等类型
#![allow(unused_mut)]  // 无需可变
#![allow(unused_must_use)]  //

/*
[dependencies]
calamine = "0.25.0"
*/

extern crate calamine;
use calamine::{open_workbook_auto,open_workbook, Reader, Xlsx};
// 路径拼接
use std::path::Path;
// use crate::slice;
// use std::slice::SliceIndex;
// 迭代一层目录文件
use std::fs;
use std::io;
// 写数据
use std::fs::OpenOptions;
use std::io::Write;

// 提取表格a列数据-->数组
fn lie_to_vec(file_path:&Path,lie:usize)-> Result<Vec<String>, Box<dyn std::error::Error>> {
    // let path = r"C:\Users\Administrator\Desktop\数据\第四批数据\output_1.xlsx"; // 请替换为你的文件路径
    let mut workbook: Xlsx<_>= open_workbook(file_path)?;
    // 获取工作簿中的第一个工作表
    let sheet1 = workbook.worksheet_range("工作表1")?; // 请替换为你的工作表名称
    // 提取A列的数据
    let mut a_column: Vec<String> = Vec::new();
    for row in sheet1.rows() {
        if let Some(cell) = row.get(lie) { // A列是第0列
            let v = cell.to_string();
            // println!("{}",v);
            a_column.push(v);
        }
    }
    Ok(a_column)
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut a_column_all: Vec<String> = Vec::new();
    let dir_path = r"C:\Users\Administrator\Desktop\数据\第四批数据\xlsx"; 
    let mut dir_set: fs::ReadDir = fs::read_dir(dir_path).unwrap();
    // 合并所有a列
    for (i,dir) in dir_set.into_iter().enumerate(){
        if i==i{
            let mulu_file: fs::DirEntry = dir.expect("解析dir出现问题");
            // let s = mulu_file.path().display();
            let file_path = mulu_file.path().to_string_lossy().into_owned();
            // println!(">>>>>> s ---> \n{:#?}",mulu_file.path().display());
            println!(">>>>>> file_path ---> {:#?}",file_path);

            // 打开XLSX文件
            // let path = Path::new(r"C:\Users\Administrator\Desktop\数据\第四批数据\output_1.xlsx");
            let file_path1 = Path::new(file_path.as_str());
            let lie_a_set = if let Ok(lie_a_set) = lie_to_vec(file_path1,0) {
                //println!("lie_a_set ---> {:#?}",lie_a_set);
                lie_a_set
            } else {
                eprintln!("大帅比警告:解析变量失败 xxxxxxxx ");
                return Ok(());  // 提前退出程序
            };
            //println!("lie_a_set ---> {:#?}",lie_a_set);
            a_column_all.extend(lie_a_set);
        }
    }

    let file_path = r"C:\Users\Administrator\Desktop\rust_url_all.txt"; // 保存的文件路径
    let mut file = OpenOptions::new()
        .create(true)
        .append(true)
        .open(file_path)
        .expect("无法创建文本文件");

    for (i,k) in a_column_all.iter().enumerate(){
        if i % 10000 == 0 { // 每1000条记录打印一次
            println!("{}-->{}",i,k);
        }
        writeln!(file, "{}", k).expect("不能将链接写入到文本文件");
    }
    
    // 输出A列的数据
    // for (i,value) in a_column.into_iter().enumerate() {
    //     println!("{} ---> {}", i,value);
    // }
    Ok(())
}

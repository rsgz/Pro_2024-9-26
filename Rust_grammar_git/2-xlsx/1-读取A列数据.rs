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
use std::path::Path;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // 打开XLSX文件
    let path = Path::new(r"C:\Users\Administrator\Desktop\数据\第四批数据\output_1.xlsx");
    // let path = r"C:\Users\Administrator\Desktop\数据\第四批数据\output_1.xlsx"; // 请替换为你的文件路径
    let mut workbook: Xlsx<_>= open_workbook(path)?;

    // 获取工作簿中的第一个工作表
    let sheet1 = workbook.worksheet_range("工作表1")?; // 请替换为你的工作表名称

    // 提取A列的数据
    // let mut a_column: Vec<String> = Vec::new();
    for row in sheet1.rows() {
        if let Some(cell) = row.get(0) { // A列是第0列
            let v = cell.to_string();
            println!("{}",v);
            // a_column.push(value);
        }
    }

    // 输出A列的数据
    // for value in a_column {
    //     println!("{}", value);
    // }

    Ok(())
}

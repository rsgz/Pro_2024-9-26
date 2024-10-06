// use std::io::stdin;
use std::io::{stdin, Write,stdout};

pub fn function_in_sub_module() {
    println!("called `module1::sub_module::function_in_sub_module()`");
}

// 点击 任意键 关闭 cmd窗口
pub fn end(){
    println!("你可以-->按任意键 关闭...");
    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();
}

// 输入 字符串
// let name:String=input(String::from("请输入一些话:"));
pub fn input(some_string:String) -> String {
  print!("{}",some_string);
  stdout().flush().unwrap(); 
  let mut input = String::new();
  stdin().read_line(&mut input).expect("读取不到用户输入的数据!");
  input.trim().to_string()
}
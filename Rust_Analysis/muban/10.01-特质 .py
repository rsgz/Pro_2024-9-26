crate = "Temp"

特质名1 = "Summary"
特质_方法1 = "summarize"
特质_方法2 = "summarize_author"

结构体1 = "Tweet"

r"""
特质方法 先实现 特质_方法1
特质方法 返回结构体字段的值 字符串
"""

s = f"""
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ lib.rs ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
#![allow(non_snake_case)]  //
pub trait {特质名1} {{
    
    fn {特质_方法1}(&self) -> String {{
        format!("(Read more from {{}}...)", self.{特质_方法2}())
    }}

    fn {特质_方法2}(&self) -> String;
}}

pub struct {结构体1} {{
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}}


impl {特质名1} for {结构体1} {{
    fn {特质_方法2}(&self) -> String {{
        format!("@{{}}", self.username)
    }}
}}


﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ main.rs ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
use {crate}::{{{特质名1,结构体1}}};


fn main() {{
    let tweet = {结构体1} {{
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    }};
    println!("1 new tweet: {{}}", tweet.{特质_方法1}());
}}
"""

print(s)
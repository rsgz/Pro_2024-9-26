
特质名1 = "Summary"
特质_方法1 = "summarize"

结构体1 = "NewsArticle"
结构体2 = "Tweet"

r"""
特质方法先声明 后实现
特质方法 返回结构体字段的值 字符串
"""

s = f"""
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ lib.rs ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
pub trait {特质名1} {{
    fn {特质_方法1}(&self) -> String;
}}

pub struct {结构体1} {{
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}}

impl {特质名1} for {结构体1} {{
    fn {特质_方法1}(&self) -> String {{
        format!("{{}}, by {{}} ({{}})", self.headline, self.author, self.location)
    }}
}}

pub struct {结构体2} {{
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}}

impl {特质名1} for {结构体2} {{
    fn {特质_方法1}(&self) -> String {{
        format!("{{}}: {{}}", self.username, self.content)
    }}
}}

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ main.rs ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
use Temp::{{{结构体1}, {结构体2}}};

fn main() {{
    let tweet = {结构体2} {{
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
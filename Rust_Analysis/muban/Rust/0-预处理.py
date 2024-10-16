# 下面设置 变量 部分
v1 = "obj"  # 这个建议设置一个模板变量
tishi = ""  # 提示部分

r"""
主要就是去掉大括号的影响
"""

def quchu_shouhang(s):
    lines = s.split('\n')
    new_text = '\n'.join(lines[1:])  # 去除第一行
    return new_text

s = r"""
pub trait Summary {
    fn summarize_author(&self) -> String;

    fn summarize(&self) -> String {
        format!("(Read more from {}...)", self.summarize_author())
    }
}

impl Summary for Tweet {
    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}

let tweet = Tweet {
    username: String::from("horse_ebooks"),
    content: String::from(
        "of course, as you probably already know, people",
    ),
    reply: false,
    retweet: false,
};
println!("1 new tweet: {}", tweet.summarize());

"""
start = "﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ 代码生成 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀"
end = "﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ 代码结束 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀"
huan = '\n'
o1 = f'{v1} = ""  # {tishi} '  # obj = "vvv"  # 请输入 打印对象叫啥名字
o2 = "sentence = f'''\\"+"\n"              # sentence = f"""\
o3 = r"""
'''
print(sentence)
"""
s = huan+o2+quchu_shouhang(s)+quchu_shouhang(o3)
s = s.replace("{","{{").replace("}","}}")  # 兼容{}语法
new_text = s.replace(v1,f"{{{v1}}}")
last = start+huan+o1+huan+new_text+end  # o1放到替换变量之后加上去,防止被替换
print(last)

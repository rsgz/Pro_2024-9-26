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
fn main() {
    let mut s = String::from("hello");
    s.push_str(", world!"); // push_str() 在字符串后追加字面值
    println!("{}", s); // 将打印 `hello, world!`
}
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

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
    let numbers = vec![1, 2, 3, 4, 5];
    let numbers2: Vec<_> = numbers.iter().map(|num| {
        let v = num*100;
        let name = format!("niubi_{}",num);  // 构建字符串
        (num,v)
    }).collect();
    print!("{:?}",numbers2);  // [(1, 100), (2, 200), (3, 300), (4, 400), (5, 500)]
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

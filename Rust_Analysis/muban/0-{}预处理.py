# 下面设置 变量 部分
v1 = "obj"  # 这个建议设置一个
tishi = ""  # 提示部分


s = r"""
sentence = f'''\
print!("{:?}",obj);
print!("{:#?}",obj);
println!("{:?}",obj);
println!("{:#?}",obj);
dbg!(obj);

if i%10000==0 {
    println!("{:?}-->{:?}", i,url);
}
'''
print(sentence)
"""

s = f'{v1} = ""  # 请输入 打印对象叫啥名字 '+s

s = s.replace("{","{{").replace("}","}}")  # 兼容{}语法

# 因为后期改变了那个 第一行 的写法 所以不用去除第一行了
# lines = s.split('\n')
# new_text = '\n'.join(lines[1:])  # 去除第一行

# 下面设置 变量 部分
# v1 = "obj"  # 这个建议设置一个
# new_text = new_text.replace(v1,f"{{{v1}}}")
# print(new_text)

print(s)
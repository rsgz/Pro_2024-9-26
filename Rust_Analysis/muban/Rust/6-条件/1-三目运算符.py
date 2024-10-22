

sentence = f'''\
let x=100;
let z = if x % 2 == 1 {{ "odd 奇数" }} else {{ "even 偶数" }}; // 三目运算符 判断奇偶数
println!("{{}}", z); // 调用闭包并打印结果
'''
print(sentence)
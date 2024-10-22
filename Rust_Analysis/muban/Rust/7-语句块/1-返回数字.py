sentence = f'''\
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ 返回数字 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
let y = {{
    let x: i32 = 3;
    x + 1
}};
println!("{{}}",y);

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ 返回String ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
let y: String = {{
    let x: String = "33".to_string();
    x
}};
println!("{{}}",y); // "33"

或者
let s = "6666666666";
let spaces3: String = {{
    let temp2: String = s.len().to_string(); // 创建 String 对象
    temp2 // 获取一个字符串切片
}};
println!("{{}}",spaces3); // 10 String

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ 返回String ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀

'''
print(sentence)
sentence = f'''\
fn main() {{
    let x = 5;
    let x = x + 1;  // 在main函数的作用域内对之前的x进行遮蔽
    {{
        let x = x * 2;  // 在当前的花括号作用域内，对之前的x进行遮蔽
        println!("The value of x in the inner scope is: {{}}", x);
    }}
    println!("The value of x is: {{}}", x);
}}
'''
print(sentence)
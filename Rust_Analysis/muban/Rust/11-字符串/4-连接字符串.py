s1 = ""
s2 = ""

sentence = f'''\
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ push_str ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
fn main() {{
    let mut s = String::from("hello");
    s.push_str(", world!"); // push_str() 在字符串后追加字面值
    println!("{{}}", s); // 将打印 `hello, world!`
}}
或者
fn main() {{
    let mut s = String::from("Hello ");
    s.push_str("rust");
    println!("追加字符串 push_str() -> {{}}", s);
    s.push('!');
    println!("追加字符 push() -> {{}}", s);
}}
'''
print(sentence)
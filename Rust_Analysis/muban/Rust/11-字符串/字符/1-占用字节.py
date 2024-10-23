sentence = f'''\
// Rust 中的字符是 Unicode 类型，因此每个字符占据 4 个字节内存空间
fn main() {{
    let x = '中';
    println!("字符'中'占用了{{}}字节的内存大小",std::mem::size_of_val(&x));
}}
'''
print(sentence)
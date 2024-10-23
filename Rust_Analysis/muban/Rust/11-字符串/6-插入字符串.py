sentence = f'''\
fn main() {{
    let mut s = String::from("Hello rust!");
    s.insert(5, ',');
    println!("插入字符 insert() -> {{}}", s);
    s.insert_str(6, " I like");
    println!("插入字符串 insert_str() -> {{}}", s);
}}
'''
print(sentence)
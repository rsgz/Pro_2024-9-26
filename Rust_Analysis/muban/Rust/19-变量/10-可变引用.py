sentence = f'''\
// 可变引用同时只能存在一个
fn main() {{
    let mut s = String::from("hello");
    change(&mut s);
}}

fn change(some_string: &mut String) {{
    some_string.push_str(", world");
}}
'''
print(sentence)

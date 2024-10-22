sentence = f'''\
fn calculate_length(s: &String) -> usize {{
    s.len()
}}

fn main() {{
    let s1 = String::from("hello");
    let len = calculate_length(&s1);
    println!("长度 '{{}}' is {{}}.", s1, len);
}}
'''
print(sentence)
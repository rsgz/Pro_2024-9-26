sentence = f'''\
fn clear(text: &mut String) -> () {{
    *text = String::from("");
}}

fn main() {{
    let mut text = String::from("rsgz");
    clear(& mut text);
    print!("{{:#?}}",text);
}}
'''
print(sentence)
sentence = f'''\
fn main() {{
    let data = "  Yellow-eyed penguin,65  ";
    let fields: Vec<_> = data.split(',').map(|field| field.trim()).collect();
    print!("{{:?}}",fields);  // ["Yellow-eyed penguin", "65"]
}}
'''
print(sentence)
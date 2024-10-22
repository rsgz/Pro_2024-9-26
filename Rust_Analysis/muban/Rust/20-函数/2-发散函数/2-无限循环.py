sentence = f'''\
fn forever() -> ! {{
    loop {{
        //...
    }};
}}

fn main() {{
    forever();
    println!("{{}}",666);
}}
'''
print(sentence)
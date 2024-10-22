类型 = "i16"

sentence = f'''\
fn main() {{
    // 适合不同变量 类型
    let max = {类型}::MAX;
    let min = {类型}::MIN;
    println!("{{}}~{{}}",max,min);
}}
'''
print(sentence)
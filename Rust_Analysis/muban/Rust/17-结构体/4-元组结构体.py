sentence = f'''\
fn main() {{
    // 定义结构体
    #[derive(Debug)]
    struct Color(i32, i32, i32);
    #[derive(Debug)]
    struct Point(i32, i32, i32);  // 结构体必须要有名称，但是结构体的字段可以没有名称

    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
    println!("{{:?}}", black);
    println!("{{:?}}", origin);
}}
'''
print(sentence)
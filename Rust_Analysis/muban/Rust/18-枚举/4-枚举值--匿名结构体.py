sentence = f'''\
#[derive(Debug)]
enum Message {{
    Quit,  // 没有关联任何数据
    Move {{ x: i32, y: i32 }},  // 匿名结构体
    Write(String),  // String 字符串
    ChangeColor(i32, i32, i32),  // 三个 i32
}}

fn main() {{
    let m1: Message = Message::Quit;
    let m2: Message = Message::Move{{x:1,y:1}};
    let m3: Message = Message::ChangeColor(255,255,0);
    print!("{{:#?}}",m1);
    print!("{{:#?}}",m2);
    print!("{{:#?}}",m3);
}}

/*
QuitMove {{
    x: 1,
    y: 1,
}}

ChangeColor(
    255,
    255,
    0,
)
*/
'''
print(sentence)
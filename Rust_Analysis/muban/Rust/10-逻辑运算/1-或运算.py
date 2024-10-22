sentence = f'''\
fn main() {{
    let penguin_data = "\\
    common name,length (cm)
    Little penguin,33
    Yellow-eyed penguin,65
    Fiordland penguin,60
    Invalid,data
    ";
    // 分行 返回数组
    for (i,zi) in penguin_data.lines().enumerate() {{
        // println!("{{}}--->{{}}", i,&zi);
        // 跳过第一行和空白行 空行   或运算
        if i == 0 || zi.trim().len() == 0{{
            continue;
        }}
        println!("{{}}--->{{}}", i,&zi);
    }}
}}
'''
print(sentence)
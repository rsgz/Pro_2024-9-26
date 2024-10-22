sentence = f'''\
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ 简单闭包 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
fn main() {{
    let numbers = vec![1, 2, 3, 4, 5];
    let numbers2: Vec<_> = numbers.iter().map(|num| num*num).collect();
    print!("{{:?}}",numbers2);  // [1, 4, 9, 16, 25]
}}

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ 复杂闭包 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
fn main() {{
    let numbers = vec![1, 2, 3, 4, 5];
    let numbers2: Vec<_> = numbers.iter().map(|num| {{
        let v = num*100;
        let name = format!("niubi_{{}}",num);  // 构建字符串
        (num,v)
    }}).collect();
    print!("{{:?}}",numbers2);  // [(1, 100), (2, 200), (3, 300), (4, 400), (5, 500)]
}}
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ 代码结束 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
'''
print(sentence)
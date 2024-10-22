sentence = f'''\
 use std::fmt::Debug;

 // 定义一个结构体，并自动派生 Debug 特质
 #[derive(Debug)]
 struct Point {{
     x: i32,
     y: i32,
 }}

 fn report<T: Debug>(item: T) {{
     println!("{{:?}}", item);
 }}

 fn main() {{
     let point = Point {{ x: 10, y: 20 }};
     println!("{{:?}}", point); // 输出: Point {{ x: 10, y: 20 }}
     report(point); // 输出: Point {{ x: 10, y: 20 }}
 }}

'''
print(sentence)

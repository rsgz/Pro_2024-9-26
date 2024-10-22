报错 = r"""
error[E0716]: temporary value dropped while borrowed
let s: &str = usize_data.to_string().as_str();
to_string()创建的 string 对象是一个临时值 必须掷定新变量 延长生命周期

修复1： 利用mut 可变性 (需要同类型)
    let mut ss: &str = "";
    let usize_data:usize= 100;
    let s: String = usize_data.to_string();
    ss = s.as_str();  // "100"
    println!("{:?}",ss);

修复2： 利用let 变量遮蔽 (可以不同数据类型)
    let ss: &str = "";
    let usize_data:usize= 100;
    let s: String = usize_data.to_string();
    let ss = s.as_str();  // "100"
    println!("{:?}",ss);

"""


&str = r"""
=========================== &str--> =========================== 
&str-->&str
let spaces = "  100 ";
let spaces = spaces.trim();

&str-->String
let spaces = " bbb 100 a";
let spaces = spaces.to_uppercase();

&str-->数字
let s:i32 = "42".parse().expect("解析错了");
let s:i32 = "42".parse::<i32>().unwrap();

&str-->usize
spaces2.len()

&str-->迭代器
let data = "  Yellow-eyed penguin,65  ";
let fields: Vec<_> = data.split(',')
"""

char = r"""
=========================== char--> ===========================
char-->u8
let c: u8 = 'a' as u8; // 将字符'a'转换为整数，97

"""


u16 = r"""
u16-->u8      超过范围就会报错
let a: u8 = 10;
let b: u16 = 15;
let b2: u8 = b.try_into().unwrap();


"""

usize = r"""
=========================== usize--> ===========================
usize-->String
let temp: String = spaces2.len().to_string();
"""

i8 = r"""
=========================== i8--> ===========================
i8-->i32
let b: i32 = 100_i8 as i32;  // 100

"""

f32= r"""
=========================== f32--> ===========================
f32-->
let y: f32 = 3.0; // f32
"""

f64 = r"""
=========================== f64--> ===========================
f64-->i8
let a = 3.1 as i8;  // 3
"""

String= r"""
=========================== String--> ===========================
String-->&str
spaces2 = temp.as_str();
或者
let y: String = {{
    let x: String = "33".to_string();
    x // 返回 String 对象本身
}};

let y: &str = y.as_str();
println!("{{}}", y); // 调用闭包并打印结果
"""

迭代器 = r"""
=========================== 迭代器--> ===========================
迭代器-->迭代器适配器-->迭代器
map 是一个迭代器适配器方法,会返回一个新的迭代器
let data = "  Yellow-eyed penguin,65  ";
let fields: Vec<_> = data.split(',').map(|field| field.trim())

迭代器适配器
map
filter
fold
scan
for_each

迭代器-->数组
collect() 将迭代器转化成 数组
data.split(',').map(|field| field.trim()).collect();
"""

数组 = r"""
=========================== 数组--> ===========================
数组-->迭代器
enumerate() 方法返回一个迭代器
for (i, record) in records.enumerate()
或者
let numbers: Vec<i32> = vec![1, 2, 3, 4, 5];
let squares: std::slice::Iter<'_, i32> = numbers.iter();
"""

NaN = r"""
=========================== -->NaN ===========================
判断一个数值是否是 NaN
let x = (-42.0_f32).sqrt();
if x.is_nan() {
    println!("未定义的数学行为")
}
"""

内存地址 = r"""
内存地址-->指针
https://course.rs/advance/into-types/converse.html

"""

函数 = r"""
fn add_with_extra(x: i32, y: i32) -> i32 {}
fn add(x:u32,y:u32) -> u32 {}
fn plus_or_minus(x:i32) -> i32 {}
fn clear(text: &mut String) -> () {}

"""

笔记 = r"""
基本数据类型
布尔类型（Boolean）  bool: 可以是 true 或 false。
字符类型（Character）  char: 表示一个 Unicode 标量值，如 ‘a’、‘α’ 和 ‘∞’。

整数类型（Integer Types）
有符号整数：i8, i16, i32, i64, i128 和 isize（指针大小）。
无符号整数：u8, u16, u32, u64, u128 和 usize（指针大小）。

浮点类型（Floating-Point Types）
f32: 32位浮点数。
f64: 64位浮点数（默认）。

原始指针（Raw Pointers）
*const T: 指向类型 T 的不可变原始指针。
*mut T: 指向类型 T 的可变原始指针。

函数指针（Function Pointers）
例如，fn() 表示一个不带参数和返回值的函数指针。

数组（Array）   [T; N]: 一个固定大小为 N 的元素类型为 T 的数组。

切片（Slice）   [T]: 一个动态大小、连续序列的 T 类型元素的引用。

元组（Tuple）  (T, U, ...): 有限数量的异构元素的组合。

复合数据类型（Compound Types）
结构体（Struct）   可以定义自定义的数据结构。
枚举（Enum）       可以定义一组命名的值，每个值都可以有相关的数据。
联合（Union）      可以在相同的内存位置存储不同的数据类型。
"""
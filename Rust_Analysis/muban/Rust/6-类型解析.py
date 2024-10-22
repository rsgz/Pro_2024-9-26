r"""
&str-->&str
let spaces = "  100 ";
let spaces = spaces.trim();


&str-->usize
spaces2.len()

&str-->String
let spaces = " bbb 100 a";
let spaces = spaces.to_uppercase();



usize-->String
let temp: String = spaces2.len().to_string();

String-->&str
spaces2 = temp.as_str();

&str-->迭代器
let data = "  Yellow-eyed penguin,65  ";
let fields: Vec<_> = data.split(',')

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

数组-->迭代器
enumerate() 方法返回一个迭代器
for (i, record) in records.enumerate()
或者
let numbers: Vec<i32> = vec![1, 2, 3, 4, 5];
let squares: std::slice::Iter<'_, i32> = numbers.iter();

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
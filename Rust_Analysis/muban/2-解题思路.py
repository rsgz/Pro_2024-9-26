# 下面所有的解题思路 就是 遇到什么数据类型 怎么解析

r"""
match 语句 冗长
只对 Result 或 Option 中的某个特定变体感兴趣时，可以使用 if let 来简化代码

>>> 1
类型:dir_set: ReadDir,Iterator<Item = Result<DirEntry, Error>>
解析:for x in dir_set
# ReadDir数据类型 实现了 Iterator特质
# 特质 Iterator 有一个关联类型 Item  指定了迭代器每次迭代返回的类型
dir_set: fs::ReadDir --> Iterator<Item = Result<DirEntry, Error>>
for dir in dir_set{

}
>>> 2
类型:dir: Result<DirEntry, Error>
解析:match dir

>>> 3
类型:mulu: DirEntry,
类型:mulu: fs::DirEntry,
类型:mulu: std::fs::DirEntry,
解析:mulu.path().display();

>>> 4
borrow later used here
temporary value is freed
let file_name_str = entry.path().to_string_lossy().into_owned();
println!(">>>>>> File path ---> \n{:#?}", file_name_str);
"""

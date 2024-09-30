# 下面所有的解题思路 就是 遇到什么数据类型 怎么解析

r"""
match 语句 冗长
只对 Result 或 Option 中的某个特定变体感兴趣时，可以使用 if let 来简化代码

// Implements notable traits: Iterator<Item = Result<DirEntry, Error>>
let dir_set: ReadDir
ReadDir数据类型 实现了 Iterator特质
特质 Iterator 有一个关联类型 Item  指定了迭代器每次迭代返回的类型

dir_set: fs::ReadDir --> Iterator<Item = Result<DirEntry, Error>>
for dir in dir_set{

}
"""

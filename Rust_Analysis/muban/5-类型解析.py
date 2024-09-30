
# dir: Result<DirEntry, Error>
mode = "dir: Result<DirEntry, Error>"


# 模式理解  [解析dir_set变量，如果是Iterator类型可以直接for in迭代。然后迭代出来子元素是 Result < DirEntry, Error >]
mode = "dir_set: fs::ReadDir --> Iterator < Item = Result < DirEntry, Error >>"
解析1 = "dir_set"  # Iterator
解析2 = "dir"  # Result < DirEntry, Error >
s = f"""
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ for in 写法﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
for {解析2} in {解析1}{{
    {解析2}
}}

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ for in enumerate写法﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
for (i,{解析2}) in {解析1}.into_iter().enumerate(){{
    if i==0{{
        println!(">>>>>> {解析2} ---> \\n{{:#?}}",{解析2});
        println!(">>>>>> {解析2} ---> \\n{{:#?}}",std::any::type_name_of_val(&{解析2}));
        
    }}

}}
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ 代码结束 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
"""
print(s)
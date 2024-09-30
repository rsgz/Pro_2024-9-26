# 优米科技 运行这个 切换python3.8  跑图切换python3.10

解析 = "fs::read_dir(dir_path)"
想获取 = "dir_set"  # 你想获取解析对象里面的什么子元素呢？
sentence = f""" 
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ unwrap() 写法  外部返回值﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
let {想获取} = {解析}.unwrap();
println!("{{:#?}}",{想获取});
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ if let 写法  无返回值﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
// 将匹配到的值的作用域限制在{{}}内部   需要注意末尾加不加分号的区别
if let Ok({想获取}) = {解析} {{
    {想获取}
}};

或者
if let Ok({想获取}) = {解析} {{
    {想获取}
}} else {{
    eprintln!("大帅比警告:解析变量失败 xxxxxxxx ");
    return;  // 提前退出程序
}};

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ if let else写法  有返回值﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
// if let结合else，可以将变量的作用域扩展到if let块之外，这样就可以在块外部使用这个变量，从而减少了代码的嵌套层级
let {想获取} = if let Ok({想获取}) = {解析} {{
    {想获取}
}} else {{
    eprintln!("大帅比警告:解析变量失败 xxxxxxxx ");
    return;  // 提前退出程序
}};
println!("{{:#?}}",{想获取});

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ match 写法 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
// 解析的类型必须是 Result 类型   本质上是一种枚举类型
let obj = {解析};  # let obj: Result<fs::ReadDir, io::Error> = fs::read_dir(dir_path);

match {解析} {{
    Ok({想获取}) => {{
        {想获取};
    }},
    Err(e) => {{
        eprintln!("大帅比警告:解析变量失败 ---> {{}}", e);
    }}
}}

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ 代码结束 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
"""
print(sentence)

r"""
let path = zi.path();
        println!("{{:?}}", path.display());
"""
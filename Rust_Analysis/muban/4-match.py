# 优米科技 运行这个 切换python3.8  跑图切换python3.10

解析 = "fs::read_dir(dir_path)"
想获取 = "dir_set"  # 你想获取解析对象里面的什么子元素呢？
sentence = f""" 


﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ ? 写法  外部返回值﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
use std::io;

fn main() -> std::io::Result<()> {{
    // ? 运算符可以简化错误处理。它的工作原理是，如果结果是 Ok，它会解包 Ok 并返回里面的值；如果是 Err，它会提前返回 Err。
    let mut {想获取} = {解析}?;
    println!("{{:#?}}",{想获取});
    Ok(())
}}
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ expect() 写法  外部返回值﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
//  expect 通常不推荐用于生产代码，因为它们在遇到错误时会 panic
let {想获取} = {解析}.expect();
println!("{{:#?}}",{想获取});
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ unwrap() 写法  外部返回值﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
// unwrap 通常不推荐用于生产代码，因为它们在遇到错误时会 panic
let {想获取} = {解析}.unwrap();
println!("{{:#?}}",{想获取});

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ if let Err写法  外部返回值﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
let f = {解析};
if let Err(e) = f {{
    eprintln!("大帅比警告:解析变量失败 ---> {{}}", e);
    return Err(e);
}}
let mut {想获取} = f.unwrap();
println!("{{:#?}}",{想获取});
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ if let 写法  内部返回值﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
// 将匹配到的值的作用域限制在{{}}内部   需要注意末尾加不加分号的区别
if let Ok({想获取}) = {解析} {{
    println!("{{:#?}}",{想获取});
    {想获取}
    
}};

或者
if let Ok({想获取}) = {解析} {{
    println!("{{:#?}}",{想获取});
    {想获取}
}} else {{
    eprintln!("大帅比警告:解析变量失败 xxxxxxxx ");
    return;  // 提前退出程序
}};
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ if let else写法  外部返回值﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
// if let结合else，可以将变量的作用域扩展到if let块之外，这样就可以在块外部使用这个变量，从而减少了代码的嵌套层级
let {想获取} = if let Ok({想获取}) = {解析} {{
    println!("{{:#?}}",{想获取});
    {想获取}
}} else {{
    eprintln!("大帅比警告:解析变量失败 xxxxxxxx ");
    return;  // 提前退出程序
}};
println!("{{:#?}}",{想获取});

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ match 写法 内部返回值﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
// 解析的类型必须是 Result 类型   本质上是一种枚举类型
let obj = {解析};  # let obj: Result<fs::ReadDir, io::Error> = fs::read_dir(dir_path);

match {解析} {{
    Ok({想获取}) => {{
        println!("{{:#?}}",{想获取});
        {想获取};
    }},
    Err(e) => {{
        eprintln!("大帅比警告:解析变量失败 ---> {{}}", e);
    }}
}}

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ match 写法 外部返回值﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
// 解析的类型必须是 Result 类型   本质上是一种枚举类型
let obj = {解析};  # let obj: Result<fs::ReadDir, io::Error> = fs::read_dir(dir_path);

let mut {想获取} = match {解析} {{
    Ok({想获取}) => {{
        {想获取}
    }},
    Err(e) => {{
        eprintln!("大帅比警告:解析变量失败 ---> {{}}", e);
        return ();
    }}
}}
println!("{{:#?}}",{想获取});
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ 代码结束 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
"""
print(sentence)

r"""
let path = zi.path();
        println!("{{:?}}", path.display());
"""
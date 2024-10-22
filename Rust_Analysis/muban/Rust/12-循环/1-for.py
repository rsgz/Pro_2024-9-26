解析1 = "records"  # 父集合
解析2 = "zi"  # 子元素

开始=1
结束=100  # 包含结束

开始a = 'a'
结束a = 'z'  # 包含结束

s = f"""
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ for in 1..=5 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
for i in {开始}..={结束} {{
    println!("{{}}",i);
}}

for i in '{开始a}'..='{结束a}' {{
    println!("{{}}",i);
}}

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ for in 写法﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
for {解析2} in {解析1}{{
    {解析2}
}}

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ for iter() 写法﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
fn greet_world() {{
    for {解析2} in {解析1}.iter() {{
        println!("{{}}", &{解析2});
    }}
}}

fn main() {{
    greet_world();
}}

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ for in .into_iter().enumerate()写法﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
for (i,{解析2}) in {解析1}.into_iter().enumerate(){{
    if i==0{{
        println!(">>>>>> {解析2} ---> \\n{{:#?}}",{解析2});
        println!(">>>>>> {解析2} ---> \\n{{:#?}}",std::any::type_name_of_val(&{解析2}));
        
    }}

}}
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ 代码结束 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
"""
print(s)
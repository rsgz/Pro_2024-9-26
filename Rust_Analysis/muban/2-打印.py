obj = "vvv"  # 请输入 打印对象叫啥名字

sentence = f"""\
print!("{{:?}}",{obj});
print!("{{:#?}}",{obj});
println!("{{:?}}",{obj});
println!("{{:#?}}",{obj});
dbg!({obj});

if i%10000==0 {{
    println!("{{:?}}-->{{:?}}", i,url);
}}
"""
print(sentence)
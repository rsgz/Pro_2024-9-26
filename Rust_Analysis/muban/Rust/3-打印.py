obj = "fields"  #

sentence = f'''\
print!("{{:?}}",{obj});
print!("{{:#?}}",{obj});
println!("{{:?}}",{obj});
println!("{{:#?}}",{obj});

println!(">>>>>> {obj} ---> \\n{{:#?}}",{obj});

dbg!({obj});

// 打印频率
if i%10000==0 {{
    println!("{{:?}}-->{{:?}}", i,url);
}}
'''
print(sentence)
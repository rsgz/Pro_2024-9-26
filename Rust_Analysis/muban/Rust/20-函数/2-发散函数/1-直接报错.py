sentence = f'''\
fn dead_end() -> ! {{
  panic!("你已经到了穷途末路，崩溃吧！");
}}

'''
print(sentence)
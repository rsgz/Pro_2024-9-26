sentence = f'''\
let tup: (i32, f64, u8) = (500, 6.4, 1);

let tup = (500, 6.4, 1);
let (x, y, z) = tup;


'''
print(sentence)
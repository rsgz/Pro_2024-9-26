r'''
就我看到的 io::Result 写法有很多：
std::io::Result<()>

'''



s = f"""
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ std::io::Result<()> 写法﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
use std::fs::File;

fn read_file() -> std::io::Result<()> {{
    let f = File::open("hello.txt");

    let mut f = match f {{
        Ok(file) => file,
        Err(e) => {{
            eprintln!("Failed to open file: {{}}", e);
            return Err(e);
        }}
    }};

    // ... 使用文件对象 f ...
    Ok(())
}}
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ std::io::Result<()> 写法﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
"""

print(s)
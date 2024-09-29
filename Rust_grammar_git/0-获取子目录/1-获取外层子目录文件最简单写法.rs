use std::fs;
use std::io;

fn main() -> io::Result<()> {
    // let dir_path: &str = r"C:\Users\Administrator\Desktop\data\err"; // 注意路径分隔符需要双斜杠
    let dir_path: &str = r"\\PC-202407311638\share"; // 注意路径分隔符需要双斜杠
    for entry in fs::read_dir(dir_path)? { // 正确地遍历 dirset
        println!("{:?}", entry?.path().display());
    }
    Ok(())
}

/*
"\\\\PC-202407311638\\share\\0"
"\\\\PC-202407311638\\share\\00"     
"\\\\PC-202407311638\\share\\011.txt"
"\\\\PC-202407311638\\share\\斌"  


上面是获取子目录的最简单的写法
但是自能获取到 最外层的子目录
? 只能用在  -> io::Result<()>  和 Ok(())  一起出现的地方
*/
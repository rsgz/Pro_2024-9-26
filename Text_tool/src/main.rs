// use std::fs::File;
// use std::path::Path;
// use std::io::{self, BufRead, BufReader};
use std::fs;
use std::io;

// 调用这个函数 直接可以获取 文本文件里面  所有行数据
/*
let file_path = r"C:\Users\Administrator\Desktop\新技术.txt";
let mut urls = match get_lines(file_path) {
    Ok(urls) => urls,
    Err(e) => {
        eprintln!("打开文件失败: {}", e);
        // return Err(e);
        Vec::new()
    }
};

dbg!(urls);
*/

/*
pub fn get_lines<P>(filename: P) -> io::Result<Vec<String>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    let reader = BufReader::new(file);

    let mut lines = Vec::new();
    for line in reader.lines() {
        let line = line?;
        // 可以选择在这里添加对网址格式的验证
        lines.push(line);
    }

    Ok(lines)
}

*/


// fn main()-> io::Result<()>{
//     let file_path = r"C:\Users\Administrator\Desktop\data\err\rust_url_err_32568.txt";
//     let mut urls = match get_lines(file_path) {
//         Ok(urls) => urls,
//         Err(e) => {
//             eprintln!("打开文件失败: {}", e);
//             // return Err(e);
//             Vec::new()
//         }
//     };

//     // dbg!(urls);

//     let dir_path: &str = r"C:\Users\Administrator\Desktop\data\err";
//     // let dir_set: fs::ReadDir = fs::read_dir(dir_path).unwrap();
//     let dir_set: fs::ReadDir = fs::read_dir(dir_path)?;
//     // dbg!(dir_set);
//     // for r in dir_path{
//     //     let m = r.path().display();
//     //     println!("{m}");
//     // }
//     for entry in dir_set{
//         match entry {
//             Ok(entry) => {
//                 // 获取条目的路径
//                 let path = entry.path();
//                 // 打印路径
//                 println!("Entry: {:?}", path.display());
//             },
//             Err(e) => {
//                 // 如果读取条目时出错，打印错误信息
//                 eprintln!("Failed to read entry: {}", e);
//             }
//         }
//     }
//     Ok(())

// }


// fn main() -> io::Result<()> {
//     let dir_path: &str = r"C:\Users\Administrator\Desktop\data\err"; // 注意路径分隔符需要双斜杠
//     let dirset: fs::ReadDir = fs::read_dir(dir_path)?;
//     //dbg!(dirset);
//     for entry in dirset { // 正确地遍历 dirset
//         // let entry: fs::DirEntry = entry?; // 处理 Result，可能会出现错误
//         // let path: std::path::PathBuf = entry.path();
//         // entry?.path()
//         // 打印出路径
//         println!("{:?}", entry?.path().display());
//     }
//     Ok(())
// }
fn main() -> io::Result<()> {
    // let dir_path: &str = r"C:\Users\Administrator\Desktop\data\err"; // 注意路径分隔符需要双斜杠
    let dir_path: &str = r"\\PC-202407311638\share"; // 注意路径分隔符需要双斜杠
    // if let = fs::read_dir(dir_path);
    for entry in fs::read_dir(dir_path)? { // 正确地遍历 dirset
        println!("{:?}", entry?.path().display());
    }
    Ok(())
}
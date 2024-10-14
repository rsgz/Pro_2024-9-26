use std::error::Error;

use std::fs::File;
use std::io::BufReader;
use csv::ReaderBuilder;

// 写数据
use std::fs::OpenOptions;
use std::io::Write;

/*
[dependencies]
csv = "1.1"
*/

fn main() -> Result<(), Box<dyn Error>> {
    let csv_path = r"E:\爬取结果\3-商品\2024-10-04\1-连衣裙\37\https___www_pixiefaire_com_collections_crabapples_products_flutter-sleeve-dress-18.csv";

    let file_path = r"C:\Users\Administrator\Desktop\links.txt"; // 保存的文件路径
    let mut file_link = OpenOptions::new()
        .create(true)
        .append(true)
        .open(file_path)
        .expect("无法创建文本文件");


    // 创建一个BufReader来包装文件，这样我们可以使用csv::Reader
    let file = File::open(csv_path)?; // 替换为你的 CSV 文件路径
    let reader = BufReader::new(file);

    // 创建 CSV 读取器
    let mut rdr = ReaderBuilder::new()
        .has_headers(true) // 假设你的 CSV 文件包含头部
        .from_reader(reader);

    // 获取 "Image Src" 列的索引
    let image_src_index = rdr.headers()?.iter()
        .position(|h| h == "Image Src")
        .ok_or("Image Src column not found in CSV")?;

    // 遍历每一行并打印 "Image Src" 列的值
    for result in rdr.records() {
        let record = result?;
        if let Some(image_src) = record.get(image_src_index) {
            if !image_src.is_empty() {
                println!("{}", image_src);
                writeln!(file_link, "{}", image_src).expect("不能将链接写入到文本文件");
            }
        }
    }

    Ok(())
}

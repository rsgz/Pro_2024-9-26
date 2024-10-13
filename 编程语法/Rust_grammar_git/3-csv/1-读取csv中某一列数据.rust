use std::error::Error;
use std::fs::File;
use std::io::BufReader;
use csv::ReaderBuilder;

/*
[dependencies]
csv = "1.1"
*/

fn main() -> Result<(), Box<dyn Error>> {
    let csv_path = r"E:\爬取结果\3-商品\2024-10-04\1-连衣裙\36\https___www_nooteboomtextiles_com_collections_application-dresses_fR%5Bnamed_tags_en__Collection%5D%5B0%5D=Fashion%20Fabrics.csv";
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
            println!("{}", image_src);
        }
    }

    Ok(())
}

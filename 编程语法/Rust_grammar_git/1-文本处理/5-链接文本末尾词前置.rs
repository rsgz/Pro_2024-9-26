#![allow(dead_code)]
#![allow(unused_variables)]
#![allow(unused_imports)]

// use std::collections::HashSet;
// 读数据
use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::iter::Enumerate;
use std::path::Path;
// 写数据
use std::fs::OpenOptions;
use std::io::Write;
use urlencoding::decode;  // 解码
use rust_translate::{translate, translate_to_english, translate_from_english};

/*
[dependencies]
urlencoding = "2.1.3"
rust-translate = "0.1.3"
tokio = { version = "1.0", features = ["full"] }
*/


fn read_lines_from_file<P>(filename: P) -> io::Result<Vec<String>>
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

fn extract_last_part(url: &str) -> Option<String> {
    let mut parts = url.split('/');
    let last_part = parts.next_back()?;
    Some(last_part.to_string())
}

#[tokio::main]
async fn main() {
    // let record = "https://chatglm.cn/main/alltoolsdetail?lang=zh";
    let p=Path::new(r"C:\Users\Administrator\Desktop\rust_url3.txt");
    let mut urls_save = Vec::new();
    match read_lines_from_file(p) {
        Ok(urls) => {
            for (i, url) in urls.into_iter().enumerate() {
                let url_parts: Vec<&str> = url.split('/').collect();
                let last_part: &&str = url_parts.last().unwrap_or(&""); // 安全地获取最后一个部分
                let mut end: String = last_part.to_string();

                if end.is_empty() {
                    if url_parts.len() >= 2 {
                        end = url_parts[url_parts.len() - 2].to_string(); // 处理末尾是 '/' 的情况
                    }
                }
                let s: &str = end.as_str();

                let end2: String = s.replace("-", " ").replace("_", " ").replace("?", " ").replace("=", " ");
                let s2: &str = end2.as_str();
                let s2: std::borrow::Cow<'_, str> = decode(s2).expect("UTF-8 decoding failed");

                if i % 10000 == 0 {
                    // println!("{:?}-->{:?}", decoded_end, url);
                    println!("{:?}-->{:?}", s2, url);
                }

                /*由于自动翻译的时间太慢了 需要等待很久  就取消了 还是谷歌在线翻译快多了 */

                // urls_save.push(decoded_end + ":" + url.as_str());
                // let zh_text = translate_from_english(s2.as_ref(), "zh").await.unwrap();
                // println!("Translated to zh: {}", zh_text);

                // let translator = Translator::new("en", "zh");  // 创建英语到西班牙语的翻译器
                // let translated_text = translator.translate(s2.into_owned());  // 将英文文本翻译为西珙牙文
                // println!("{}", translated_text);  // 输出翻译结果

                urls_save.push(s2.into_owned() + ":" + url.as_str());
                // urls_save.push(zh_text + ":" + url.as_str());
            }
        },
        Err(e) => {
            eprintln!("打开文件失败: {}", e);
        }
    }
    
    let file_path = r"C:\Users\Administrator\Desktop\rust_url4.txt"; // 保存的文件路径
    let mut file = OpenOptions::new()
        .create(true)
        .append(true)
        .open(file_path)
        .expect("无法创建文本文件");
    for a in urls_save{
        writeln!(file, "{}", a).expect("不能将链接写入到文本文件");    
    }
    println!("所有链接写入成功!!!");
}
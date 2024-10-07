use reqwest;
// use reqwest::RedirectPolicy;
// use std::io::stdin;
// use regex::Regex;
use scraper::{Html, Selector};
use std::fs::OpenOptions;
// use std::io::Write;

use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::path::Path;
// use url::Url;
use chrono::Local;
use std::io::{stdin, Write,stdout};

// 输入 字符串
// let name:String=input(String::from("请输入一些话:"));
pub fn input(some_string:String) -> String {
    print!("{}",some_string);
    stdout().flush().unwrap(); 
    let mut input = String::new();
    stdin().read_line(&mut input).expect("读取不到用户输入的数据!");
    input.trim().to_string()
  }

fn end(){
    println!("你可以-->按任意键 关闭...");
    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();
}

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



#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = reqwest::Client::builder()
        .timeout(std::time::Duration::from_secs(10))
        .proxy(reqwest::Proxy::https("http://127.0.0.1:7890")?)
        //.redirect(RedirectPolicy::limited(10))
        .build()?;

    let input:String=input(String::from("请输入从多少开始:"));
    let n_start = input.parse().expect("Not a number!");

    let file_path = "C:\\Users\\Administrator\\Desktop\\遍历网址.txt";
    match read_lines_from_file(file_path) {
        Ok(urls) => {
            println!("读取到的网址列表：");
            // for url in urls {
            for (index, url) in urls.into_iter().enumerate() {
                let fmt = "%Y年%m月%d日 %H:%M:%S";
                let now = Local::now().format(fmt);
                println!("{} -- {} --> {}", now,index+1,url);

                // if index<12789{
                
                // let n_start = 14485;
                if index<n_start{
                    continue;
                }

                
                // println!("{}-->{}", index+1,url);

                // let url = "https://ipv4.icanhazip.com/";
                // let url = "https://www.ipchicken.com/";
                // let url = "http://survivalarcherysystems.myshopify.com";
                let base_url=&url;

                match client.get(base_url)
                    .header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
                    .send().await{
                        Ok(response)=>{
                            // 获取最终URL的域名
                            let final_url = response.url().clone();
                            let scheme = final_url.scheme(); // 获取协议，如 "http" 或 "https"
                            let domain = final_url.host_str().expect("No domain found").to_string();
                            let full_domain = format!("{}://{}", scheme, domain); // 将协议和域名组合
                            
                            // println!("{}-->{}", index+1, domain);
                            // println!("{}-->{}", index+1, domain);
                            // if index%500==0 {
                            //     println!("{}-->{}", index+1, domain);
                            // }
                            

                            let body = response.text().await?;
                            // println!("Response body: {}", body);  // Response body: 38.94.108.7  美国IP 代理成功

                            let fragment = Html::parse_document(&body);
                            let selector = Selector::parse("a").unwrap();

                            // let file_path = r"C:\Users\Administrator\Desktop\rust_url15000.txt"; // 输出文件路径
                            let file_path = format!(r"C:\Users\Administrator\Desktop\rust_url{}.txt", n_start);
                            // let file_path = r"C:\Users\Administrator\Desktop\rust_url15000.txt"; // 输出文件路径
                            // let file_path = "rust_url_results.txt"; // 输出文件路径
                            let mut file = OpenOptions::new()
                                .create(true)
                                .append(true)
                                .open(file_path)
                                .expect("无法创建文本文件");

                            for element in fragment.select(&selector) {
                                if let Some(href) = element.value().attr("href") {
                                    if !href.starts_with("javascript:") && !href.contains("cdn.") {
                                        let full_url = if href.starts_with("http://") || href.starts_with("https://") {
                                            href.to_string()
                                        } else {
                                            // 如果是相对路径，则与基础URL拼接
                                            if href.starts_with('/') {
                                                format!("{}{}", full_domain, href)
                                            } else {
                                                format!("{}/{}", full_domain, href)
                                            }
                                        };
                                        // println!("{}", full_url);
                                        // println!("--> {}", full_url);
                                        writeln!(file, "{}", full_url.as_str()).expect("不能将链接写入到文本文件");
                                    }
                                }
                            }
                        },Err(e)=>{
                            eprintln!("无法访问网址 {}: {}", base_url, e);
                            let file_path = format!(r"C:\Users\Administrator\Desktop\rust_url_err_{}.txt", n_start);
                            // let file_path = r"C:\Users\Administrator\Desktop\rust_url_err_15000.txt"; // 输出文件路径
                            // let file_path = "rust_url_results.txt"; // 输出文件路径
                            let mut file = OpenOptions::new()
                                .create(true)
                                .append(true)
                                .open(file_path)
                                .expect("无法创建文本文件");
                            writeln!(file, "{}", base_url).expect("不能将链接写入到文本文件");
                            continue;
                        }
                    };
            }
        },
        Err(e) => {
            eprintln!("读取文件时发生错误：{}", e);
        }
    }

    end();
    Ok(())
}
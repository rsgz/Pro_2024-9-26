#![allow(dead_code)]

mod common;
use reqwest::Response;
use common::txt::get_lines;
// use reqwest::Client;
use tokio::task;
use reqwest;
use scraper::{Html, Selector};
use std::fs::OpenOptions;
use std::io::Write;

// dbg!(urls);
// println!("{:?}",urls);

async fn extract_and_save_urls(response:Response, write_path:&str) -> Result<(), Box<dyn std::error::Error>> {
    // let response1 = response.clone();
    let final_url = response.url().clone();
    let scheme = final_url.scheme(); // 获取协议，如 "http" 或 "https"
    let domain = final_url.host_str().expect("No domain found").to_string();
    let full_domain = format!("{}://{}", scheme, domain); // 将协议和域名组合
    dbg!(&full_domain);
    println!("1");
    // println!(response.text());
    let body = match response.text().await {
        Ok(text) => {
            println!("{}", text);
            text
        },
        Err(e) => {
            eprintln!("读取响应文本错误: {}", e);
            String::from("0")
        },
    };

    // let body = response.text().await?;
    println!("1.1");
    let fragment = Html::parse_document(&body);
    println!("1.2");
    let selector = Selector::parse("a").unwrap();
    println!("1.3");
    println!("2");

    let mut file = OpenOptions::new()
        .create(true)
        .append(true)
        .open(write_path)
        .expect("无法创建文本文件");
    println!("3");
    for element in fragment.select(&selector) {
        println!("4");
        if let Some(href) = element.value().attr("href") {
            println!("5");
            if !href.starts_with("javascript:") && !href.contains("cdn.") {
                println!("6");
                let full_url = if href.starts_with("http://") || href.starts_with("https://") {
                    println!("7");
                    href.to_string()
                }
                else {
                    println!("8");
                    // 如果是相对路径，则与基础URL拼接
                    if href.starts_with('/') {
                        format!("{}{}", full_domain, href)
                    } else {
                        format!("{}/{}", full_domain, href)
                    }
                };
                println!("9");
                println!("{:?}",full_url.as_str());
                writeln!(file, "{}", full_url.as_str()).expect("不能将链接写入到文本文件");
            }
        }
    }

    Ok(())
}

#[tokio::main]
async fn main() {
    // 拿到了 所有链接
    let file_path = r"C:\Users\Administrator\Desktop\遍历网址.txt";
    let urls = match get_lines(file_path) {
        Ok(urls) => urls,
        Err(e) => {
            eprintln!("打开文件失败: {}", e);
            // return Err(e);
            Vec::new()
        }
    };

    // 创建 请求对象
    // let client = Client::new();
    let client = reqwest::Client::builder()
                .timeout(std::time::Duration::from_secs(10))
                .proxy(reqwest::Proxy::https("http://127.0.0.1:7890").unwrap())
                //.redirect(RedirectPolicy::limited(10))
                .build().unwrap();

    // 并发任务 都放里面
    let mut tasks = Vec::new();

    for (i,url) in urls.into_iter().enumerate() {
        let client = client.clone(); // Clone the client for each task.
        let url = url.to_string(); // Clone the URL for the move into the task.
        tasks.push(task::spawn(async move {
            match client.get(&url)
                    .header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
                    .send().await {
                Ok(response) => {
                    let write_path = r"C:\Users\Administrator\Desktop\rust_url_666.txt";
                    // extract_and_save_urls(response, write_path).await.expect("处理 链接失败");
                    if let Err(e) = extract_and_save_urls(response, write_path).await {
                        eprintln!("处理链接失败: {} 错误: {}", url, e);
                    };
                    // if let Ok(body) = response.text().await {
                    //     // println!("{}", body);
                    //     let first_ten_chars: String = body.chars().take(100).collect();
                    //     println!("{}", first_ten_chars);

                    // } else {
                    //     eprintln!("链接响应体读取失败: {}", url);
                    // }

                    if i%10000==0 {
                        println!("{:?}-->{:?}", i,url);
                    }


                }
                Err(e) => {
                    eprintln!("网址请求错误: {} 错误: {}", url, e);
                }
            }
        }));
    }

    // Wait for all tasks to complete.
    for task in tasks {
        let _ = task.await; // Ignore the result, errors are already logged.
    }
}
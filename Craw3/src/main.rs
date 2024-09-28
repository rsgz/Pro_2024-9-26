use reqwest;
// use reqwest::RedirectPolicy;
use std::io::stdin;
// use regex::Regex;
use scraper::{Html, Selector};
use std::fs::OpenOptions;
use std::io::Write;

use tokio::task;
use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::path::Path;
// use url::Url;
use futures::future::join_all;


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
async fn main()-> Result<(), Box<dyn std::error::Error>>{

    let mut client = reqwest::Client::builder()
        // ...（配置不变）
        .timeout(std::time::Duration::from_secs(10))
        .proxy(reqwest::Proxy::https("http://127.0.0.1:7890")?)
        //.redirect(RedirectPolicy::limited(10))
        .build()?;

    let file_path = "C:\\Users\\Administrator\\Desktop\\遍历网址.txt";
    let urls = read_lines_from_file(file_path).unwrap();

    let fetches = urls.into_iter().map(|url| async{
        let client2 = client.clone();
        client2.get(url)
        .header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
        .send().await
    });

    let responses = join_all(fetches).await;
    for (i,response) in responses.into_iter().enumerate() {
        if let Ok(response1) = response {
            // 处理每个响应
            // 获取最终URL的域名
            let final_url = response1.url().clone();
            let scheme = final_url.scheme(); // 获取协议，如 "http" 或 "https"
            let domain = final_url.host_str().expect("No domain found").to_string();
            let full_domain = format!("{}://{}", scheme, domain); // 将协议和域名组合
            
            println!("{}-->{}", i+1, domain);

            let body = response1.text().await?;
            // println!("Response body: {}", body);  // Response body: 38.94.108.7  美国IP 代理成功

            let fragment = Html::parse_document(&body);
            let selector = Selector::parse("a").unwrap();

            let file_path = r"C:\Users\Administrator\Desktop\rust_url22.txt"; // 输出文件路径
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

        }
    }


    // let mut tasks = Vec::new();

    // // for url in urls {
    // for (i,url) in urls.into_iter().enumerate() {
    //     let client = client.clone();
    //     tasks.push(task::spawn(async move {
    //         process_url(i, &url, client).await;
    //     }));
    // }

    // for task in tasks {
    //     task.await.unwrap();
    // }

    end();
    Ok(())
}

async fn process_url(index: usize, url: &str, client: reqwest::Client) -> Result<(), Box<dyn std::error::Error>> {
    // ...（处理单个URL的代码）
    match client.get(url)
    .header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
    .send().await{
        Ok(response)=>{
            // 获取最终URL的域名
            let final_url = response.url().clone();
            let scheme = final_url.scheme(); // 获取协议，如 "http" 或 "https"
            let domain = final_url.host_str().expect("No domain found").to_string();
            let full_domain = format!("{}://{}", scheme, domain); // 将协议和域名组合
            
            println!("{}-->{}", index+1, domain);
            // println!("{}-->{}", index+1, domain);
            // if index%500==0 {
            //     println!("{}-->{}", index+1, domain);
            // }
            

            let body = response.text().await?;
            // println!("Response body: {}", body);  // Response body: 38.94.108.7  美国IP 代理成功

            let fragment = Html::parse_document(&body);
            let selector = Selector::parse("a").unwrap();

            let file_path = r"C:\Users\Administrator\Desktop\rust_url22.txt"; // 输出文件路径
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
            eprintln!("无法访问网址 {}: {}", url, e);
            let file_path = r"C:\Users\Administrator\Desktop\rust_url_err22.txt"; // 输出文件路径
            // let file_path = "rust_url_results.txt"; // 输出文件路径
            let mut file = OpenOptions::new()
                .create(true)
                .append(true)
                .open(file_path)
                .expect("无法创建文本文件");
            writeln!(file, "{}", url).expect("不能将链接写入到文本文件");
            // continue;
        }
    };

    Ok(())
}

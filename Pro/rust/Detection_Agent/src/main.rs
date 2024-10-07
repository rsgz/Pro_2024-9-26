use reqwest;
use std::io::stdin;

/*
之前第一个版本 同步 reqwest = {version = "0.11", features = ["blocking"]} 
结论：
clash 系统代理开不开无所谓  全局一定要开
*/

fn end(){
    println!("你可以-->按任意键 关闭...");
    let mut input = String::new();
    stdin().read_line(&mut input).unwrap();
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client = reqwest::Client::builder()
        .timeout(std::time::Duration::from_secs(10))
        .proxy(reqwest::Proxy::https("http://127.0.0.1:7890")?)
        .build()?;

    let url = "https://uncle-mikes-bake-shoppe.myshopify.com";
    // let url = "https://www.ipchicken.com/";
    // let url = "http://survivalarcherysystems.myshopify.com";
    let response = client.get(url)
        .header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
        .send().await?;
    let body = response.text().await?;
    println!("Response body: {}", body);  // Response body: 38.94.108.7  美国IP 代理成功

    end();
    Ok(())
}
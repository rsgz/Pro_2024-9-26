use reqwest::Client;
use tokio::sync::Semaphore;
use std::num::NonZeroUsize;
use futures::stream::{self, StreamExt};

#[tokio::main]
async fn main() {
    let urls = vec![r"https://rweverydayessentials.myshopify.com",
r"http://planetbachelorette.myshopify.com",
r"https://florencescoveljewelry876-com.myshopify.com",
r"https://666c0d-2.myshopify.com",
r"https://weddink.myshopify.com",
r"https://demo-jdsmarketing.myshopify.com",
r"https://b09944-88.myshopify.com",
r"https://michellesmess.myshopify.com",
r"https://announce-it.myshopify.com",
r"https://sam-nail-supply.myshopify.com",
r"https://frenzy-flare.myshopify.com",
r"https://minty-tees.myshopify.com",
r"https://www-gspotzone-com.myshopify.com",
r"https://candy-wrapper-store.myshopify.com",
r"https://tbs-transfers.myshopify.com",
r"http://charm-fig.myshopify.com",
r"https://the-celebration-place.myshopify.com",
r"https://elliefont-styles.myshopify.com",
r"https://monogramsoffmadison-com.myshopify.com",
r"https://six-stories.myshopify.com",
r"https://neon-cowboys.myshopify.com",
r"https://littlebarnacles.myshopify.com",
r"https://yourmainevent.myshopify.com",
r"https://lisajaud13.myshopify.com",
r"https://something-new-bridal-box.myshopify.com",
r"https://ginger-squared.myshopify.com",
r"http://condom-usa.myshopify.com",
r"https://bachelorette-priveco.myshopify.com",
r"http://inslee-by-design.myshopify.com",
r"https://sugarbabyaprons.myshopify.com",
r"https://double-k-originals.myshopify.com",
r"https://end-of-the-lane.myshopify.com",
r"https://one-blushing-bride.myshopify.com",
r"https://downtown-darling-wholesale.myshopify.com",
r"https://flower-moxie.myshopify.com",
r"https://figurama-collectors-limited.myshopify.com",
r"https://ohjuliettestore.myshopify.com",
r"https://georgia-hardinge.myshopify.com",
r"https://the-obsessions-boutique.myshopify.com",
r"https://jelly-pop-shoes.myshopify.com",
r"https://scl-harborside.myshopify.com",
r"https://shopcarolineandcompany-com.myshopify.com",
r"https://adam-tucker.myshopify.com",
r"https://bill-blass.myshopify.com",
r"https://blondo-shop.myshopify.com",
r"https://femmeliberee-4547.myshopify.com",
r"https://shop-gottahavemypumps-com.myshopify.com",
r"http://tennessee-farrier-supply.myshopify.com",
r"https://sabah-us.myshopify.com",
r"https://yellow-box-footwear-shoes.myshopify.com",
r"https://prota-fiori.myshopify.com",
r"https://healthyfeet-store.myshopify.com",
r"https://honest-johns-trading-post.myshopify.com",
r"https://nanostudio-official.myshopify.com",
r"https://theme-tests-fastsimon.myshopify.com",
r"https://romika-usa.myshopify.com",
r"https://happy-feet-plus.myshopify.com",
r"https://mast-shoes.myshopify.com",
r"https://sandpad-store-demo.myshopify.com",
r"https://caverleyshoes-com.myshopify.com",
r"https://zou-xou-shoes.myshopify.com",
r"https://bt-beloria-infinity.myshopify.com",
r"https://sabah-4.myshopify.com",
r"https://malone-souliers.myshopify.com",
r"https://mave-and-chez.myshopify.com",
r"https://bakers-shoes-store.myshopify.com",
r"https://flyshoesleather.myshopify.com",
r"https://covid19-dev.myshopify.com",
r"https://hobson-shoes.myshopify.com",
r"https://webberry-my.myshopify.com",
r"https://vintage-redefined.myshopify.com",
r"https://seliga-shoes.myshopify.com",
r"https://sole-shoes-new-zealand.myshopify.com",
r"https://boundless-theme-apparel.myshopify.com",
r"https://besty-fisher.myshopify.com",
r"https://staud-dev-test.myshopify.com",
r"https://1a1cae-3.myshopify.com",
r"https://hush-puppies-philippines.myshopify.com",
r"https://minnies-treasure-chest.myshopify.com",
r"https://bvstore-26045.myshopify.com",
r"https://bata-pakistan.myshopify.com",
r"https://little-fox-fashions.myshopify.com",
r"https://shoeplanet-pk.myshopify.com",
r"https://hushpuppiespk.myshopify.com",
r"https://mafalda-shoes.myshopify.com",
r"https://e9ff52-3.myshopify.com",
r"https://the-blue-body-brazil.myshopify.com",
r"https://friday-night-dolls-boutique.myshopify.com",
r"https://litlookz-studio.myshopify.com",
r"https://thatgirl-studios.myshopify.com",
r"https://89cc07-2.myshopify.com",
r"https://257750-2.myshopify.com",
r"https://beeglee-in.myshopify.com",
r"https://beginningboutique-us.myshopify.com",
r"https://violate-the-dress-code.myshopify.com",
r"https://3466f3-a5.myshopify.com",
r"https://vested-by-monet.myshopify.com",
r"https://pixies-lounge-online.myshopify.com",
r"https://misters-choices.myshopify.com",
r"https://seagypsy-couture.myshopify.com",]; // 示例 URL 列表

    let client = Client::new();
    let concurrency_limit = NonZeroUsize::new(100).unwrap(); // 设置并发限制
    let semaphore = Semaphore::new(concurrency_limit.into());

    let mut stream = stream::iter(urls.into_iter().enumerate().map(|(i, url)| {
        let client = client.clone();
        let semaphore = semaphore.clone();
        let url = url.to_string();

        tokio::spawn(async move {
            let permit = semaphore.acquire().await.unwrap(); // 获取信号量许可
            let response = client.get(&url)
                .header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
                .send()
                .await;
            drop(permit); // 释放信号量许可
            (i, response)
        })
    }));

    while let Some(task) = stream.next().await {
        match task {
            Ok((i, result)) => {
                match result {
                    Ok(response) => {
                        // 处理响应
                        println!("URL {} fetched successfully!", i);
                    },
                    Err(e) => {
                        // 处理错误
                        eprintln!("Failed to fetch URL {}: {}", i, e);
                    }
                }
            },
            Err(e) => {
                // 处理任务 panic 的情况
                eprintln!("Task panicked: {:?}", e);
            }
        }
    }
}

var Bzhan_url = "https://www.bilibili.com/video";

if (window.location.href.startsWith(Bzhan_url)) {
    (async ()=>{
        var fengmian=async ()=>{
            console.log("rsgz_Bzhan.js 被加载");
            // 视频封面
            var img_url1 = document.querySelectorAll("div.video-capture-img picture img")[0].getAttribute('src');
            console.log("视频封面1:","https:"+img_url1)
            var img_url2 = document.querySelectorAll("img#wxwork-share-pic")[0].getAttribute('src');
            console.log("视频封面2:","https:"+img_url2)

            //
        }

        await delay(1500);
        await fengmian();
    })();

}




// if (window.location.href.startsWith(Bzhan_url)) {
//     (async () => {
//         console.log("rsgz_Bzhan.js 被加载");
//
//         // 定义获取封面图片并输出的异步函数
//         async function fengmian() {
//             await delay(1500);
//
//             // 视频封面
//             const img = document.querySelectorAll('div.video-capture-img picture img')[0];
//             let img_url = img.getAttribute('src');
//             img_url = "https:" + img_url;
//             console.log("视频封面:", img_url);
//         }
//
//         // 调用异步函数
//         await fengmian();
//     })();
// }
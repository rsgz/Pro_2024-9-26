var pinduoduo_url = "https://mobile.yangkeduo.com/"


$(function (){
    if (window.location.href.startsWith(pinduoduo_url)){
        console.log("rsgz_pinduoduo.js 被加载");
        chrome.runtime.onMessage.addListener( async function (request, sender, sendResponse){
            if (window.location.href.startsWith(pinduoduo_url)){
                // -------------- 拼多多商品图 -------------
                if(request.pinduoduo_2=="pinduoduo_2"){
                    await delay(200);
                    img_set = document.querySelectorAll("div[aria-label^=\"商品缩略\"] img");
                    src_list = Array.from(img_set).map((img)=>{
                        img_src = img.getAttribute("data-src");
                        return img_src.split('?imageView')[0];
                    });
                    copy_str = src_list.join(',');
                    //await navigator.clipboard.writeText(copy_str);
                    console.log('复制:', JSON.stringify(src_list));

                    chrome.runtime.sendMessage({copy:"copy",imgs:src_list})
                }
            }

        });
    }
});
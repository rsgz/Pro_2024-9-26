var demo = "https://cccccccc.shopee.cn/portal/marketing"


$(function (){
    if (window.location.href.startsWith(demo)){
        console.log("rsgz_shopee.js 被加载");
        chrome.runtime.onMessage.addListener( async function (request, sender, sendResponse){
            if (window.location.href.startsWith(demo)){
                // -------------- 广告搜索关键词 -------------
                if(request.xiapi2=="xiapi2"){
                    await delay(200);
                }
            }

            if (window.location.href.startsWith(demo)){}
            if (window.location.href.startsWith(demo)){}
            if (window.location.href.startsWith(demo)){}
        });
    }
});
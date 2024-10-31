var a1688_url = "https://detail.1688.com/"


$(function (){
    if (window.location.href.startsWith(a1688_url)){
        console.log("rsgz_1688.js 被加载");
        chrome.runtime.onMessage.addListener( async function (request, sender, sendResponse){
            if (window.location.href.startsWith(a1688_url)){
                // -------------- 广告搜索关键词 -------------
                if(request.a1688_rsgz_2=="a1688_rsgz_2"){
                    await delay(200);
                    // 给图片编号
                    var sku_names = document.querySelectorAll("div.sku-item-name");
                    for (var i=0;i<sku_names.length;i++) {
                        sku_name = sku_names[i];
                        sku_name.innerText = (i+1).toString()+"-->"+sku_name.innerText;
                    }

                    // 批量获取链接
                    var sku_imgs = document.querySelectorAll("div.sku-item-image");
                    urls=[];
                    for(let img of sku_imgs){
                        style = img.getAttribute("style");
                        urlRegex = /https.*\"/g;
                        url = style.match(urlRegex)[0];
                        url=url.slice(0,-1)
                        urls.push(url);
                    }
                    console.log(JSON.stringify(urls));

                }

                if(request.a1688_rsgz_3=="a1688_rsgz_3"){
                    await delay(200);
                    // 给图片编号
                    var sku_names = document.querySelectorAll("div.prop-name");
                    for (var i=0;i<sku_names.length;i++) {
                        sku_name = sku_names[i];
                        sku_name.innerText = (i+1).toString()+"-->"+sku_name.innerText;
                    }

                    // 批量获取链接
                    var sku_imgs = document.querySelectorAll("div.prop-img");
                    urls=[]
                    for(let img of sku_imgs){
                        style = img.getAttribute("style");
                        urlRegex = /https.*\"/g;
                        url = style.match(urlRegex)[0];
                        url=url.slice(0,-1)
                        urls.push(url);
                    }
                    console.log(JSON.stringify(urls));
                }
            }

            if (window.location.href.startsWith(demo)){}
            if (window.location.href.startsWith(demo)){}
            if (window.location.href.startsWith(demo)){}
        });
    }
});
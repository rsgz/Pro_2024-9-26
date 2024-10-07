var a_douyin_url = "https://www.douyin.com/"

// ================== 抖音优化 ==================
if (window.location.href.startsWith(a_douyin_url)){
    console.log("进入rsgz_douyin.js");
    try{
        // <span id="state_4">161900</span>
        setTimeout(()=>{
            // ==========插入按钮==========
            // var divElement = document.querySelectorAll('div[data-state="normal"][class~="danmakuContainer"]')[0].parentNode
            // 上面
            var divElement = document.querySelectorAll('div[data-click="doubleClick"]')[0];
            var divElement2 = document.querySelectorAll('div[data-state="normal"][class~="danmakuContainer"]')[0].parentNode
            // ========downloadBtn 按钮========== 在这个div里面插入一个下载按钮
            var downloadBtn = document.createElement('button');
            downloadBtn.innerText = "下载视频";

            // 设置按钮样式，可以根据需要修改
            downloadBtn.id="douyin_down_id";
            downloadBtn.style.padding = "5px 10px";
            downloadBtn.style.margin = "10px";
            downloadBtn.style.backgroundColor = "blue";
            downloadBtn.style.color = "white";
            downloadBtn.style.border = "none";
            downloadBtn.style.float="right";
            // ========插入按钮==========

            if(window.location.href.startsWith("https://www.douyin.com/user")){
                console.log("插入下面按钮");
                divElement2.appendChild(downloadBtn);
            } else if(window.location.href.startsWith(a_douyin_url)){
                console.log("插入上面按钮");
                divElement.appendChild(downloadBtn);
            }

            console.log("=============优化 抖音 下载=============");
            console.log("=============已经添加 下载按钮!!!=============");

            console.log("=============返回抖音下载链接!!!=============");
            // 点击按钮时发送消息给background.js
            document.getElementById("douyin_down_id").addEventListener("click", function() {
                var video = document.querySelectorAll('xg-video-container.xg-video-container')[0];
                var source = video.querySelectorAll("video source")[0];
                var videoLink = 'https:'+source.getAttribute('src');  // 你要下载的视频链接
                console.log("抖音视频:",videoLink);

                chrome.runtime.sendMessage({
                    message: "downloadVideo",
                    videoLink: videoLink
                });
            });

        },1500)

    }catch (e) {
        // ...
    }
}

$(function (){
    if (window.location.href.startsWith(a_douyin_url)){
        //console.log("rsgz_shopee.js 被加载");
        chrome.runtime.onMessage.addListener( async function (request, sender, sendResponse){
            if (window.location.href.startsWith(a_douyin_url)){
                // -------------- 获取抖音视频链接 -------------
                if(request.douyin_rsgz_2=="douyin_rsgz_2"){
                    await delay(200);
                    var video = document.querySelectorAll('xg-video-container.xg-video-container')[0];
                    var source = video.querySelectorAll("video source")[0];
                    var videoLink = 'https:'+source.getAttribute('src');  // 你要下载的视频链接
                    console.log("抖音视频:",videoLink);
                }
            }


        });
    }
});
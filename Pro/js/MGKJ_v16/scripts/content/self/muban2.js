var demo = "http://www.360doc.com";

$(function (){
    if (window.location.href.startsWith(demo)){
        // console.log("main_360doc.js 被加载")
        chrome.runtime.onMessage.addListener( async function (request, sender, sendResponse){
            // 填写预设样式和条件
            if(request.instruct=="xxxxxxx"){
                console.log("1")
                $('span#treelist_75_span')[0].click()
                Array.from(document.querySelectorAll('a')).filter(v => v.textContent.includes('原创收益'))[0].click()
                click_html()
                await delay(500);
            }

            // --------------xxx--------------
            // --------------xxx--------------
            // --------------xxx--------------
            // --------------xxx--------------
        });
    }
});


// 原创
async function yuanchuang(){
    $('input#yctg')[0].click()
    await delay(500)
    $('a.rbtn_confirm_s.font12')[0].click()
}




/*
1 标准 runtime onmessage
function handleMessage(request, sender, sendResponse) {
    const instruct = request.instruct
    if(instruct=="add"){

    }
    // Send a response back if needed
    sendResponse('Response from background script');
}

chrome.runtime.onMessage.addListener(handleMessage);

2 ======DOMContentLoaded 和 load ======
// 监听DOMContentLoaded事件
document.addEventListener('DOMContentLoaded', function () {
  console.log('DOMContentLoaded事件触发：DOM结构已经加载完成，但样式表、图片等资源可能还在加载中...');
});

// 监听load事件
window.addEventListener('load', function () {
  console.log('load事件触发：整个页面及所有资源（包括样式表、图片等）已完全加载完毕！');
});
DOMContentLoaded: 当页面的 DOM 结构构建完成，但不包括样式表、图像等外部资源的加载完成的时候就出发了
load: 整个页面的所有资源（包括样式表、图像等外部资源）加载完成后触发。也就是说，当整个页面及其所有关联资源（如图片、样式表等）都加载完成后，load事件触发
*/
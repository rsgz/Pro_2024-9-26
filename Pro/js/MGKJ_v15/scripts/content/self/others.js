$(()=>{
// 任何网站都执行
chrome.runtime.onMessage.addListener(async function(request, sender, sendResponse) {
    // 任意网页修改
    if(request.others_2024_8_27_renyi_xiugai==="others_2024_8_27_renyi_xiugai"){
        console.log("request.others_2024_8_27_renyi_xiugai");
        (async ()=>{
            console.log('执行 others.js');
            console.log('当前网页内容可随意修改!');
            document.body.contentEditable='true';
        })();
    }
    
    // 禁止修改
    if(request.others_2024_8_27_buke_xiugai==="others_2024_8_27_buke_xiugai"){
        console.log("request.others_2024_8_27_buke_xiugai");
        (async ()=>{
            console.log('执行 others.js');
            console.log('网页内容不可修改!');
            document.body.contentEditable='false';
        })();
    }

    // 更换背景
    if(request.others_2024_8_27_genggai_beijing_tu==="others_2024_8_27_genggai_beijing_tu"){
        console.log("request.others_2024_8_27_genggai_beijing_tu");
        (async ()=>{
            console.log('执行 others.js');
            console.log('更改网页背景图!');

            $('*').each(function() {
                $(this).css('background-color', 'transparent');
            });

            // 随机图片
            // let n_index=Math.ceil(Math.random()*20); // 1--10 随机整数
            // let n_index=Math.ceil(Math.random()*20); // 1--10 随机整数
            const imgUrl = chrome.runtime.getURL(`images/bg_body/${n_index}.jpg`);
            console.log(imgUrl);

            // $('body:eq(0)').css('background-image', `url(images/bg_body/${n_index}.jpg)`);  // GET https://www.remove.bg/images/bg_body/2.jpg 404 (Not Found)
            $('body:eq(0)').css('background-image', `url(${imgUrl})`);  // chrome-extension://adgoedbokpojecgmcepihcjbghlehgnf/images/bg_body/2.jpg

            // others.js:30 Uncaught (in promise) TypeError: chrome.extension.getURL is not a function   content.js不能使用这个接口？？
            // const imgUrl = chrome.extension.getURL(`../../../images/bg_body/${n_index}.jpg`);
            
            
        })();
    }

    // 复制文本
    if(request.ohter_fuzhi_wenben==="ohter_fuzhi_wenben"){
        console.log("request.ohter_fuzhi_wenben");
        let s=`var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);

// 复制文本
function copyTextToClipboard(text) {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.select();
    try {
        const successful = document.execCommand('copy');
        const msg = successful ? 'successful' : 'unsuccessful';
        console.log('Copying text command was ' + msg);
    } catch (err) {
        console.error('Oops, unable to copy', err);
    }
    document.body.removeChild(textArea);
}`
            console.log(s);
            copyTextToClipboard(s);
    }
        


})
});
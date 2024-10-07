var doc360_url = "http://www.360doc.com";



$(function (){
    if (window.location.href.startsWith(doc360_url)){
        console.log("main_360doc.js 被加载")
        chrome.runtime.onMessage.addListener( async function (request, sender, sendResponse){
            // 进入草稿
            // if(request.to_360doc=="to_360doc"){
            //     // window.location.href = "http://www.360doc.com/edit/writeartnew.aspx";
            //     window.open("http://www.360doc.com/edit/writeartnew.aspx")
            // }

            // 填写预设样式和条件
            if(request.instruct=="add"){
                console.log("1")
                click_html()
                await delay(500);
                write_code(title=request.title,content=request.content);
                await delay(900);
                click_html()
                await delay(500);
                await yuanchuang()
            }

            // 点击 草稿箱
            if(request.caogao=="caogao"){
                $('span#treelist_75_span')[0].click()
            }

            if(request.shouyi=="shouyi"){
                Array.from(document.querySelectorAll('a')).filter(v => v.textContent.includes('原创收益'))[0].click()
            }

        });

    }
});




// 点击右上角的html
function  click_html(){
    var element = document.querySelector('span.toolbars_btn.b18.b18s.ui_c');
    if (element) {
        element.click()
    }else{
        console.log("没有找到元素")
    }
}

// 输入样式
function write_code(title, content){
    code = `<blockquote class="quote360doc" style="background-color:#D7EBC5;color:#D15656;font-size: 16px;"><span style="font-size: 16px;">表白：黑白圣堂血天使，天剑鬼刀阿修罗。&nbsp;<br>讲解对象：</span><span style="font-size: 16px; color: rgb(0, 0, 0);"><strong>/${title}</strong></span><span style="font-size: 16px;"><br>作者：融水公子 rsgz<br><span style="color: rgb(209, 86, 86);background-color: rgb(215, 235, 197);">===<br><span style="font-size: 16px;"><br>${content}</span></span></span><p><br></p><span style="font-size: 16px;"><span style="color: rgb(209, 86, 86);background-color: rgb(215, 235, 197);"><span style="font-size: 16px;">===</span>&nbsp;<pre style="font-size: 18px;white-space: pre; margin-top: 0px; margin-bottom: 0px; padding: 12px; font-family: Consolas, &quot;Andale Mono WT&quot;, &quot;Andale Mono&quot;, &quot;Lucida Console&quot;, &quot;Lucida Sans Typewriter&quot;, &quot;DejaVu Sans Mono&quot;, &quot;Bitstream Vera Sans Mono&quot;, &quot;Liberation Mono&quot;, &quot;Nimbus Mono L&quot;, Monaco, &quot;Courier New&quot;, Courier, monospace; color: rgb(255, 112, 159); box-sizing: border-box; font-size: 16px; line-height: 1.5; overflow: auto; background-color: rgb(35, 36, 31);">公众号：不浪仙人</pre><span style="background-color: rgb(215, 235, 197); color: rgb(209, 86, 86); font-size: 16px;">谢谢大家的支持！可以点击我的<a href="http://www.360doc.com/userhome/54508727" target="_blank">头像</a>，进入我的空间浏览更多文章呢。建议大家360doc[</span><span style="background-color: rgb(215, 235, 197); text-decoration: underline; color: rgb(209, 86, 86); font-size: 16px;"><a href="http://www.360doc.com]%E6%B3%A8%E5%86%8C%E4%B8%80%E4%B8%AA%E8%B4%A6%E5%8F%B7%E7%99%BB%E5%BD%95%EF%BC%8C%E9%87%8C%E9%9D%A2%E7%9C%9F%E7%9A%84%E6%9C%89%E5%BE%88%E5%A4%9A%E4%BC%98%E7%A7%80%E7%9A%84%E6%96%87%E7%AB%A0%EF%BC%8C%E6%AC%A2%E8%BF%8E%E5%A4%A7%E5%AE%B6%E7%9A%84%E5%88%B0%E6%9D%A5%E3%80%82/" style="outline: 0px; color: rgb(61, 107, 167);">www.360doc.com]</a></span><span style="font-size: 16px;"><span style="color: rgb(209, 86, 86); font-size: 16px; background-color: rgb(215, 235, 197);">注册一个账号登录，里面真的有很多优秀的文章，欢迎大家的到来。</span><br>---</span></span></span></blockquote>';`
    var textarea = document.querySelector('textarea[style="position: absolute; padding: 0; width: 1px;"]');
    if (textarea) {
        // textarea 赋值
        textarea_value(textarea2=textarea,value=code);
        // title
        input1 = document.querySelectorAll('input#TextBox2')[0]
        input_value(input2=input1,value=title)
        // 标签
        input2 = $("input.f_left.txttags")[0]
        input_value(input2=input2,value=title)
        // 来源
        input3 = $('input[name="TextBox1"]')[0]
        input_value(input2=input3,value="http://www.rsgz.top/")
    }
}

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

2 document.addEventListener 的时候可以选择这两个DOMContentLoaded 和 load，那么这两个有什么区别
DOMContentLoaded: 当页面的 DOM 结构构建完成，但不包括样式表、图像等外部资源的加载完成的时候就出发了
load: 整个页面的所有资源（包括样式表、图像等外部资源）加载完成后触发。也就是说，当整个页面及其所有关联资源（如图片、样式表等）都加载完成后，load事件触发
*/
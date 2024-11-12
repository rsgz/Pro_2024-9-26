var wishpost_url = "https://www.wishpost.cn/";


// 进入wish post
// $(function (){
//     chrome.runtime.onMessage.addListener( function (request, sender, sendResponse){
//         if(request.to_wishpost=="to_wishpost"){
//             // window.location.href = "https://www.wishpost.cn/welcome/#/login?next=%2Forders-bag-search";
//             window.open('https://www.wishpost.cn/welcome/#/login?next=%2Forders-bag-search')
//         }
//     });
// });

$(function (){
    if (window.location.href.startsWith(wishpost_url)){
        console.log("wishpost.js 被加载")
        chrome.runtime.onMessage.addListener( async function (request, sender, sendResponse){
            // 进入wish post
            // if(request.to_wishpost=="to_wishpost"){
            //     window.location.href = "https://www.wishpost.cn/welcome/#/login?next=%2Forders-bag-search";
            // }

            // 填写预设样式和条件  denglu:"wishpost"
            if(request.denglu=="wishpost"){
                console.log("我登录了 wishpost")
                var input_denglu = $('form[novalidate="novalidate"]')[0].querySelectorAll('input')[0]
                input_value(input2=input_denglu,value="xxx")

                var input_mima = $('form[novalidate="novalidate"]')[0].querySelectorAll('input')[1]
                input_value(input2=input_mima,value="xxx")

                $('div.v-input--selection-controls__ripple')[0].click();
                await delay(500);
                $('div.v-card__text.pa-0>button>span.wt-btn-content')[0].click();
            }

            // 申诉
            if(request.shensu=="shensu"){
                // $('a[href="/payment-console"]')[0].click();
                window.location.href = "https://www.wishpost.cn/home/#/user/epc-dispute-tool";
            }

            // 历史运费
            if(request.lishiyunfei=="lishiyunfei"){
                window.location.href = "https://www.wishpost.cn/payment-console";
            }

            // 预估运费
            if(request.pingguyunfei=="pingguyunfei"){
                window.location.href = "https://www.wishpost.cn/home/#/logistics/logistics-products/advisor-tool";
            }

        });

    }
});

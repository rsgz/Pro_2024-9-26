// importScripts("js/jquery.js");
var dianxiaomi_url = "https://www.dianxiaomi.com";


function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}  

// 在background.js中，您可以监听并拦截请求，然后修改它们的参数
chrome.webRequest.onBeforeRequest.addListener(
    function(details) {
      // 检查请求是否符合您要拦截的条件
      /*
      Request URL:https://b08-api.shop6888.com/apis/Action
      method:POST
      {"action":"goods.search","data":{"pageIndex":1,"pageSize":20,"keywords":" car "}}
      */
      if (details.method === 'POST' && url.href === 'https://b08-api.shop6888.com/apis/Action') {
        /*
        // 修改请求参数
        let modifiedUrl = new URL(details.url);
        modifiedUrl.searchParams.set('paramName', 'newValue');
        
        // 返回一个修改过的请求对象
        return { redirectUrl: modifiedUrl.href };
        */

        try {
            // 尝试解析请求体为JSON
            requestJson = JSON.parse(decodeURIComponent(String.fromCharCode.apply(null, new Uint8Array(details.requestBody.raw[0].bytes))));
          } catch (e) {
            // 解析失败，可能是请求体不是JSON或者格式不正确
            console.error('Error parsing request body:', e);
            return; // 不修改请求
          }
    
          // 检查请求体是否包含特定的action和数据
          if (requestJson.action === 'goods.search' && requestJson.data) {
            // 修改请求参数
            requestJson.data.pageSize = 20000;
    
            // 将修改后的JSON对象转换回字符串
            let modifiedRequestBody = JSON.stringify(requestJson);
    
            // 返回一个包含修改后请求体的请求对象
            return {
              requestHeaders: details.requestHeaders,
              requestBody: {
                raw: [{
                  bytes: new TextEncoder().encode(modifiedRequestBody).buffer
                }]
              }
            };
          }
      }
    },
    // { urls: ["<all_urls>"] },
    { urls: ["https://b08-api.shop6888.com/apis/Action"] },
    ["blocking", 'requestBody']
  );
  

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    console.log(request)
    // --------------------------------------------- 获取所有界面tab  ---------------------------------------------
    // 传递信息给content.js
    if (request.method === "getTabs") {
        chrome.tabs.query({}, function(tabs) {
          let tabsInfo = tabs.map(tab => ({
            title: tab.title,
            url: tab.url
          }));
          sendResponse({tabsInfo: tabsInfo});
        });
        return true; // 表示异步响应
    }

    // --------------------------------------------- 抖音优化 ---------------------------------------------
    if (request.message === "downloadVideo") {
        var videoLink = request.videoLink; // 获取视频链接

        // 下载视频
        chrome.downloads.download({ url: videoLink }, downloadId => {
            if (downloadId === undefined) {
                console.error('下载失败');
            } else {
                console.log('下载已经开始，下载ID为:', downloadId);
            }
        });
    }

    // --------------------------------------------- 拼多多 ---------------------------------------------
    if (request.copy === "copy"){
        for(var i=0;i<request.imgs.length;i++){
            chrome.downloads.download({ url: request.imgs[i] }, downloadId => {
                if (downloadId === undefined) {
                    console.error('下载失败');
                } else {
                    console.log('下载已经开始，下载ID为:', downloadId);
                }
            });
        }
    }

    // --------------------------------------------- 店小蜜 ---------------------------------------------
    // 客服
    if(request.kefu==="dian_kefu"){
        // window.location.href = "https://www.dianxiaomi.com/ticket/index.htm?type=afterSale";
        chrome.tabs.create({ url: 'https://www.dianxiaomi.com/ticket/index.htm?type=afterSale' });
        console.log('...dian_kefu')
    }


    // --------------------------------------------- myshopify ---------------------------------------------
    // myshopify_jin_ru_kucun  进入库存
    if(request.myshopify_jin_ru_kucun==="myshopify_jin_ru_kucun"){
        chrome.tabs.create({ url: 'https://b08-admin.shop6888.com/#/goods/goodsManagement' });
        console.log('进入https://b08-admin.shop6888.com/#/goods/goodsManagement');
    }

    // myshopify_jin_ru_wang_zhan_guan_li  进入网站管理
    if(request.myshopify_jin_ru_wang_zhan_guan_li==="myshopify_jin_ru_wang_zhan_guan_li"){
        chrome.tabs.create({ url: 'https://b08-admin.shop6888.com/#/goods/shopWebsiteManagement' });
        console.log('进入https://b08-admin.shop6888.com/#/goods/shopWebsiteManagement')
    }

    // 网站内部预览  https://b08.shop6888.com/redirect?websiteid=264
    if(request.myshopify_neibu_yulan==="myshopify_neibu_yulan"){
        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            chrome.tabs.sendMessage(tabs[0].id, { myshopify_huoqu_bianhao_yuming: "myshopify_huoqu_bianhao_yuming" }, async function(response) {
                console.log("Content script response:", response);
                const bianhao_yuming_s1=response

                // Object.entries(bianhao_yuming_s1).forEach(async ([key, value]) => {
                //     console.log(`Key: ${key}, Value: ${value}`);
                //     console.log(`https://b08.shop6888.com/redirect?websiteid=${key}`);
                //     // const bianhao = key;
                //     const yuming = value;
                //     await delay(ms=1000);
                //     chrome.tabs.create({ url: `https://b08.shop6888.com/redirect?websiteid=${key}` });
                // });

                for (const [key, value] of Object.entries(response)) {
                    console.log(`Key: ${key}, Value: ${value}`);
                    console.log(`https://b08.shop6888.com/redirect?websiteid=${key}`);
        
                    // 创建标签页时使用唯一的 URL，并且使用正确的延迟方法
                    await new Promise(resolve => setTimeout(resolve, 300)); // 1秒延迟
                    chrome.tabs.create({ url: `https://b08.shop6888.com/redirect?websiteid=${key}` });
                }
            });
        });
    }

    // 网站外部预览 myshopify_waibu_yulan
    if(request.myshopify_waibu_yulan==="myshopify_waibu_yulan"){
        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            chrome.tabs.sendMessage(tabs[0].id, { myshopify_huoqu_bianhao_yuming: "myshopify_huoqu_bianhao_yuming" }, function(response) {
                console.log("Content script response:", response);
                const bianhao_yuming_s1=response
                Object.entries(bianhao_yuming_s1).forEach(([key, value]) => {
                    console.log(`Key: ${key}, Value: ${value}`);
                    const bianhao = key;
                    const yuming = value;
                    chrome.tabs.create({ url: `${yuming}` });
                });
            });
        });
    }

    // myshopify_shangping_shuliang  商品数量
    if(request.myshopify_shangping_shuliang==="myshopify_shangping_shuliang"){
        // 在 service-worker.js 中发送消息到 content.js
        chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
            chrome.tabs.sendMessage(tabs[0].id, { myshopify_huoqu_bianhao_yuming: "myshopify_huoqu_bianhao_yuming" }, function(response) {
                console.log("Content script response:", response);
                const bianhao_yuming_s1=response
                Object.entries(bianhao_yuming_s1).forEach(([key, value]) => {
                    console.log(`Key: ${key}, Value: ${value}`);
                    const bianhao = key;
                    const yuming = value.replace('https://','').replace('http://','');
                    chrome.tabs.create({ url: `https://b08-admin.shop6888.com/#/goods/shopGoodsManagement/${bianhao}_${yuming}` });
                });
            });
        });
        // const fanwei_start=Number(request.fanwei_start);
        // const fanwei_end=Number(request.fanwei_end);
        // chrome.storage.local.get(['myshopify_website_bianhao_yuming'], async function (data) {
            // const wangzhan_bianhaos = data.column1;
            // const yu_mings = data.column2;
            // for(var i=fanwei_start;i<=fanwei_end;i++){
                // chrome.tabs.create({ url: `https://b08-admin.shop6888.com/#/goods/shopGoodsManagement/${wangzhan_bianhaos[i-fanwei_start]}_${yu_mings[i-fanwei_start]}` });
            // }
        // });
        
        // console.log('打开了多个库存页面!这些库存页面的打开是根据你后台传进的csv文件决定的!');
    }

    // --------------------------------------------- timu ---------------------------------------------
    // 进入后台
    if(request.to_timu1==="to_timu1"){
        chrome.tabs.create({ url: 'https://kuajing.pinduoduo.com/' });
    }

    // 普通备货单
    if(request.to_timu2==="to_timu2"){
        chrome.tabs.create({ url: 'https://kuajing.pinduoduo.com/main/order-manage' });
    }

    // 发货台
    if(request.to_timu3==="to_timu3"){
        chrome.tabs.create({ url: 'https://kuajing.pinduoduo.com/main/order-manager/shipping-desk' });
    }

    // 下载
    if(request.xiazai==="xiazai"){
        // 获取图片的URL
        const imageUrl = 'https://img.ltwebstatic.com/images3_pi/2023/10/13/e0/1697165059ed829754d0d5dc0958766489fd5ded7f_thumbnail_220x293.jpg'; // 替换为你想要下载的图片的 URL

        // 下载图片
        chrome.downloads.download({ url: imageUrl }, downloadId => {
            if (downloadId === undefined) {
                console.error('下载失败');
            } else {
                console.log('下载已经开始，下载ID为:', downloadId);
            }
        });
    }


    // chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    //     if (changeInfo.status === 'complete' && tab.url === 'https://www.dianxiaomi.com/ticket/index.htm?type=afterSale') {
    //         // 在新页面加载完成后继续
    //         $('div[onclick="CUST_WISH_TICKET.setAfterSale(3, this);"]')[0].click();
    //     }
    // });
});


// console.log(chrome.tabs[0].audible)
var xiapi_rsgz = "https://seller.shopee.cn"
var xiapi_guanggao = "https://seller.shopee.cn/portal/marketing"
var xiapi_xinjiapo = "https://sg.xiapibuy.com/"
var xiapi_dainpuchanpin = "https://seller.shopee.cn/portal/product/list"
var xiapi_zhekou = "https://seller.shopee.cn/portal/marketing/discount/"
$(function (){
    if (window.location.href.startsWith(xiapi_rsgz||xiapi_xinjiapo)){
    //if (window.location.href.startsWith(xiapi_rsgz)){
        console.log("rsgz_shopee.js 被加载");
        chrome.runtime.onMessage.addListener( async function (request, sender, sendResponse){
            // -------------- 广告搜索关键词 -------------
            if (window.location.href.startsWith(xiapi_guanggao)){
                if(request.xiapi2==="xiapi2"){
                    await delay(200);
                    // p 标签所有包含的关键词
                    div= document.querySelectorAll("div[class=\"search-auto-list\"]")[0];
                    p_set = div.querySelectorAll("p")
                    p_words_l=[]
                    for (var i=0;i<p_set.length;i++) {
                        p = p_set[i];
                        p_words = p.innerText;
                        console.log(p_words)
                        p_words_l.push(p_words)
                    }

                    var lie1 = ["p_words_l"];
                    var shuxing = [p_words_l];

                    table1 = liebiaoTobiaoge(lie1,shuxing);
                    copy(table1)
                    console.log("广告搜索关键词:",table1)

                }

                if(request.xiapi3==="xiapi3"){
                    tr_set = document.querySelectorAll("div[class=\"selector\"] table tbody tr");
                    guanjianzi_l = []
                    sousuoliang_l = []
                    for (var i=0;i<tr_set.length;i++) {
                        tr = tr_set[i];
                        guanjianzi = tr.querySelectorAll('td')[0].innerText;
                        sousuoliang = tr.querySelectorAll('td')[2].innerText;
                        guanjianzi_l.push(guanjianzi)
                        sousuoliang_l.push(sousuoliang)
                    }

                    var lie1 = ["guanjianzi_l","sousuoliang_l"];
                    var shuxing = [guanjianzi_l, sousuoliang_l];

                    table1 = liebiaoTobiaoge(lie1,shuxing);
                    copy(table1)
                    console.log("关键词搜索量:",table1)
                }
            }

            // 站点 搜索框关键词
            if (window.location.href.startsWith(xiapi_xinjiapo)){
                if(request.xiapi4==="xiapi4"){
                    a_set = Array.from(document.querySelectorAll('div#shopee-searchbar-listbox a'));
                    a_set.slice(1,a_set.length);
                    lie1 =['sousuoci'];
                    shuxing=[a_set];
                    table = liebiaoTobiaoge(lie1, shuxing);
                    copy(table)
                    console.log("站点搜索关键词:",table)
                }
            }

            // 店铺产品    图片 标题 产品id 父sku
            if (window.location.href.startsWith(xiapi_dainpuchanpin)){
                if(request.xiapi5==="xiapi5"){
                    // 获取图片链接
                    pic_set = document.querySelectorAll("div.product-image.product-image-box img");
                    pic_url_l = Array.from(pic_set).map((img)=>{return img.getAttribute('src')});

                    // 获取标题
                    title_set = document.querySelectorAll('div.shopee-table__cell a span.product-name-wrap');
                    title_l = Array.from(title_set).map((title)=>{return title.innerText});

                    // 获取产品id
                    id_set = document.querySelectorAll("div.shopee-table__cell p.product-name-wrap a");
                    id_l = Array.from(id_set).map((id)=>{
                        id=id.getAttribute('href');
                        id=id.split('/');
                        id=id[id.length-1];
                        return id;
                    });

                    // 获取父 sku
                    div_set = document.querySelectorAll('div.product-sku div');
                    sku_l = Array.from(div_set).map((div)=>{return div.innerText.slice(7,div.innerText.length)});

                    lie1 = ['pic_url_l', 'title_l', 'id_l', 'sku_l'];
                    shuxing = [pic_url_l, title_l, id_l, sku_l];
                    table = liebiaoTobiaoge(lie1, shuxing);
                    copy(table)
                    console.log("产品数据抓取:",table)
                }
            }

            // 营销中心 填写折扣价格
            if (window.location.href.startsWith(xiapi_zhekou)){
                if(request.xiapi6==="xiapi6"){
                    xiapi6_input_value = request.xiapi6_input;
                    biao1 = document.querySelectorAll('div.discount-item-component')[0];
                    input_set = biao1.querySelectorAll('div.discount-edit-item-model-component form div.shopee-input.currency-input input');
                    Array.from(input_set).forEach((input)=>{input_value(input2=input,value=xiapi6_input_value)});
                }
            }


        });
    }

});

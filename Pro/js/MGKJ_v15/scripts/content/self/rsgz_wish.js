const wish_url = "https://www.wish.com/";


$(function (){
    if (window.location.href.startsWith(wish_url)){
        console.log("wish.js 被加载")
        chrome.runtime.onMessage.addListener(function (request, sender, sendResponse){
            const huilv = parseInt(request.hui)
            console.log("当前汇率: ", huilv)

            // ================================ 复制价格 =====================================
            if(request.wish_1=="SIZE XS"){
                console.log("SIZE XS 模式")
                var exchangeRate = huilv; // 汇率
                var table = document.createElement("table");
                var tr1 = document.createElement("tr");
                var th1 = document.createElement("th");
                var th2 = document.createElement("th");
                th1.innerHTML = "Size";
                th2.innerHTML = "Price";
                tr1.appendChild(th1);
                tr1.appendChild(th2);
                table.appendChild(tr1);
                chicun_l = ["SIZE XS","XS","SIZE S","SIZE M","SIZE L","SIZE XL","SIZE 2XL","S","M","L","XL","2XL","3XL","4XL","5XL","6XL","7XL","8XL"];
                divElements2 = document.querySelectorAll("div[class^=DimensionSection__DimensionText-sc]");
                divElements2.forEach(function(div) {
                    var chicun = div.innerText;
                    if (chicun_l.includes(chicun)) {
                        div.click();
                        var priceUSD = parseFloat(document.querySelectorAll('div[data-testid="product-price"]')[0].innerText.replace("$", ""));
                        var priceCOP = priceUSD * exchangeRate;

                        var tr = document.createElement("tr");
                        var td1 = document.createElement("td");
                        var td2 = document.createElement("td");
                        td1.innerHTML = chicun;
                        td2.innerHTML = priceCOP.toFixed(2) + "";
                        tr.appendChild(td1);
                        tr.appendChild(td2);
                        table.appendChild(tr);
                    }
                });

                console.log(table)
                copy(table);
            }

            if(request.wish_2=="SIZE 70cm"){
                var exchangeRate = huilv; // 汇率
                console.log("SIZE 70cm 模式")

                var table = document.createElement("table");
                var tr1 = document.createElement("tr");
                var th1 = document.createElement("th");
                var th2 = document.createElement("th");
                th1.innerHTML = "Size";
                th2.innerHTML = "Price";
                tr1.appendChild(th1);
                tr1.appendChild(th2);
                table.appendChild(tr1);
// chicun_l = ["SIZE XS","XS","SIZE S","SIZE M","SIZE L","SIZE XL","SIZE 2XL","S","M","L","XL","2XL","3XL","4XL","5XL","6XL","7XL","8XL"];
                chicun_l = ['SIZE 70cm', '70cm', 'SIZE 80cm','SIZE 90cm','SIZE 100cm','SIZE 110cm','80cm','90cm', '100cm', '110cm', '120cm', '130cm', '140cm', '150cm', '160cm', '170cm', '180cm']
                divElements2 = document.querySelectorAll("div[class^=DimensionSection__DimensionText-sc]");
                divElements2.forEach(function(div) {
                    var chicun = div.innerText;
                    if (chicun_l.includes(chicun)) {
                        div.click();
                        var priceUSD = parseFloat(document.querySelectorAll('div[data-testid="product-price"]')[0].innerText.replace("$", ""));
                        var priceCOP = priceUSD * exchangeRate;

                        var tr = document.createElement("tr");
                        var td1 = document.createElement("td");
                        var td2 = document.createElement("td");
                        td1.innerHTML = chicun;
                        td2.innerHTML = priceCOP.toFixed(2) + "";
                        tr.appendChild(td1);
                        tr.appendChild(td2);
                        table.appendChild(tr);
                    }
                });
                console.log(table)
                copy(table);

            }

            if(request.wish_3=="SIZE 70"){
                var exchangeRate = huilv; // 汇率
                console.log("SIZE 70 模式")

                var table = document.createElement("table");
                var tr1 = document.createElement("tr");
                var th1 = document.createElement("th");
                var th2 = document.createElement("th");
                th1.innerHTML = "Size";
                th2.innerHTML = "Price";
                tr1.appendChild(th1);
                tr1.appendChild(th2);
                table.appendChild(tr1);
// chicun_l = ["SIZE XS","XS","SIZE S","SIZE M","SIZE L","SIZE XL","SIZE 2XL","S","M","L","XL","2XL","3XL","4XL","5XL","6XL","7XL","8XL"];
                chicun_l = ['SIZE 70', '70', 'SIZE 80','SIZE 90','SIZE 100','SIZE 110','80','90', '100', '110', '120', '130', '140', '150', '160', '170', '180']
                divElements2 = document.querySelectorAll("div[class^=DimensionSection__DimensionText-sc]");
                divElements2.forEach(function(div) {
                    var chicun = div.innerText;
                    if (chicun_l.includes(chicun)) {
                        div.click();
                        var priceUSD = parseFloat(document.querySelectorAll('div[data-testid="product-price"]')[0].innerText.replace("$", ""));
                        var priceCOP = priceUSD * exchangeRate;

                        var tr = document.createElement("tr");
                        var td1 = document.createElement("td");
                        var td2 = document.createElement("td");
                        td1.innerHTML = chicun;
                        td2.innerHTML = priceCOP.toFixed(2) + "";
                        tr.appendChild(td1);
                        tr.appendChild(td2);
                        table.appendChild(tr);
                    }
                });
                console.log(table)
                copy(table);
            }

            // ================================ 复制价格 =====================================
            /*
            https://merchant.wish.com/md/home
            店铺评分 当前余额 待确认余额
             */
        });
    }
});

// ---------------------------------------白描app 复制 图片转表格----------------------------------------------
const baimiaoapp = "https://web.baimiaoapp.com/"

$(function (){
    if (window.location.href.startsWith(baimiaoapp)){
        chrome.runtime.onMessage.addListener(function (request, sender, sendResponse){
            if(request.baimiao_biao=="copy"){
                table1 = $("div.table-html-wrap>table")[0]
                copy(table1)
                console.log("复制表格成功!!! baimiao")
            }
        });
    }
});
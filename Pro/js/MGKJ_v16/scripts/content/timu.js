var timu_url = "https://kuajing.pinduoduo.com/";
var timu_url2 = "https://www.temu.com/";


// 所有的业务逻辑
if (window.location.href.startsWith(timu_url || timu_url2)) {
    console.log("timu.js 被加载")
    chrome.runtime.onMessage.addListener(async function(request, sender, sendResponse) {
        // 抢 发货台
        if(request.fahuotai1==="qiang"){
            let intervalId = null;
            let count = 0;
            let time_jiange = 0;
            let que = null;
            let span1 = null;
            let maxCount = 1;
            let start = parseInt(request.jiange_kaishi);  // 开始时间
            let end = parseInt(request.jiange_jieshu);    // 结束时间
            let stopRecursive=false;
            let tai = parseInt(request.taihao)-1  // 这是发货台号

            function getRandomInt(a, b) {
                // 确保a和b都为整数
                a = Math.floor(a);
                b = Math.floor(b);
                if (a > b) {
                    // 如果a大于b，交换它们的值
                    [a, b] = [b, a];
                }
                return Math.floor(Math.random() * (b - a + 1)) + a;
            }

            function ss() {
                console.log('输入  s()  来停止执行目标点击');
                if (stopRecursive) {return;}

                intervalId = setInterval(() => {
                    count++;
                    console.log('点击1次 --------------------->');
                    try {
                        console.log(start,end,tai)
                        span1 = Array.from(document.querySelectorAll('a[data-tracking-id]>span')).filter(v => v.textContent.includes('加入发货台'))[tai];
                        console.log(span1)
                        if (span1) {
                            const event = new MouseEvent('click', {
                                bubbles: true,
                                cancelable: true,
                                view: window
                            });
                            span1.dispatchEvent(event);

                            que = Array.from(document.querySelectorAll('div[data-testid="beast-core-portal-main"] span')).filter(v => v.textContent.includes('确认'))[0]
                            console.log(que)
                            que.click()
                        } else {
                            console.log('不存在此元素!!!');
                        }
                    }catch (e){
                        console.log(e)
                    }

                    if (count >= maxCount) {
                        console.log('已达到最大循环次数，销毁setInterval');
                        console.log('间隔:', time_jiange);
                        clearInterval(intervalId);
                        ss();
                    }

                    if(request.fahuotai2=="qiang_stop"){
                        stopRecursive = true;
                    }


                }, time_jiange);

                time_jiange = getRandomInt(start, end);
            }

            function s() {
                clearInterval(intervalId);
            }

            document.addEventListener('keydown', function(event) {
                if (event.key === 's') {
                    stopRecursive = true;
                    console.log('已停止');
                }
            });

            await delay(parseInt(request.runtime)*1000)
            ss();
        }

        // 提取排行榜数据
        if(request.temu_paihangbang1==="temu_paihangbang1"){
            console.log("----------- 排行榜数据抓取中 -----------")
            one = document.querySelector('div.autoFitList');
            list = one.querySelectorAll('div[role="link"] a[pageelsn]');  // a img list
            sale_l = one.querySelectorAll('div[role="link"] div[data-sales]');  //

            shangpingzhuye_l=[]
            title_l = []
            shangping_pic_l = []
            temu_price1_l = []
            temu_product_num_l = []
            temu_shichang_price_l = []
            zhekou_l = []

            // 提取网页数据
            for(var i=0;i<list.length;i++){
                ele = list[i];
                shangpingzhuye ="https://www.temu.com/"+ele.getAttribute('href');  // 商品主页
                title = ele.querySelector("img").getAttribute('alt');  // 标题
                shangping_pic = ele.querySelector("img").getAttribute('src');  // 图片链接

                sale_ele=sale_l[i];
                temu_price1 = sale_ele.querySelector('div[data-type="price"]').getAttribute("aria-label");  // 售价
                temu_product_num = sale_ele.querySelector('span[data-type="saleTips"]').getAttribute("aria-label").replace("sold","");  // 销量
                temu_shichang_price = sale_ele.querySelector('span[data-type="marketPrice"]').innerText;  // 市场价
                zhekou = sale_ele.querySelector('div[data-type="discount"] span').innerText;  // 折扣

                shangpingzhuye_l.push(shangpingzhuye);
                title_l.push(title)
                shangping_pic_l.push(shangping_pic)
                temu_price1_l.push(temu_price1)
                temu_product_num_l.push(temu_product_num)
                temu_shichang_price_l.push(temu_shichang_price)
                zhekou_l.push(zhekou)
            }

            var lie1 = ['商品图片', '价格', '销售数量', '市场价', '折扣','商品主页', '商品标题'];
            // var shop_level_value_l = [0, 0, 0, 0, 0];
            // var sale_value_l = [0, 0, 0, 0, 0];
            var shuxing = [shangping_pic_l, temu_price1_l, temu_product_num_l, temu_shichang_price_l, zhekou_l, shangpingzhuye_l, title_l];

            // 创建table元素
            var table1 = document.createElement("table");

            // 创建表头行
            var tr1 = document.createElement("tr");
            for (let i = 0; i < lie1.length; i++) {
                var th1 = document.createElement("th"); // 创建th元素
                th1.textContent = lie1[i]; // 设置th元素的文本内容
                tr1.appendChild(th1); // 将th元素添加到tr1元素中
            }
            table1.appendChild(tr1); // 将tr1元素添加到table1元素中

            // 创建数据行
            for (let j = 0; j < shuxing[0].length; j++) {
                var tr2 = document.createElement("tr");
                for (let i = 0; i < shuxing.length; i++) {
                    var td1 = document.createElement('td')
                    if (lie1[i]==='商品图片') { // 如果数组名包含'rsgz_pic'
                        var img = document.createElement('img'); // 创建img元素
                        img.setAttribute('src', shuxing[i][j]); // 设置img的src属性为图片链接
                        img.style.width = '50px'; // 设置img的宽度
                        img.style.height = '50px'; // 设置img的高度
                        td1.appendChild(img); // 将img添加到td元素中
                    } else {
                        td1.textContent = shuxing[i][j]; // 设置td元素的文本内容
                    }
                    tr2.appendChild(td1); // 将td元素添加到tr2元素中
                }
                table1.appendChild(tr2); // 将tr2元素添加到table1元素中
            }

            f = document.querySelector("footer")
            f.appendChild(table1)
            console.log(table1)
        }
    });
}
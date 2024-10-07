var dianxiaomi_url = "https://www.dianxiaomi.com";


// 所有的业务逻辑
if (window.location.href.startsWith(dianxiaomi_url)) {
    console.log("dxm_main.js 被加载")

    chrome.runtime.onMessage.addListener(async function (request, sender, sendResponse) {
        // ==================================== 页首 页末 ====================================
        // 滑动至页首
        if (request.action === "to_yeshou") {
            try {
                document.querySelectorAll("div.title.lh32")[0].scrollIntoView({behavior: "smooth"});
            } catch (err) {
                console.log(err);
            }
        }

        // 滑动至页末
        if (request.action === "to_yemo") {
            try {
                // document.querySelectorAll("div.foot-cont")[0].scrollIntoView({ behavior: "smooth" });
                document.querySelectorAll("div.paging-box.page-down")[0].scrollIntoView({behavior: "smooth"});
            } catch (err) {
                console.log(err);
            }
        }

        // ==================================== 抓取数据 ====================================
        dxm_zhua_data(request);   //这个被上面代替了

        // ==================================== 打广告 ====================================
        if (request.action === "do_advertising") {
            console.log("1 我来响应 do_advertising")
            // 一些值的初始化  ==========================================
//      clothing_type_choose="type2"  // 衣服大类的选择
            clothing_type_choose = request.clothing_type  // 衣服大类的选择
//      start_data="2023/2/3"          // 开始日期
            start_data = request.startData     // 开始日期
//      end_data="2023/3/8"            // 结束日期
            end_data = request.endData         // 结束日期

            console.log("2 clothing_type_choose:", clothing_type_choose)
            console.log("3 start_data:", start_data)
            console.log("4 end_data:", end_data)

            // 广告词预设
            // var clothing_type_arr = ['type1', 'type2', 'type3','type4']; // 服装类型
            // var keywords = {
            //   type1: ['long sleeve shirts for women','long sleeve tops','long sleeve tshirts','long sleeve tshirts round neck'], // 服装类型1对应的关键词
            //   type2: ['blouses','casual blouse for women','casual blouse tops','long sleeve casual blouse'], // 服装类型2对应的关键词
            //   type3: ['Ladies dress','3d half sleeve dress','Women casual dress','Half sleeve casual dress'], // 服装类型3对应的关键词
            //   type4: ['Ladies dress4','3d half sleeve dress4','Women casual dress4','Half sleeve casual dress4'] // 服装类型3对应的关键词
            // };

            chrome.storage.local.get(['column1', 'column2', 'column3'], function (data) {
                // 检查是否成功检索到数据
                if (chrome.runtime.lastError) {
                    console.error(chrome.runtime.lastError);
                    return;
                }


                console.log('5 content.js show data.column1:', data.column1);
                console.log('6 content.js show data.column2:', data.column2);
                const input1_arr = data.column1
                const input2_arr = data.column2
                const input3_arr = data.column3

                console.log("7 input1_arr:", input1_arr)
                var clothing_type_arr = input1_arr //服装类型
                // var clothing_type_arr = ['type1', 'type2', 'type3', 'type4']; // 服装类型
                // var input3_arr = [1, 2, 3, 4, 5];
                var keywords = {};

                for (var i = 0; i < clothing_type_arr.length; i++) {
                    var type = clothing_type_arr[i];
                    var keyword = input3_arr[i].toString().split(',');
                    keywords[type] = keyword;
                }
                console.log("8 keywords", keywords)
                console.log("9 keywords.type10", keywords.type10)


                // 返回随机大类的广告词
                const keywordMap = new Map();

                function return_clothing_types_keywords(dalei, dalei_arr) {
                    /*
                    clothing_types  这是服装定义的大类
                    clothing_type_arr  这是大类数组
                    count  这是对应返回关键词的数量
                    返回 ['blouses', 'casual blouse tops']
                    */
                    for (const type of dalei_arr) {
                        const ad_arr = keywords[type];
                        console.log("9.5 dalei:", dalei)
                        console.log("10 ad_arr:", ad_arr)
                        const random_ads = getRandomKeywords(ad_arr, 25); // 获取随机的25个关键词
                        keywordMap.set(type, random_ads);
                    }

                    console.log("11 keywordMap:", keywordMap)

                    function getRandomKeywords(arr, count) {
                        console.log("12 arr:", typeof arr, arr)
                        const shuffled = arr.sort(() => 0.5 - Math.random()); // 随机排序
                        a = shuffled.slice(0, count); // 截取指定数量的关键词
                        console.log("13 a:", a)
                        return a
                    }

                    return keywordMap.get(dalei);
                }

                // keywords_list = return_clothing_types_keywords(clothing_types="type2", clothing_type_arr=clothing_type_arr, count=25)

                // 这个可以实现在列表数据里面找到目标的人名和店铺等级
                function find_dianpu_info(dianpu_infos_arr, shop_name, find_obj) {
                    /*
                    the_dianpu_dengji = find_dianpu_info(dianpu_infos_arr=dianpu_infos,shop_name="侵权-110邬鹏飞 222",find_obj="dianpu_dengji")
                    the_renming = find_dianpu_info(dianpu_infos_arr=dianpu_infos,shop_name="侵权-110邬鹏飞 222",find_obj="renming")
                    */
                    if (find_obj == "renming") {
                        for (var i = 0; i < dianpu_infos_arr.length; i++) {
                            if (dianpu_infos_arr[i][0] == shop_name) {
                                // 如果数据库中的店铺名和寻找的店铺名一样
                                return dianpu_infos_arr[i][1]
                            }
                        }
                    } else if (find_obj == "dianpu_dengji") {
                        for (var i = 0; i < dianpu_infos_arr.length; i++) {
                            if (dianpu_infos_arr[i][0] == shop_name) {
                                // 如果数据库中的店铺名和寻找的店铺名一样
                                return dianpu_infos_arr[i][2]
                            }
                        }
                    }
                }

                // 计算天数间隔
                function calculateDateDifference(start_date, end_date) {
                    start_date = new Date(start_date);
                    end_date = new Date(end_date);
                    // 计算时间差异（以毫秒为单位）
                    var time_difference = end_date.getTime() - start_date.getTime();
                    // 将毫秒转换为天数
                    var days_difference = Math.ceil(time_difference / (1000 * 60 * 60 * 24));
                    return days_difference;
                }

                // var start_date = '2023/2/4';
                // var end_date = '2023/2/6';
                // var days_difference = calculateDateDifference(start_date, end_date);
                // console.log(days_difference);

                // 天数循环
                function date_dizeng(start_date, end_date, xunhuan_n) {
                    /*
                      开始日期 结束日期  循环次数
                      d = date_dizeng(start_date='2023/2/4',end_date='2023/3/2',xunhuan_n)
                    */
                    var days_difference = calculateDateDifference(start_date = start_date, end_date = end_date);
                    xunhuan_n = days_difference  // 根据天数间隔递增
                    var date_set = []
                    console.log("start_date:", start_date);
                    console.log("end_date:", end_date);
                    console.log("xunhuan_n:", xunhuan_n);

                    var startDate = new Date(start_date);
                    var endDate = new Date(end_date);
                    var currentDate = new Date(start_date);
                    for (var i = 0; i < xunhuan_n + 1; i++) {
                        date_set.push(currentDate.toLocaleDateString())
                        // console.log(currentDate.toLocaleDateString()); // 打印当前日期
                        // 递增日期
                        currentDate.setDate(currentDate.getDate() + 1);
                        // 如果超过结束日期，则重新回到开始日期
                        if (currentDate > endDate) {
                            currentDate = new Date(start_date);
                        }
                    }
                    return date_set
                }

                // 天数分组
                function date_fenzu(start_date, end_date) {
                    // 日期分组 25-26 26-27 27-28 28-29  递增分组
                    var date_set = date_dizeng(start_date = start_date, end_date = end_date, xunhuan_n = 0)
                    result = [];
                    for (var i = 0; i < date_set.length - 1; i++) {
                        // var start_date = date_set[i];
                        // var end_date = date_set[i + 1];
                        result.push([date_set[i], date_set[i + 1]]);
                    }
                    console.log(result)
                    return result
                }

                // 分组加倍
                function repeatedArray(originalArray, n) {
                    const repeatedArray = [];
                    for (let i = 0; i < n; i++) {
                        repeatedArray.push(...originalArray);
                    }
                    return repeatedArray;
                }

                /*
                const originalArray = [1, 2, 3];
                const result = repeatedArray(originalArray, 3);
                console.log(result); // [1, 2, 3, 1, 2, 3, 1, 2, 3]
                */

                // 图片  店铺   活动名称  产品id  活动时间  预算  广告词
                // 图片  活动名称  店铺名称 店铺等级 预算 wish_id PB关键词  连续活动    *开始时间(PST)  *结束时间(PST)  IntenseBoost

                console.log("函数外 clothing_type_arr 可用吗？", clothing_type_arr)

                function get_wish_info(callback) {
                    console.log("函数内 clothing_type_arr 可用吗？", clothing_type_arr)
                    console.log("开始 编辑selector")
                    // ======图片 id 店铺 sku 销量======
                    // 1 图片
                    pic_selector = 'td>div>div>img'
                    // 2 活动名称：姓名+fu_sku
                    fu_sku_selector = 'table[class="in-table-border wish-online-table"]>tbody>tr.content[data-shopid] td:nth-of-type(6)'
                    // 3 完整店铺名
                    // 铂金03郭亚松  这种形式店小蜜模板会报错的
                    dianpu_name = "div.gray-c[data-shopid]"
                    // 4 店铺等级
                    // 需要从店铺名里面处理字段
                    // 5 预算  默认 10.5
                    yusuan = "10.5"
                    // 6 wish_id  就是产品id
                    id_selector = 'div>div>div.limingcentUrlpic>a'
                    // 7 PB关键词
                    // 需要对应版随机25个
                    // 8 连续活动   默认不填写
                    // 9 *开始时间(PST) 手动输入
                    // 10 *结束时间(PST)  手动输入
                    // 11 IntenseBoost  默认不处理
                    var img_set = document.querySelectorAll(pic_selector)         // 1 图片
                    var fu_sku_set = document.querySelectorAll(fu_sku_selector)   // 2 活动名称：姓名+fu_sku
                    var dianpuming_set = document.querySelectorAll(dianpu_name)  // 3 完整店铺名
                                                                                 // 4 店铺等级
                                                                                 // 5 预算
                    var id_set = document.querySelectorAll(id_selector)           // 6 wish_id  就是产品id
                                                                                  // 7 PB关键词
                                                                                  // 8 连续活动   默认不填写
                                                                                  // 9 *开始时间(PST) 手动输入
                                                                                  // 10 *结束时间(PST)  手动输入
                                                                                  // 11 IntenseBoost  默认不处理
                    console.log("开始 创建table")
                    var table = document.createElement('table')
                    document.body.appendChild(table)
                    table.id = "rsgz_table"

                    table_sty = document.getElementById(table.id)
                    table_sty.border = 1
                    table_sty.cellSpacing = 0  // 设置边框
                    var thead = table.createTHead();
                    var tbody = table.createTBody();

                    var tr = document.createElement("tr");   //

                    th = document.createElement("th");
                    th.innerHTML = "图片"  // 1 图片
                    tr.appendChild(th);

                    th = document.createElement("th");
                    th.innerHTML = "店铺等级"  // 2 店铺等级
                    tr.appendChild(th);

                    th = document.createElement("th");
                    th.innerHTML = "活动名称"  // 2 活动名称
                    tr.appendChild(th);

                    th = document.createElement("th");
                    th.innerHTML = "店铺名称"  // 3 店铺名称
                    tr.appendChild(th);

                    th = document.createElement("th");
                    th.innerHTML = "预算"  // 4 预算
                    tr.appendChild(th);

                    th = document.createElement("th");
                    th.innerHTML = "Wish产品ID"  // 5 id
                    tr.appendChild(th);

                    th = document.createElement("th");
                    th.innerHTML = "PB关键词"  // 6 PB关键词
                    tr.appendChild(th);

                    th = document.createElement("th");
                    th.innerHTML = "连续活动"  // 7 连续活动
                    tr.appendChild(th);

                    th = document.createElement("th");
                    th.innerHTML = "开始时间(PST)"  // 8 开始时间(PST)
                    tr.appendChild(th);

                    th = document.createElement("th");
                    th.innerHTML = "结束时间(PST)"  // 9 结束时间(PST)
                    tr.appendChild(th);

                    th = document.createElement("th");
                    th.innerHTML = "IntenseBoost"  // 10 IntenseBoost
                    tr.appendChild(th);

                    thead.appendChild(tr);

                    console.log("开始 时间分组")
                    var arr = date_fenzu(start_date = start_data, end_date = end_data)
                    var new_date_arr = repeatedArray(originalArray = arr, n = Math.ceil(id_set.length / arr.length))  // 参数化成整数还得加1

                    console.log("id_set:", id_set)
                    console.log("开始 批量插入td数据")
                    for (let i = 0; i < id_set.length; i++) {
                        try {
                            console.log("i:", i, id_set[i])
                            var tr = document.createElement('tr')
                            var pic_td = document.createElement('td')
                            var newImg = document.createElement('img');
                            newImg.src = img_set[i].src;  // 1 图片
                            pic_td.appendChild(newImg);
                            tr.appendChild(pic_td)

                            var the_dianpu_dengji_td = document.createElement('td')
                            the_fu_sku = fu_sku_set[i].innerText
                            shop_name = dianpuming_set[i].innerText.replace(/「/g, '').replace(/」/g, '')  // 「铂金03郭亚松（Green Style Fashion Store）09」
                            the_dianpu_dengji = find_dianpu_info(dianpu_infos_arr = dianpu_infos, shop_name = shop_name, find_obj = "dianpu_dengji")
                            the_renming = find_dianpu_info(dianpu_infos_arr = dianpu_infos, shop_name = shop_name, find_obj = "renming")
                            the_dianpu_dengji_td.textContent = the_dianpu_dengji  // 2 店铺等级
                            tr.appendChild(the_dianpu_dengji_td)

                            var huodong_mingcheng_td = document.createElement('td')
                            huodong_mingcheng_td.textContent = the_renming + the_fu_sku  // 2 姓名+父sku  活动名称
                            tr.appendChild(huodong_mingcheng_td)

                            var shop_name_td = document.createElement('td')
                            shop_name_td.textContent = shop_name  // 3 店铺名称
                            tr.appendChild(shop_name_td)

                            var yusuan_td = document.createElement('td')
                            yusuan_td.textContent = yusuan  // 4 预算
                            tr.appendChild(yusuan_td)

                            var id_td = document.createElement('td')
                            id_td.textContent = id_set[i].innerText  // 5 wish ID
                            tr.appendChild(id_td)

                            var pb_td = document.createElement('td')
                            // get_wish_info(callback, the_clothing_type_arr)
                            console.log("pb_td.textContent: 调用随机 计算广告词 return_clothing_types_keywords")
                            // pb_td.textContent = return_clothing_types_keywords(clothing_type_choose, clothing_type_arr, 25)  // 6 PB关键词
                            pb_td.textContent = return_clothing_types_keywords(clothing_type_choose, clothing_type_arr)  // 6 PB关键词
                            tr.appendChild(pb_td)

                            var lianxu_td = document.createElement('td')
                            lianxu_td.textContent = ""  // 7 连续活动
                            tr.appendChild(lianxu_td)

                            var start_time_td = document.createElement('td')
                            start_time_td.textContent = new_date_arr[i][0]  // 8 开始时间(PST)
                            tr.appendChild(start_time_td)

                            var end_time_td = document.createElement('td')
                            end_time_td.textContent = new_date_arr[i][1]  // 9 结束时间(PST)
                            tr.appendChild(end_time_td)

                            var IntenseBoost_td = document.createElement('td')
                            IntenseBoost_td.textContent = ""  // IntenseBoost
                            tr.appendChild(IntenseBoost_td)
                            thead.appendChild(tr);
                        } catch (err) {
                            console.log(err)
                        }

                    }
                    callback();
                }

                get_wish_info(function () {
                    console.log("数据生成完毕~!")
                })

            });
        }

        // 复制广告
        if (request.action === "advertisingCopy") {
            function copy(element) {
                // 选择元素内容
                var selection = document.getSelection()
                var range = document.createRange()
                range.selectNodeContents(element)
                selection.removeAllRanges()
                selection.addRange(range)
                document.execCommand('copy')
            }

            try {
                // 能复制元素内容
                copy(document.querySelector("#rsgz_table"))
            } catch (e) {
                console.log(e)
            }

            try {
                // 能复制元素内容
                copy(document.querySelector("#table2"))
            } catch (e) {
                console.log(e)
            }


        }

        // 删除广告
        if (request.action === "advertisingDel") {
            try {
                // 能删除元素内容
                document.querySelector("#rsgz_table").remove()
            } catch (e) {
                console.log(e)
            }

            try {
                // 能删除元素内容
                document.querySelector("#table2").remove()
            } catch (e) {
                console.log(e)
            }

        }

        // 替换sku
        if (request.action === "do_tihuan_sku") {
            const lao_sku_value = request.lao_sku_value
            const xin_sku_value = request.xin_sku_value
            // lao = /CXYLT/g;  // regex = new RegExp(lao, "g");
            // xin='RongHuaCXYLT'
            const lao = new RegExp(lao_sku_value, "g");
            const xin = xin_sku_value
            fu_sku = document.querySelectorAll('input[datatype="parentSku"]')[0]
            document.querySelectorAll('input[datatype="parentSku"]')[0].value = fu_sku.value.replace(lao, xin)
            for (ele of document.querySelectorAll("input[name='sku']")) {
                ele.value = ele.value.replace(lao, xin)
            }
        }

        // ==================================== 客服 ====================================
        // 待发布
        if (request.daifabu === "dian_daifabu") {
            window.location.href = "https://www.dianxiaomi.com/product/offline.htm?productState=0&state=0";
        }

        // 在线产品
        if (request.zaixian_pro === "dian_zaixian_pro") {
            window.location.href = "https://www.dianxiaomi.com/product/index.htm";
        }

        // 客服
        if (request.dxm_kefu_text) {
            var sendContent = $("textarea#sendContent")[0];
            if (sendContent) {
                sendContent_value = sendContent.value + request.dxm_kefu_text;
                textarea_value(textarea2 = sendContent, value = sendContent_value)
            }
        }

        // ==================================== 下架 ====================================
        // 300页
        if(request.dxm_xiajia_wish=== "dxm_xiajia_300"){
            select = document.querySelector("#upPage > li:nth-child(1) > a > select")
            option = document.querySelector("#upPage > li:nth-child(1) > a > select > option:nth-child(3)")
            select_option(select,option)
        }

        // 高级筛选功能
        if(request.dxm_xiajia_wish=== "dxm_xiajia_shaixuan"){
            document.querySelector(".advancedSearchBtn").click();  // 高级筛选
            inp1 = document.querySelector("#soldLift");  // 出售量区间
            inp2 = document.querySelector("#soldRight");
            input_value(input2=inp1,value=0);
            input_value(input2=inp2,value=0);

            riq1 = document.querySelector("#timeLift");
            riq2 = document.querySelector("#timeRight");
            input_value(input2=riq1,value="2022-6-1");
            input_value(input2=riq2,value="2023-10-31");

            await delay(500);
            document.querySelector("td[class='f-right'] button[type='submit']").click();
        }

        // 测试销量 是否为0
        if (request.dxm_xiajia_wish === "dxm_xiajia_ce0") {
            dxm_xiaji_xiaoliang_num = 0
            gao_xiaoliang = []
            for (var i = 1; i <= 700; i++) {
                try {
                    xp = '//tbody/tr[' + String(i) + ']/td[5]'
                    text = document.evaluate(xp, document).iterateNext().innerText
                    if (parseInt(text) > 0) {
                        document.evaluate(xp, document).iterateNext().style.backgroundColor = "#ff0000";
                        document.evaluate(xp, document).iterateNext().style.fontSize = "40px";
                        document.evaluate(xp, document).iterateNext().style.color = "yellow";

                        // 记录销量值
                        xp_temp=document.evaluate(xp, document).iterateNext();
                        num_temp=parseInt(text);
                        gao_xiaoliang.push({xp:xp_temp,num:num_temp});

                        dxm_xiaji_xiaoliang_num++;
                    }else{
                        document.evaluate(xp, document).iterateNext().style.backgroundColor = 'green';
                    }

                } catch (e) {
                    // ....
                }
            }

            // 高销量定位
            if (dxm_xiaji_xiaoliang_num !== 0){
                arr= gao_xiaoliang
                var maxNum = Math.max(...arr.map(o => o.num));
                var maxXp = arr.find(o => o.num === maxNum).xp;
                move_to_ele(maxXp);
            }

            // 控制台提示
            if (dxm_xiaji_xiaoliang_num === 0) {
                console.log(dxm_xiaji_xiaoliang_num);
            } else {
                console.log(`xxxxxxxxxxx 不能下架 数据有问题 高销量 ${maxNum} xxxxxxxxxxx`,);
                console.log(`xxxxxxxxxxx 不能下架 数据有问题 高销量 ${maxNum} xxxxxxxxxxx`);
                console.log(`xxxxxxxxxxx 不能下架 数据有问题 高销量 ${maxNum} xxxxxxxxxxx`);
                console.log(`xxxxxxxxxxx 不能下架 数据有问题 高销量 ${maxNum} xxxxxxxxxxx`);
                console.log(`xxxxxxxxxxx 不能下架 数据有问题 高销量 ${maxNum} xxxxxxxxxxx`);
            }

        }

        // 下架产品 0-0 销量
        var xiaoliang_bioazhun = 0;
        if (request.dxm_xiajia_wish === "dxm_xiajia_xiajia") {
            if(dxm_xiaji_xiaoliang_num!==xiaoliang_bioazhun){
                alert("有销量不为0的产品 不能下架!!!")
                return;
            }
            document.querySelector("#selectAll").click();
            await delay(300);
            document.querySelector("div[class='pull-left tree_relative'] li:nth-child(5) a:nth-child(1)").click();
            await delay(500);
            document.querySelector("#asyncBatchModal > div.modal-dialog > div > div.modal-footer > button.button.btn-determine").click();
        }

        // 下一页
        if (request.dxm_xiajia_wish === "dxm_xiajia_xiayiye") {
            document.querySelector("ul[id='upPage'] a[title='下一页']").click();
        }


        // 综合三部
        if (request.dxm_xiajia_wish === "dxm_xiajia_3xia") {
            var start_opt=1
            async function ce1(){
                // 测试销量 是否为0
                if (start_opt===1) {
                    dxm_xiaji_xiaoliang_num = 0
                    gao_xiaoliang = []
                    for (var i = 1; i <= 700; i++) {
                        try {
                            xp = '//tbody/tr[' + String(i) + ']/td[5]'
                            text = document.evaluate(xp, document).iterateNext().innerText
                            if (parseInt(text) > 0) {
                                document.evaluate(xp, document).iterateNext().style.backgroundColor = "#ff0000";
                                document.evaluate(xp, document).iterateNext().style.fontSize = "40px";
                                document.evaluate(xp, document).iterateNext().style.color = "yellow";

                                // 记录销量值
                                xp_temp=document.evaluate(xp, document).iterateNext();
                                num_temp=parseInt(text);
                                gao_xiaoliang.push({xp:xp_temp,num:num_temp});

                                dxm_xiaji_xiaoliang_num++;
                            }else{
                                document.evaluate(xp, document).iterateNext().style.backgroundColor = 'green';
                            }

                        } catch (e) {
                            // ....
                        }
                    }

                    // 高销量定位
                    if (dxm_xiaji_xiaoliang_num !== 0){
                        arr= gao_xiaoliang
                        var maxNum = Math.max(...arr.map(o => o.num));
                        var maxXp = arr.find(o => o.num === maxNum).xp;
                        move_to_ele(maxXp);
                    }

                    // 控制台提示
                    if (dxm_xiaji_xiaoliang_num === 0) {
                        console.log(dxm_xiaji_xiaoliang_num);
                    } else {
                        console.log(`xxxxxxxxxxx 不能下架 数据有问题 高销量 ${maxNum} xxxxxxxxxxx`,);
                        console.log(`xxxxxxxxxxx 不能下架 数据有问题 高销量 ${maxNum} xxxxxxxxxxx`);
                        console.log(`xxxxxxxxxxx 不能下架 数据有问题 高销量 ${maxNum} xxxxxxxxxxx`);
                        console.log(`xxxxxxxxxxx 不能下架 数据有问题 高销量 ${maxNum} xxxxxxxxxxx`);
                        console.log(`xxxxxxxxxxx 不能下架 数据有问题 高销量 ${maxNum} xxxxxxxxxxx`);
                    }

                }
            }

            // 下架产品 0-0 销量
            async function xiao0(){
                var xiaoliang_bioazhun = 0;
                if (start_opt===1) {
                    if(dxm_xiaji_xiaoliang_num!==xiaoliang_bioazhun){
                        alert("有销量不为0的产品 不能下架!!!")
                        return;
                    }
                    document.querySelector("#selectAll").click();
                    await delay(300);
                    document.querySelector("div[class='pull-left tree_relative'] li:nth-child(5) a:nth-child(1)").click();
                    await delay(500);
                    document.querySelector("#asyncBatchModal > div.modal-dialog > div > div.modal-footer > button.button.btn-determine").click();
                }
            }

            // 下一页
            async function xia1(){
                if (start_opt===1) {
                    document.querySelector("ul[id='upPage'] a[title='下一页']").click();
                }
            }

            await ce1()
            await xiao0()
            await xia1()
            await (()=>{document.querySelector("div[id='syncBatchOfflineModal'] div[class='modal-footer'] button[type='button']").click()})()
            beep(250,200,30);
        }

        // 删除
        if (request.dxm_xiajia_wish === "dxm_xiajia_3del"){
            async function del_product(){
                // 全选
                document.querySelector("#selectAll").click();
                await delay(300);
                // 删除
                // document.querySelector("div[class='pull-left tree_relative'] li:nth-child(5) a:nth-child(1)").click();
                document.querySelector("div[class='pull-left tree_relative'] li:nth-child(8) a:nth-child(1)").click()
                await delay(500);
                // 彻底删除
                document.querySelector("div.gray-c.delDetail input").click()
                await delay(500);
                // 确定
                document.querySelector('div.modal-footer button[onclick="publishedProBatchDelete();"]').click()
                await delay(500);
                // 关闭
                document.querySelector('div.modal-footer button[onclick="closeSyncFromBatchModal();"]').click()
                await delay(500);
            }

            await del_product()
        }



    });
}






// ==================================== 抓取数据 ====================================
var dxm_zhua_data = (request)=>{
    console.log("dxm_zhua_data.js 被加载")
    // 抓取指定数据
    if (request.action === "do_drap_data") {
        try{
            console.log("pic:", request.pic)
            console.log("title:", request.title)
            console.log("id", request.id)
            console.log("shop_name", request.shop_name)
            console.log("shop_level", request.shop_level)
            console.log("ren_ming", request.ren_ming)
            console.log("shanghu_id", request.shanghu_id)
            console.log("sale", request.sale)
            console.log("fu_sku", request.fu_sku)
            console.log("creat_time", request.creat_time)
            console.log("update_time", request.update_time)
            console.log("audit_status", request.audit_status)

            // 显示选取的变量有哪些
            // request.temp,  这一个是没有的 但是呢 很奇怪 因为之前原来的数组 进行真假值过滤的时候总是往后退一位  然后我多加一位就好了
            var target = [
                request.temp,
                request.pic,
                request.title,
                request.id,
                request.shop_name,
                request.shop_level,
                request.ren_ming,
                request.shanghu_id,
                request.sale,
                request.fu_sku,
                request.creat_time,
                request.update_time,
                request.audit_status]
            // reduce 方式传递三个参数  acc表示累加到的数组 会返回 value
            // value 表示target 数组里面每个元素  if(value) 会过滤真值
            // index 是每个元素的索引
            const filteredVariables = target.reduce((acc, value, index) => {
                if (value) {
                    // consol.log("Object.keys(request)[index]:",Object.keys(request)[index], index)
                    console.log(value)
                    acc.push(Object.keys(request)[index]);
                }
                return acc;
            }, []);

            console.log("filteredVariables:", filteredVariables);  // ['shop_level', 'sale',"shop_level"]

            function find_dianpu_info(dianpu_infos_arr,shop_name,find_obj) {
                /*
                the_dianpu_dengji = find_dianpu_info(dianpu_infos_arr=dianpu_infos,shop_name="侵权-110邬鹏飞 222",find_obj="dianpu_dengji")
                the_renming = find_dianpu_info(dianpu_infos_arr=dianpu_infos,shop_name="侵权-110邬鹏飞 222",find_obj="renming")
                */
                if(find_obj=="renming"){
                    for(var i=0;i<dianpu_infos_arr.length;i++){
                        if(dianpu_infos_arr[i][0]==shop_name){
                            // 如果数据库中的店铺名和寻找的店铺名一样
                            return dianpu_infos_arr[i][1]
                        }
                    }
                } else if(find_obj=="dianpu_dengji"){
                    for(var i=0;i<dianpu_infos_arr.length;i++){
                        if(dianpu_infos_arr[i][0]==shop_name){
                            // 如果数据库中的店铺名和寻找的店铺名一样
                            return dianpu_infos_arr[i][2]
                        }
                    }
                }else if(find_obj=="shanghu_id"){
                    for(var i=0;i<dianpu_infos_arr.length;i++){
                        if(dianpu_infos_arr[i][0]==shop_name){
                            // 如果数据库中的店铺名和寻找的店铺名一样
                            return dianpu_infos_arr[i][3]
                        }
                    }
                }

            }

            // 需要根据选中的选项来抓取数据
            // var lie1 = ['shop_level', 'sale', 'shop_level'];
            var lie1 = filteredVariables;

            pic=document.querySelectorAll("td>div>div>img")
            title=[];
            id=[];
            shop_name_set=[];
            shop_level=[];
            ren_ming=[];
            shanghu_id=[]
            sale=[];
            fu_sku=[];
            creat_time=[];
            update_time=[];
            audit_status=[];

            var riqi_set = document.querySelectorAll('td.w70-all > p[data-toggle="tooltip"]');
            creat_time_set = Array.from(riqi_set).filter(function(element, index) {
                return index % 2 == 0;
            });

            update_time_set = Array.from(riqi_set).filter(function(element, index) {
                return index % 2 == 1;
            });

            // .innerText
            console.log("creat_time", creat_time)
            console.log("update_time", update_time)
            for(var ii = 0; ii < document.querySelectorAll("div>div>div.limingcentUrlpic>a").length; ii++) {
                the_shop_name = document.querySelectorAll("div.gray-c[data-shopid]")[ii].innerText.replace(/「/g, '').replace(/」/g, '')  // 「铂金03郭亚松（Green Style Fashion Store）09」

                the_dianpu_dengji = find_dianpu_info(dianpu_infos, the_shop_name, "dianpu_dengji")
                shop_level.push(the_dianpu_dengji)

                the_renming = find_dianpu_info(dianpu_infos, the_shop_name, "renming")
                the_shanghu_id = find_dianpu_info(dianpu_infos, the_shop_name, "shanghu_id")
                ren_ming.push(the_renming)

                shop_name_set.push(the_shop_name)
                title.push(document.querySelectorAll("span.white-space")[ii].innerText)
                id.push(document.querySelectorAll("div>div>div.limingcentUrlpic>a")[ii].innerText)
                sale.push(document.querySelectorAll('table[class="in-table-border wish-online-table"]>tbody>tr.content[data-shopid] td:nth-of-type(5)')[ii].innerText)
                fu_sku.push(document.querySelectorAll('table[class="in-table-border wish-online-table"]>tbody>tr.content[data-shopid] td:nth-of-type(6)')[ii].innerText)
                audit_status.push(document.querySelectorAll('div[class="p-top5 inline-block m-left4"]>span[data-original-title][title]:first-child')[ii].innerText)
                creat_time.push(creat_time_set[ii].innerText)
                update_time.push(update_time_set[ii].innerText)
                shanghu_id.push(the_shanghu_id)
            }

            console.log("shop_level", shop_level)
            console.log("ren_ming", ren_ming)

            // var shuxing = filteredVariables; // 这样直接写不行 需要字符串数组转化成变量数组
            var shuxing = []
            if(filteredVariables.includes("pic")){
                shuxing.push(pic)
                // console.log("pic", pic)
            }
            if(filteredVariables.includes("title")){
                shuxing.push(title)
                // console.log("title", title)
            }
            if(filteredVariables.includes("id")){
                shuxing.push(id)
                // console.log("id", id)
            }
            if(filteredVariables.includes("shop_name")){
                shuxing.push(shop_name_set)
            }
            if(filteredVariables.includes("shop_level")){
                shuxing.push(shop_level)
            }
            if(filteredVariables.includes("ren_ming")){
                shuxing.push(ren_ming)
            }
            if(filteredVariables.includes("shanghu_id")){
                shuxing.push(shanghu_id)
            }
            if(filteredVariables.includes("sale")){
                shuxing.push(sale)
            }
            if(filteredVariables.includes("fu_sku")){
                shuxing.push(fu_sku)
            }
            if(filteredVariables.includes("creat_time")){
                shuxing.push(creat_time)
            }
            if(filteredVariables.includes("update_time")){
                shuxing.push(update_time)
            }
            if(filteredVariables.includes("audit_status")){
                shuxing.push(audit_status)
            }

            console.log("shuxing:", shuxing)
            // 创建table元素
            var table1 = document.createElement("table");
            table1.border = 1
            table1.cellSpacing = 0  // 设置边框
            table1.id = "table2"

            // 创建表头行
            var tr1 = document.createElement("tr");
            for (let i = 0; i < lie1.length; i++) {
                var th1 = document.createElement("th"); // 创建th元素
                th1.textContent = lie1[i]; // 设置th元素的文本内容
                tr1.appendChild(th1); // 将th元素添加到tr1元素中
            }
            table1.appendChild(tr1); // 将tr1元素添加到table1元素中

            // 创建数据行
            for (let j = 0; j < document.querySelectorAll("div>div>div.limingcentUrlpic>a").length; j++) {
                var tr2 = document.createElement("tr");
                for (let i = 0; i < shuxing.length; i++) {
                    if(shuxing[i]==pic){
                        var td1 = document.createElement('td')
                        var newImg = document.createElement('img');
                        newImg.src = pic[j].src;  // 1 图片
                        td1.appendChild(newImg);
                        tr2.appendChild(td1)
                    }else{
                        var td1 = document.createElement("td"); // 创建td元素
                        td1.textContent = shuxing[i][j]; // 设置td元素的文本内容
                        tr2.appendChild(td1); // 将td元素添加到tr2元素中
                    }

                }
                table1.appendChild(tr2); // 将tr2元素添加到table1元素中
            }

            document.body.appendChild(table1)
            console.log("数据生成成功!!!");
        }catch (err){
            console.log(err);
        }
    }
}
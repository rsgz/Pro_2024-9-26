// --------------------------------------- 芒果店长 ----------------------------------------------
const mangguo_dianzhang = "https://www.mangoerp.com/"

$(function (){
    if (window.location.href.startsWith(mangguo_dianzhang)){
        console.log("mangguodianzhang.js 被加载!")
        chrome.runtime.onMessage.addListener(async function (request, sender, sendResponse){
            console.log("1111111")
            if(request.fahuo1=="yifahuo_wish"){
                des = Array.from(document.querySelectorAll("li.flex3>a")).filter(v=>v.textContent.includes('已发货'))[0]
                console.log(des)
                des.click()
            }

            if(request.pingtai=="wish_wish"){
                console.log("wish_wish")
                Array.from(document.querySelectorAll("a[ng-click=\"vm.filters.platform.add(platform.site)\"]")).filter(v=>v.textContent.includes('wish'))[0].click()
            }

            if(request.pingtai=="ozon_wish"){
                Array.from(document.querySelectorAll("a[ng-click=\"vm.filters.platform.add(platform.site)\"]")).filter(v=>v.textContent.includes('Ozon'))[0].click()
            }

            if(request.baoguo_ozon=="daochu"){
                $("a[ng-click=\"vm.exportPage('parcel')\"]")[0].click();
                setTimeout(()=>{
                    Array.from(document.querySelectorAll("button.btn.btn-primary.ng-binding")).filter(v=>v.textContent.includes('导出'))[0].click()
                    setTimeout(()=>{
                        Array.from(document.querySelectorAll("label")).filter(v=>v.textContent.includes(' ozon long 易邮宝'))[0].click()
                        setTimeout(()=>{
                            Array.from(document.querySelectorAll('button[class="btn btn-primary"]')).filter(v=>v.textContent.includes('下一步'))[0].click()
                            setTimeout(()=>{
                                Array.from(document.querySelectorAll('button[class="btn btn-primary"]')).filter(v=>v.textContent.includes('下一步'))[0].click()
                            },300)
                        },300)
                    },500)
                },100)
            }

            if(request.dayin_time=="today_wish"){
                Array.from(document.querySelectorAll("a[ng-click=\"vm.latest(1, 'printTime')\"]")).filter(v=>v.textContent.includes('今天'))[0].click()
            }

            if(request.dayin_time=="yesterday_wish"){
                Array.from(document.querySelectorAll("a[ng-click=\"vm.latest(4, 'printTime')\"]")).filter(v=>v.textContent.includes('昨天'))[0].click()
            }

            if(request.dayin_time=="1month_wish"){
                Array.from(document.querySelectorAll("a[ng-click=\"vm.selectDate('printTime')\"]")).filter(v=>v.textContent.includes('自定义时间'))[0].click()
                setTimeout(()=>{
                    inp1 = document.querySelector('input[ng-model="vm.startTime"]');
                    inp2 = document.querySelector('input[ng-model="vm.endTime"]');
                    var d=new Date()
                    var d2=new Date()
                    d2.setDate(d2.getDate() - 30)
                    d2.toLocaleString()

                    input_value(input2=inp1,value=d2.toLocaleString())
                    input_value(input2=inp2,value=d.toLocaleString())

                    fanwei1 = Array.from(document.querySelectorAll('div.modal-header.ng-scope')).filter(v=>v.textContent.includes('选择时间'))[0].nextElementSibling.nextElementSibling
                    Array.from(fanwei1.querySelectorAll("button")).filter(v=>v.textContent.includes('确定'))[0].click()
                }, 50);
            }

            if(request.dayin_time=="2month_wish"){
                Array.from(document.querySelectorAll("a[ng-click=\"vm.selectDate('printTime')\"]")).filter(v=>v.textContent.includes('自定义时间'))[0].click()
                setTimeout(()=>{
                    inp1 = document.querySelector('input[ng-model="vm.startTime"]');
                    inp2 = document.querySelector('input[ng-model="vm.endTime"]');
                    var d=new Date()
                    var d2=new Date()
                    d2.setDate(d2.getDate() - 60)
                    d2.toLocaleString()

                    input_value(input2=inp1,value=d2.toLocaleString())
                    input_value(input2=inp2,value=d.toLocaleString())

                    fanwei1 = Array.from(document.querySelectorAll('div.modal-header.ng-scope')).filter(v=>v.textContent.includes('选择时间'))[0].nextElementSibling.nextElementSibling
                    Array.from(fanwei1.querySelectorAll("button")).filter(v=>v.textContent.includes('确定'))[0].click()
                }, 50);
            }

            if(request.dayin_time=="3month_wish"){
                Array.from(document.querySelectorAll("a[ng-click=\"vm.selectDate('printTime')\"]")).filter(v=>v.textContent.includes('自定义时间'))[0].click()
                setTimeout(()=>{
                    inp1 = document.querySelector('input[ng-model="vm.startTime"]');
                    inp2 = document.querySelector('input[ng-model="vm.endTime"]');
                    var d=new Date()
                    var d2=new Date()
                    d2.setDate(d2.getDate() - 90)
                    d2.toLocaleString()

                    input_value(input2=inp1,value=d2.toLocaleString())
                    input_value(input2=inp2,value=d.toLocaleString())

                    fanwei1 = Array.from(document.querySelectorAll('div.modal-header.ng-scope')).filter(v=>v.textContent.includes('选择时间'))[0].nextElementSibling.nextElementSibling
                    Array.from(fanwei1.querySelectorAll("button")).filter(v=>v.textContent.includes('确定'))[0].click()
                }, 50);
            }

            if(request.order_status=="tuikuan_wish"){
                Array.from(document.querySelectorAll("a[ng-click=\"vm.searchRefund('y')\"]")).filter(v=>v.textContent.includes('已退款'))[0].click();
            }

            if(request.order_status=="daichuli_wish"){
                select1 = Array.from(document.querySelectorAll("select>optgroup>option[value=\"wish|APPROVED\"]")).filter(v=>v.textContent.includes('待处理'))[0];
                select1_fu = select1.parentNode.parentNode;
                select1.selected = true;
                select1_fu.dispatchEvent(new Event('change'));
            }

            if(request.fahuo_time_mangguo=="wu"){
                ele = Array.from(document.querySelectorAll("td>em.ng-binding")).filter(v=>v.textContent.includes('发货时间'))[0].parentNode.nextElementSibling
                ele.querySelectorAll("span>a>i")[0].click()
            }

            if(request.jiazaishuju_mangguo=="jiazaishuju_all"){
                xiahua();
            }

            if(request.diaji_red_mangguo=="diaji_red_mangguo_40"){
                fu_set = Array.from(document.querySelectorAll("div.mg-prd.ng-scope"))
                for(var i=0;i<fu_set.length;i++){
                    // console.log(`第${i+1}组`,fu_set[i].querySelectorAll("dd").length)
                    fangkuang_num = fu_set[i].querySelectorAll("dd").length==0?1:fu_set[i].querySelectorAll("dd").length
                    if(fangkuang_num==1){   // 单个方框的时候
                        num = parseInt(fu_set[i].querySelectorAll("ul li ul li>strong")[0].textContent)
                    }else{  // 多个方框呈现的时候  购买的种类不一样
                        num = 0
                        for(var num_i=0;num_i<fangkuang_num;num_i++){
                            num = num+parseInt(fu_set[i].querySelectorAll("dd ul li ul li>strong")[num_i].textContent)
                        }
                    }
                    text_all_price = Array.from(fu_set[i].querySelectorAll("div>span")).filter(v=>v.textContent.includes('总额'))[0].textContent
                    text_all_price = parseInt(text_all_price.split('\n')[3].replace(/ /g,''))

                    if(text_all_price/num<40){
                        fu_set[i].style.backgroundColor= "red";
                    }

                    // if(40<text_all_price/num<50){
                    //     fu_set[i].style.backgroundColor= "green";
                    // }
                    
                    // if(50<text_all_price/num<80){
                    //     fu_set[i].style.backgroundColor= "blue";
                    // }

                    console.log(`第${i+1}组,${fangkuang_num}个方框,${num}件服装`)
                }

            }

            if(request.wish_excel_daoru=="wish_excel_daoru"){
                console.log("导入excel")
                var daoru = Array.from(document.querySelectorAll("span.ng-scope")).filter(v=>v.textContent.includes('Excel导入'))[0]
                console.log("daoru")
                daoru.click()
            }

            // 女上衣分类
            if(request.wish_btn_xuanzefenlei=="wish_btn_xuanzefenlei"){
                console.log("------------ 选择上衣分类--衬衫 -----------");
                s=Array.from(document.querySelectorAll("button.btn.btn-sm.btn-default")).filter(v=>v.textContent.includes('选择分类'))[0]
                move_to(ele=s,y=50)
                Array.from(document.querySelectorAll("button.btn.btn-sm.btn-default")).filter(v=>v.textContent.includes('选择分类'))[0].click();
                await delay(700);
                Array.from(document.querySelectorAll("div.dd-handle>span.ng-binding.ng-scope")).filter(v=>v.textContent.includes("女装(Women's Clothing)"))[0].click();
                await delay(700);
                Array.from(document.querySelectorAll("div.dd-handle>span.ng-binding.ng-scope")).filter(v=>v.textContent.includes("上衣(Tops)"))[0].click();
                await delay(700);
                Array.from(document.querySelectorAll("div.dd-handle>span.ng-binding.ng-scope")).filter(v=>v.textContent.includes("衬衫和衬衫(Blouses & Shirts)"))[0].click();
                await delay(1200);
                (()=>{
                    // ================== 1 女衬衫 ==================
                    // 身体闭合
                    div = Array.from(document.querySelectorAll('div[ng-repeat="attr in vm.prdAttrs"]')).filter(v => v.textContent.includes("身体闭合"))[0];
                    div.querySelectorAll('select option[value="None"]')[0].selected = true;
                    div.querySelectorAll('select')[0].dispatchEvent(new Event('change'));

                    // 修身
                    div = Array.from(document.querySelectorAll('div[ng-repeat="attr in vm.prdAttrs"]')).filter(v => v.textContent.includes("修身"))[0];
                    div.querySelectorAll('select option[value="Plus Size"]')[0].selected = true;
                    div.querySelectorAll('select')[0].dispatchEvent(new Event('change'));

                    // 布料
                    div = Array.from(document.querySelectorAll('div[ng-repeat="attr in vm.prdAttrs"]')).filter(v => v.textContent.includes("布料"))[0];
                    div.querySelectorAll('select option[value="Polyester"]')[0].selected = true;
                    div.querySelectorAll('select')[0].dispatchEvent(new Event('change'));

                    // 领口
                    div = Array.from(document.querySelectorAll('div[ng-repeat="attr in vm.prdAttrs"]')).filter(v => v.textContent.includes("领口"))[0];
                    div.querySelectorAll('select option[value="Crew Neck"]')[0].selected = true;  // 圆领
                    // div.querySelectorAll('select option[value="Scoop Neck"]')[0].selected = true;  // 大圆领
                    // div.querySelectorAll('select option[value="V Neck"]')[0].selected = true;  // V领
                    div.querySelectorAll('select')[0].dispatchEvent(new Event('change'));

                    // 季
                    div = Array.from(document.querySelectorAll('div[ng-repeat="attr in vm.prdAttrs"]')).filter(v => v.textContent.includes("季"))[0];
                    div.querySelectorAll('select option[value="Fall/Winter"]')[0].selected = true;  // 秋冬
                    div.querySelectorAll('select option[value="Spring/Summer/Fall"]')[0].selected = true;  // 春夏秋
                    div.querySelectorAll('select')[0].dispatchEvent(new Event('change'));

                    // 尺寸-原产国
                    div = Array.from(document.querySelectorAll('div[ng-repeat="attr in vm.prdAttrs"]')).filter(v => v.textContent.includes("尺寸-原产国"))[0];
                    div.querySelectorAll('select option[value="CN"]')[0].selected = true;  // 中国
                    div.querySelectorAll('select')[0].dispatchEvent(new Event('change'));

                    // 袖长
                    div = Array.from(document.querySelectorAll('div[ng-repeat="attr in vm.prdAttrs"]')).filter(v => v.textContent.includes("袖长"))[0];
                    div.querySelectorAll('select option[value="Long Sleeve"]')[0].selected = true;  // 长袖
                    // div.querySelectorAll('select option[value="Short Sleeve"]')[0].selected = true;  // 短袖
                    // div.querySelectorAll('select option[value="Sleeveless"]')[0].selected = true;  // 无袖
                    // div.querySelectorAll('select option[value="Three-Quarter Sleeve"]')[0].selected = true;  // 中长袖
                    div.querySelectorAll('select')[0].dispatchEvent(new Event('change'));

                    // 洗涤方式
                    div = Array.from(document.querySelectorAll('div[ng-repeat="attr in vm.prdAttrs"]')).filter(v => v.textContent.includes("洗涤方式"))[0];
                    div.querySelectorAll('select option[value="Machine wash"]')[0].selected = true;  // 机洗
                    div.querySelectorAll('select')[0].dispatchEvent(new Event('change'));

                    // div.querySelectorAll('select option[value="Hand wash only"]')[0].selected = true;  // 手洗
                    // div.querySelectorAll('select')[0].dispatchEvent(new Event('change'));
                })();
            }

            // 自动运费计算
            if(request.wish_btn_zidongyunfei=="wish_btn_zidongyunfei"){
                console.log("------------ 自动运费计算 -----------");
                s='label'
                ele=Array.from(document.querySelectorAll(s)).filter(v => v.textContent.includes("标签"))[0];
                move_to_ele(ele=ele)
                await delay(200);
                s=document.querySelector('div.form-group>div>input[ng-model="vm.data.enableCalculateShippingAmount"]');
                document.querySelector('div.form-group>div>input[ng-model="vm.data.enableCalculateShippingAmount"]').click()
            }

            // 国家运费
            if(request.wish_guojiayunfei=="wish_guojiayunfei"){
                console.log("------------ 国家运费 -----------");
                s='a[ng-click="vm.countryShippingShow=true"]';
                ele=Array.from(document.querySelectorAll(s)).filter(v => v.textContent.includes("展开"))[0]
                ele.click();

                await delay(700);
                s='div[class="mui-select-header ng-scope"]'
                Array.from(document.querySelectorAll(s)).filter(v => v.textContent.includes("运费模板"))[0].click();
                await delay(700);
                s='div[ng-click="vm.selectNode(node, node.children.length)"]'
                Array.from(document.querySelectorAll(s)).filter(v => v.textContent.includes("仿照店小秘70"))[0].click();
                await delay(700);
                s='a[ng-click="vm.countryShippingShow=false"]'
                Array.from(document.querySelectorAll(s)).filter(v => v.textContent.includes("收起"))[0].click();
            }

            // 全新
            if(request.wish_quanxin=="wish_quanxin"){
                console.log("------------ 全新 -----------");
                s='div.form-group>div>select>option[value="NEW"]'
                zi = document.querySelectorAll(s)[0]
                fu=zi.parentElement
                zi.selected=true;
                fu.dispatchEvent(new Event('change'))
            }

            // 物流信息
            if(request.wish_wuliu1=="wish_wuliu1"){
                console.log("------------ 物流信息 -----------");
                s='label[class="col-sm-2 control-label"]';
                ele = Array.from(document.querySelectorAll(s)).filter(v => v.textContent.includes("国家运费"))[0];
                move_to_ele(ele=ele);

                await delay(200);
                s='div[class="mui-select-header ng-scope"]>div.read.ng-binding.ng-scope';
                text = '请选择';
                ele=Array.from(document.querySelectorAll(s)).filter(v => v.textContent.includes(text))[0];
                ele.click();

                await delay(700);
                s='li[ng-init="node = item"]>div';
                text = '中国，中华人民共和国';
                Array.from(document.querySelectorAll(s)).filter(v => v.textContent.includes(text))[0].click();

                await delay(700);
                s='div>input[name="weight"]';
                inpu = document.querySelector(s);
                input_value(input2=inpu,value=request.ke);
            }

            // 所有图片上传
            if(request.wish_pic_all=="wish_pic_all"){
                console.log("------------ 所有图片上传 -----------");
                s='div.panel-heading';
                text='视频';
                ele=Array.from(document.querySelectorAll(s)).filter(v => v.textContent.includes(text))[0];
                move_to_ele(ele=ele);

                await delay(200);
                s='div.pull-right>mg-widget-uploader input';
                document.querySelector(s).click();
            }

            // 单色图
            if(request.wish_pic_dansetu=="wish_pic_dansetu"){
                console.log("------------ 单色图 -----------");
                s='div.panel-heading';
                text='SKU信息';
                ele=Array.from(document.querySelectorAll(s)).filter(v => v.textContent.includes(text))[0];
                move_to_ele(ele=ele);

                await delay(200);
                s='a[ng-click="vm.colorImgFromProduct(img)"]'
                ele.nextElementSibling.querySelectorAll(s)[0].click();
            }

            // 基本上点击五次尺寸 3 代表颜色
            /*
            * 0*3+1
            * 2*3+1
            * 3*3+1
            * 4*3+1
            * 5*3+1
            * */
            if(request.wish_size_yingyong_all=="wish_size_yingyong_all"){
                console.log("------------ 五次尺寸 -----------");
                var color_num = parseInt(request.wish_yingyongchicun_color_num)
                var xpath1 = request.wish_yingyongchicun_xpath1

                console.log("color_num:", color_num)
                console.log(xpath1)
                groups = [0,2,3,4,5]
                for(g of groups){
                    n=String(g*color_num+1)
                    console.log(n,'--------------')
                    // /html/body/div[5]/div[1]/div/div/mg-box/div/div[1]/div/form/div[9]/div[2]/div/table/tbody/tr[1]/td[5]/div[1]/select
                    // /html/body/div[5]/div[1]/div/div/mg-box/div/div[1]/div/form/div[9]/div[2]/div/table/tbody/tr[2]/td[5]/div[1]/select
                    xpath2=xpath1.replace('tbody/tr[1]','tbody/tr['+n+']');
                    console.log(xpath2);
                    // select = document.querySelector(xpath2);
                    select = document.evaluate(xpath2, document).iterateNext()  // .click()
                    move_to_ele(select);
                    await delay(200);

                    option=select.querySelector('option[value="Other"]')
                    select_option(select=select,option=option)
                    await delay(200);

                    shang(select).click()
                    await delay(200);
                }
            }

            // 3XL-8XL 设置高重
            if(request.wish_size_3XL_8XL=="wish_size_3XL_8XL"){
                console.log("------------ 默认全低重 -----------");
                // 点击批量设置
                s='span>i.fa.fa-fw.fa-copy.red[tooltip="批量设置"]'
                document.querySelector(s).click();

                // 发货国 ------------------------------------
                // 找到h3模组父对象
                s='h3[class="modal-title"]';
                text = "设置子SKU物流信息";
                h3=Array.from(document.querySelectorAll(s)).filter(v => v.textContent.includes(text))[0].parentElement.parentElement;

                // 里面找到国家选择
                s='div[class="mui-select-header ng-scope"]>div.read.ng-binding.ng-scope';
                text = '请选择';
                ele=Array.from(h3.querySelectorAll(s)).filter(v => v.textContent.includes(text))[0];
                ele.click();

                // 选择国家
                await delay(700);
                s='li[ng-init="node = item"]>div';
                text = '中国，中华人民共和国';
                Array.from(h3.querySelectorAll(s)).filter(v => v.textContent.includes(text))[0].click();

                // 填写克重  ------------------------------------
                await delay(300);
                s='div>input[name="weight"]';
                inpu = h3.querySelector(s);

                var wish_dizhong = request.wish_size_3XL_8XL_gao_weight;
                console.log("wish_dizhong:", wish_dizhong);
                input_value(input2=inpu,value=wish_dizhong);

                // 确定
                Array.from(document.querySelectorAll('button[class="btn btn-primary"]')).filter(v => v.textContent.includes("确定"))[0].click();


                console.log("------------ 3XL-8XL设置高重 -----------");
                await delay(700);
                var wish_gaozhong = request.wish_size_3XL_8XL_di_weight;
                var wish_dizhong = request.wish_size_3XL_8XL_gao_weight;
                var wish_xpath_3XL = request.wish_xpath_3XL;
                var color_num2 = parseInt(request.color_num2);

                console.log("wish_gaozhong:", wish_gaozhong);
                console.log("wish_dizhong:", wish_dizhong);
                console.log("wish_xpath_3XL:", wish_xpath_3XL);
                console.log("color_num2:", color_num2);

                yan_num=color_num2
                gao_weight_value=wish_gaozhong
                size_num=11
                weizhi = 'tr['+String(size_num*yan_num+1)+']'  //  tr[67]
                shengyu_size=6
                console.log("weizhi:", weizhi);
                xpath = wish_xpath_3XL

                // xpath="/html/body/div[6]/div[1]/div/div/mg-box/div/div[1]/div/form/div[9]/div[2]/div/table/tbody/tr[67]/td[12]/div/label[2]/span"
                async function kezhong(){
                    for (var i = 0; i < shengyu_size*yan_num+1; i++) {
                        xpath2=xpath.replace(weizhi,'tr['+String(size_num*yan_num+i)+']')
                        console.log(xpath2)
                        document.evaluate(xpath2, document).iterateNext().click()

                        await delay(500);
                        s='h3.modal-title';
                        text = '设置子SKU物流信息';
                        h3=Array.from(document.querySelectorAll(s)).filter(v => v.textContent.includes(text))[0].parentElement.parentElement;

                        // input.form-control.ng-pristine.ng-untouched.ng-valid.ng-valid-required.ng-valid-pattern.ng-valid-min
                        // weight=document.querySelectorAll("input[name='weight']")
                        weight=h3.querySelector("input.form-control.ng-pristine.ng-untouched.ng-valid.ng-valid-required.ng-valid-pattern.ng-valid-min")
                        input_value(input2=weight,value=gao_weight_value)
                        await delay(500);
                        Array.from(h3.querySelectorAll('button[class="btn btn-primary"]')).filter(v => v.textContent.includes("确定"))[0].click();
                        await delay(500);
                    }
                }
                kezhong()

            }

            // 滑动至 3XL
            if(request.wish3XL=="wish3XL"){
                console.log("------------ 滑动至3XL -----------");
                s='div.form-control.mock-input.ng-binding';
                text = '3XL';
                ele=Array.from(document.querySelectorAll(s)).filter(v => v.textContent.includes(text))[1];
                move_to_ele(ele=ele);
            }

            // 页末
            if(request.wish_yemo=="wish_yemo"){
                console.log("------------ 滑至页末 -----------");
                s="label"
                text = 'California Proposition Chemical Names';
                ele=Array.from(document.querySelectorAll(s)).filter(v => v.textContent.includes(text))[0];
                move_to_ele(ele);
            }
        });
    }
});

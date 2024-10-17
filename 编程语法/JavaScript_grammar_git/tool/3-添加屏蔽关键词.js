/*
适用网址：https://b08-admin.shop6888.com/#/goods/goodsManagement
*/
// js字符串包含
function find_ele(where,text){
    // return Array.from(document.querySelectorAll('div.el-form-item__content button')).filter(v => v.textContent.includes('添加'))[0];
    return Array.from(document.querySelectorAll(where)).filter(v => v.textContent.includes(text))[0];
}

// 封装 document.querySelectorAll
function q(where){
    return document.querySelectorAll(where)
}

// input 输入框 赋值函数
function input_value(input2,value){
    // input2 = $(str_selector)[0]
    input2.value=value;
    var event2 = document.createEvent('HTMLEvents');
    event2.initEvent("input", true, true);
    event2.eventType = 'message';
    input2.dispatchEvent(event2);
}

// 延迟函数
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// 关键词列表
key_words = "Cardigan,Shacket,Jeans,Sweater,Skirt,Jacket,Legging,pant,Pajamas,\
Robe,Dress,Sleeve,Tank,Coat,HOODIE,Jersey, Tee,Sweatshirt, Top,V-Neck,shirt,\
Bra,Shorts,Short,Vest,Bodysuit,Jumpsuit,Swimwear,Bikini,Swim,Set,gown,Blazer,";
var key_word_arr = key_words.split(",");

(async () => {
    // 首次点击
    find_ele(where='div.el-form-item__content button',text='添加')?.click();

    for(var i=0;i<key_word_arr.length;i++){
        v = key_word_arr[i];
        await delay(100); // 等待3秒
        //console.log('延迟操作完成');
        // 输入关键词
        document.querySelectorAll('div.el-input-group--append')[0]
        await delay(100); // 等待3秒
        input1 = document.querySelectorAll('div.el-input-group--append')[0].querySelectorAll('div')[0].querySelector('input');
        // input_value(input2=input1,value='111');
        input_value(input2=input1,value=v);
        await delay(100); // 等待3秒
        // 确定并且 添加
        document.querySelectorAll('div.el-input-group--append')[0].querySelectorAll('div')[1].querySelectorAll('button')[0].click(); 
        
        await delay(100); // 等待3秒
        find_ele(where='div.el-form-item__content button',text='添加')?.click();
        await delay(100); // 等待3秒
      }
  })();
/*
这个版本增加了移动到 下一页 那个span 延迟 点击span.innerText='下一页' 的按钮
*/
u_all = ""
for(var i=0;i<=30;i++){
    try {
        u = document.querySelectorAll(`cite`)[i].innerText;
        if (isEmpty(obj=u)){
            console.error('');
        }else{
            // u_all = u_all+u+"\n";
            u_all = u_all+cleanShopifyUrl(url=u)+"\n";
        }
        
    } catch (error) {
      console.error('');
    }
    
}
console.log(u_all);
copyTextToClipboard(u_all);
span = findElementsContainingText(yuansu='span',text='下一页');
span[0].scrollIntoView({ behavior: 'smooth' }); // 移动到那个位置
// span[0].click();

(async () => {
    await delay(4000); // 等待3秒
    //console.log('延迟操作完成');
    span[0].click();
  })();

// 延迟函数
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


// js字符串包含
function findElementsContainingText(yuansu,text) {
    // 选择文档中的所有元素
    const allElements = document.querySelectorAll(yuansu);
    
    // 使用filter方法筛选出包含特定文本的元素
    const matchingElements = Array.from(allElements).filter(element => {
      // 使用toLowerCase确保搜索不区分大小写
      return element.innerText.toLowerCase().includes(text.toLowerCase());
    });
  
    return matchingElements;
}

// 处理字符串 https://xl3vintageclothing.myshopify.com › ...  把右边的都截取掉
function cleanShopifyUrl(url) {
    // 使用split方法分割字符串，取第一部分，即不包含"›"的部分
    return url.split(' ›')[0];
  }

// 判断字符串是否为空
function isEmpty(obj){
    if(typeof obj == "undefined" || obj == null || obj == ""){
        return true;
    }else{
        return false;
    }
}

// 复制
function copyTextToClipboard(text) {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.select();
    try {
        const successful = document.execCommand('copy');
        const msg = successful ? 'successful' : 'unsuccessful';
        console.log('Copying text command was ' + msg);
    } catch (err) {
        console.error('Oops, unable to copy', err);
    }
    document.body.removeChild(textArea);
}


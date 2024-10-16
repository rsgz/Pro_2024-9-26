/*
这个版本将结果 ›以及后面的字符串都去除掉
https://xl3vintageclothing.myshopify.com › ...
https://castoreus.myshopify.com › products
https://ussportsdownunder.myshopify.com › ...
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


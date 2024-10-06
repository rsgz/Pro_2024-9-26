/*
这个版本将结果为空的那一行过滤掉了
*/
u_all = ""
for(var i=0;i<=30;i++){
    try {
        u = document.querySelectorAll(`cite`)[i].innerText;
        if (isEmpty(obj=u)){
            console.error('');
        }else{
            u_all = u_all+u+"\n";
        }
        
    } catch (error) {
      console.error('');
    }
    
}
console.log(u_all);

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

copyTextToClipboard(u_all);
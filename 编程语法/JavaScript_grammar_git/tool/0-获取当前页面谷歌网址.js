u_all = ""
for(var i=0;i<=30;i++){
    try {
        u = document.querySelectorAll(`cite`)[i].innerText;
        u_all = u_all+u+'\n';
    } catch (error) {
      console.error('');
    }
    
}
console.log(u_all);

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
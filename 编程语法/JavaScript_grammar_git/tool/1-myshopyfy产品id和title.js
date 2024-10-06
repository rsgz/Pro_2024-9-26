/*
或许到这些数据
适用网址：https://b08-admin.shop6888.com/#/goods/goodsManagement
1988077-->Kechele Nitro Nugget 6'2 Surfboard - FCS II
1988068-->Kechele Nitro Nugget 5'8 Surfboard - FCS II
1988057-->Kechele Nitro Nugget 5'11 Surfboard - FCS II
*/

// del_set = [1736986,1736823,1736798]
len = document.querySelectorAll(`table.el-table__body tr`).length;
v1_all = "";
for(var i=0;i<len;i++){
    var tr = document.querySelectorAll(`table.el-table__body tr`)[i];
    var v3 = tr.querySelectorAll(`td`)[3]; // title
    var v1 = tr.querySelectorAll(`td`)[1]; // id
    var v0 = tr.querySelectorAll(`td`)[0];  // 单选框

    v_temp = v1.innerText + "-->"+v3.innerText;
    v1_all = v1_all+v_temp+'\n';
    /*
    for(j=0;j<del_set;j++){
    	if(del_set[i]==Number(v1.text())){
    		v0.find(`label`).click();
    	}
    }
    */
    // console.log(i+1,"-->",v.text()); // 使用.text()来获取文本内容
    // data =data + v.text() + "\n";
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

copyTextToClipboard(v1_all);
/*
适用网址：https://b08-admin.shop6888.com/#/goods/goodsManagement
点击目标产品id所有产品  选中它们
*/

len = document.querySelectorAll(`table.el-table__body tr`).length;
key_paichu = [
    "Sweatshirt",
    "Top",
    "V-Neck",
    "Tee"
]
for(var i=0;i<len;i++){
    var tr = document.querySelectorAll(`table.el-table__body tr`)[i];
    var v3 = tr.querySelectorAll(`td`)[3]; // title
    var v1 = tr.querySelectorAll(`td`)[1]; // id
    var v0 = tr.querySelectorAll(`td`)[0];  // 单选框
    let title= v3.innerText;

    click_flag = 1; // 默认所有点击
    for(var j=0;j<key_paichu.length;j++){
        let key = key_paichu[j];
        let flag = title.includes(key);
        if(flag==true){  // 包含 主角
            click_flag = 0;
        }
    }

    if(click_flag == 1){
        v0.querySelectorAll(`label`)[0].click();
    }
}
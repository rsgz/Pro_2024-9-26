/*
适用网址：https://b08-admin.shop6888.com/#/goods/goodsManagement
点击目标产品id所有产品  选中它们
*/

del_set = [2004244,1992969,1992962,1992955,1992947,1992685,1992646,1992638,1992319,1991636,1991622,1991610,1991599,1991590,1991578,1991264,1991262,1991252,1991243,1991229,1991220,1991189,1991145,1991138,1991122,1990144,1990134,1990122,1990037,1990016,1990006,1989995,1989986,1989979,1989975,1989965,1989958,1989956,1989948,1989932,1989923,1989912,1989909,1989899,1989892,1989877,1989867,1989860,1989849,1989659,1988446,1988438,1988420,1988409,1988398,1988386,1988369,1988354,1988344,1988326,1988314,1988301,1988286,1988258,1988248,1988236,1988225,1988211,1988203,1988195,1988183,1988175,1988166,1988152,1988140,1988133,1988120,1988107,1988100,1988090,1988077,1988068,1988057]
len = document.querySelectorAll(`table.el-table__body tr`).length;
v1_all = "";
for(var i=0;i<len;i++){
    var tr = document.querySelectorAll(`table.el-table__body tr`)[i];
    var v3 = tr.querySelectorAll(`td`)[3]; // title
    var v1 = tr.querySelectorAll(`td`)[1]; // id
    var v0 = tr.querySelectorAll(`td`)[0];  // 单选框

    let flag = del_set.includes(Number(v1.innerText));
    if(flag){
        v0.querySelectorAll(`label`)[0].click();
    }
}
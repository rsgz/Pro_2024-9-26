table = "table.el-table__body"  # 先锁定 table
# tr = "tr:eq(0)"  # 指定第一行 tr
tr = "tr"  # 每一行 tr
td = "td:eq(1)"  # 第几个 td

s = f"""\
var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
document.getElementsByTagName('head')[0].appendChild(script);

for(var i=0;i<100;i++){{
    var tr = $(`{table} {tr}`).eq(i)
    var v = tr.find(`{td}`);
    console.log(v.text()); // 使用.text()来获取文本内容
}}
"""
print(s)
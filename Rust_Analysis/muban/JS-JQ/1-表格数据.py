table = "table.el-table__body"  # 先锁定 table
# tr = "tr:eq(0)"  # 指定第一行 tr
tr = "tr"  # 每一行 tr
td = "td:eq(1)"  # 第几个 td

s = f"""\
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ v1 单纯打印版本 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
// 延迟函数
function delay(ms) {{
    return new Promise(resolve => setTimeout(resolve, ms));
}}

function initialization(){{
    var script = document.createElement('script');
    script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
    document.getElementsByTagName('head')[0].appendChild(script);
}}

function main(){{
    len = $(`{table} {tr}`).length;
    for(var i=0;i<len;i++){{
        var tr = $(`{table} {tr}`).eq(i)
        var v = tr.find(`{td}`);
        console.log(v.text()); // 使用.text()来获取文本内容
    }}
}}

async function run() {{
    initialization()
    await delay(1000);
    main();
}}

run();

﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ v2 数据复制到粘贴板 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
// 使用的时候 一定要立即切换到 浏览器主界面 navigator 安全性限制 必须是 用户行为
// 延迟函数
function delay(ms) {{
    return new Promise(resolve => setTimeout(resolve, ms));
}}

async function copyTextToClipboard_navigator(text) {{
    if (!navigator.clipboard) {{
        // Clipboard API 不可用时回退到旧的复制方法
        fallbackCopyTextToClipboard(text);
        return;
    }}
    try {{
        await navigator.clipboard.writeText(text);
        console.log('Copying to clipboard was successful!');
    }} catch (err) {{
        console.error('Could not copy text: ', err);
    }}
}}
    

// 复制字符串到粘贴板函数 复制文本
function copyTextToClipboard(text) {{
    const textArea = document.createElement("textarea");
    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.select();
    try {{
        const successful = document.execCommand('copy');
        const msg = successful ? 'successful' : 'unsuccessful';
        console.log('Copying text command was ' + msg);
    }} catch (err) {{
        console.error('Oops, unable to copy', err);
    }}
    document.body.removeChild(textArea);
}}

function initialization(){{
    var script = document.createElement('script');
    script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
    document.getElementsByTagName('head')[0].appendChild(script);
}}

async function main(){{
    var data = "";
    len = $(`{table} {tr}`).length;
    for(var i=0;i<len;i++){{
        var tr = $(`{table} {tr}`).eq(i)
        var v = tr.find(`{td}`);
        console.log(i+1,"-->",v.text()); // 使用.text()来获取文本内容
        data =data + v.text() + "\\n";
    }}
    // await delay(1000);
    // copyTextToClipboard(data);  // 这个超过 1500行就会复制失败
    copyTextToClipboard_navigator(data);  // navigator 不会有这个限制
}}

async function run() {{
    initialization()
    await delay(3000);
    main();
}}

run();
﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀ 代码结束 ﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀﹀
"""
print(s)
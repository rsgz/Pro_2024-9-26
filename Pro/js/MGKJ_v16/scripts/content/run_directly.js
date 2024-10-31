console.log("run_directly.js 被加载")
var dianxiaomi_url = "https://www.dianxiaomi.com";
var a_360_doc_url = "http://www.360doc.com/"
var a_360_doc_url_edit = "http://www.360doc.com/edit/"
var a_xiapi ="https://seller.shopee.cn/"

/*
* 下面的模块将会直接加载到页面中
*/

current_url = window.location.href
console.log("当前网址:",current_url)
// ==================任何网址 优化==================
try{
    // <span id="state_4">161900</span>
    setTimeout(()=>{

        // 创建并插入样式
        var style = document.createElement('style');
        style.type = 'text/css';
        style.innerHTML = `
        .alert {
            display: none; /* 默认不显示 */
            width: 560px;
            height: 396px;
            border-radius: 3px;
            background-color: rgba(80, 227, 194, 0.45);
            background-image: none;
            background-position-x: 0%;
            background-repeat: no-repeat;
            padding: 10px;
            margin-top: 10px;
            color: #721c24;
            border: 1px solid #f5c6cb;
            text-align: center;
            line-height: 396px;
        }
        `;
        document.head.appendChild(style);

        // 创建悬浮按钮  复制按钮
        var button = document.createElement('button');
        button.id='rsgz_btn001';
        button.textContent = '复制';
        button.style.position = 'fixed';
        // 老式写法
        button.style.top = '700px';
        button.style.right = '1780px';
        button.style.zIndex = 9999;
        button.style.backgroundColor = '#000000'; // 设置背景颜色为黑色
        button.style.color = 'white';           // 设置文字颜色为白色
        button.style.padding = '10px 27px 10px 37px';  // 设置内边距

        var button2 = document.createElement('button');
        button2.textContent = '进入';
        button2.style.position = 'fixed';
        button2.style.top = '750px';
        button2.style.right = '1780px';
        button2.style.zIndex = 9999;
        button2.style.backgroundColor = '#000000'; // 设置背景颜色为黑色
        button2.style.color = 'white';           // 设置文字颜色为白色
        button2.style.padding = '10px 27px 10px 37px';  // 设置内边距

        // 复制当前页网址
        var button3 = document.createElement('button');
        button3.textContent = '当前';
        button3.style.position = 'fixed';
        button3.style.top = '800px';
        button3.style.right = '1780px';
        button3.style.zIndex = 9999;
        button3.style.backgroundColor = '#000000'; // 设置背景颜色为黑色
        button3.style.color = 'white';           // 设置文字颜色为白色
        button3.style.padding = '10px 27px 10px 37px';  // 设置内边距

        // 所有已经打开的页面
        var button4 = document.createElement('button');
        button4.textContent = '标签';
        button4.style.position = 'fixed';
        button4.style.top = '850px';
        button4.style.right = '1780px';
        button4.style.zIndex = 9999;
        button4.style.backgroundColor = '#000000'; // 设置背景颜色为黑色
        button4.style.color = 'white';           // 设置文字颜色为白色
        button4.style.padding = '10px 27px 10px 37px';  // 设置内边距

        // 添加悬浮按钮到页面  进入网址按钮 来源粘贴板的网址
        document.body.appendChild(button);
        document.body.appendChild(button2);
        document.body.appendChild(button3);
        document.body.appendChild(button4);

        // 设置页面上所有元素的文本可复制
        function makeTextCopyable() {
            const allElements = document.querySelectorAll('*');
            allElements.forEach(element => {
                element.style.userSelect = 'auto';
                element.style.webkitUserSelect = 'auto';
                element.style.MozUserSelect = 'auto';
                element.style.msUserSelect = 'auto';
            });
        }

        // 添加点击事件监听器
        button.addEventListener('click', async function() {
            var selection = window.getSelection();
            console.log("点击了复制");

            // 创建新的div元素 
            var alertBox = document.createElement('div');
            alertBox.className = 'alert'; // 添加CSS类名
            alertBox.textContent = '复制成功!'; // 设置提示文本
            document.body.appendChild(alertBox); // 将div添加到页面中
            
            // 显示提示信息
            alertBox.style.display = 'block';

            // 一秒后隐藏提示信息并从DOM中移除
            setTimeout(function() {
                alertBox.style.display = 'none'; // 隐藏提示信息
                alertBox.parentNode.removeChild(alertBox); // 从DOM中移除提示信息
            }, 500);
  
            if (selection.rangeCount > 0) {
                var range = selection.getRangeAt(0);
                var objs = range.cloneContents();
                var tempElement = document.createElement("div");
                tempElement.appendChild(objs);
                var links = tempElement.getElementsByTagName("a");
                var allText = '';

                for (var i = 0; i < links.length; i++) {
                    allText += links[i].innerText.trim() + ':' + links[i].href + '\n';
                }

                copyTextToClipboard(allText);
            }
        });

        // 添加点击事件监听器
        button2.addEventListener('click', async function() {
            // 创建新的div元素 
            var alertBox = document.createElement('div');
            alertBox.className = 'alert'; // 添加CSS类名
            alertBox.textContent = '进入!'; // 设置提示文本
            document.body.appendChild(alertBox); // 将div添加到页面中
            
            // 显示提示信息
            alertBox.style.display = 'block';

            // 一秒后隐藏提示信息并从DOM中移除
            setTimeout(function() {
                alertBox.style.display = 'none'; // 隐藏提示信息
                alertBox.parentNode.removeChild(alertBox); // 从DOM中移除提示信息
            }, 500);

            try {
                // 获取剪贴板内容
                console.log("点击了进入");
                const clipboardText = await navigator.clipboard.readText();
                // 将浏览器当前页面跳转到剪贴板中的网址
                window.location.href = clipboardText;
            } catch (error) {
                console.error('无法从剪贴板读取内容:', error);
                alert('无法从剪贴板读取内容，请确保剪贴板中包含有效的URL。');
            }
        });

        // 添加点击事件监听器
        button3.addEventListener('click', function() {
            console.log("点击了btn3");

            // 创建新的div元素 
            var alertBox = document.createElement('div');
            alertBox.className = 'alert'; // 添加CSS类名
            alertBox.textContent = '复制当前页!'; // 设置提示文本
            document.body.appendChild(alertBox); // 将div添加到页面中
            
            // 显示提示信息
            alertBox.style.display = 'block';

            // 一秒后隐藏提示信息并从DOM中移除
            setTimeout(function() {
                alertBox.style.display = 'none'; // 隐藏提示信息
                alertBox.parentNode.removeChild(alertBox); // 从DOM中移除提示信息
            }, 500);

            // 获取当前网页的标题和网址
            const pageTitle = document.title;
            const pageUrl = window.location.href;
            // 将标题和网址组合，中间用冒号分隔
            const textToCopy = `${pageTitle}:${pageUrl}`;

            // 将组合后的文本复制到剪贴板
            navigator.clipboard.writeText(textToCopy).then(function() {
                // 复制成功后的操作，例如可以弹出一个提示
                // alert('Title and URL copied to clipboard.');
                console.log('Title and URL copied to clipboard.');
            }, function(err) {
                // 处理复制失败的情况
                console.error('Could not copy text: ', err);
                // alert('Failed to copy Title and URL.');
            });
        });


        // 添加点击事件监听器
        button4.addEventListener('click', async function() {
            try {
                console.log("点击了进入btn4");
                // 向background发送消息请求所有标签页的信息
                chrome.runtime.sendMessage({method: "getTabs"}, function(response) {
                    console.log(response.tabsInfo); // 这将打印所有标签页的标题和URL
                    var tabs_self = response.tabsInfo;
                    
                    // 使用map创建一个包含所有标签页信息的字符串数组
                    var tabsInfoString = tabs_self.map(function(tab) {
                        return tab.title + " - " + tab.url;
                    }).join("\n"); // 使用join将数组连接成一个字符串，每个信息之间用换行符分隔

                    copyTextToClipboard(tabsInfoString);

                    // 这里是处理tabsInfoString的代码，例如可以将其显示在页面上或进行其他操作
                    // 例如，你可以创建一个文本节点并添加到infos元素中
                    var textNode = document.createTextNode(tabsInfoString);


                    // 创建新的div元素 
                    var infos = document.createElement('div');
                    infos.className = 'infos'; // 添加CSS类名
                    // infos.textContent = 'infos'; // 设置提示文本
                    infos.textContent = tabsInfoString;
                    infos.style.position = 'absolute';

                    infos.style.top = '50%';
                    infos.style.left = '50%';
                    infos.style.transform = 'translate(-50%, -50%)'; 

                    // infos.style.top = '200px';
                    // infos.style.right = '500px';
                    infos.style.width='1200px';
                    infos.style.height='800px';
                    infos.style.backgroundColor = 'rgba(80, 227, 194, 0.55)';
                    infos.style.color = "black";
                    infos.style.borderRadius = "6px";
                    infos.style.padding = "15px";
                    // infos.style.backgroundColor = '#50E3C2';
                    document.body.appendChild(infos); // 将div添加到页面中
                    
                    // 显示提示信息
                    // infos.appendChild(textNode);
                    infos.style.display = 'block';

                    // 一秒后隐藏提示信息并从DOM中移除
                    setTimeout(function() {
                        infos.style.display = 'none'; // 隐藏提示信息
                        infos.parentNode.removeChild(infos); // 从DOM中移除提示信息
                    }, 1000);

                    
                    document.body.appendChild(infos); // 将infos元素添加到页面中

                });


            } catch (error) {
                console.error('btn4 无法获取tabs！');
            }
        });

        // 监听键盘事件来触发按钮点击
        document.addEventListener('keydown', function(event) {
            if (event.ctrlKey && event.shiftKey && event.key === '1') {
                console.log("你触发了btn1！");
                button.click(); // 触发按钮点击
                event.preventDefault(); // 防止默认快捷键行为
            }
        });

        // 复制文本到剪贴板的函数
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

        // 设置页面上所有元素的文本可复制
        function makeTextCopyable() {
            const allElements = document.querySelectorAll('*');
            allElements.forEach(element => {
                element.style.userSelect = 'auto';
                element.style.webkitUserSelect = 'auto';
                element.style.MozUserSelect = 'auto';
                element.style.msUserSelect = 'auto';
            });
        }

        // 在页面加载完毕后执行函数
        document.addEventListener('DOMContentLoaded', makeTextCopyable);

        // text = document.querySelector("#state_4").innerText
        // document.querySelector("#state_4").style.color="red";
        // document.querySelector("#state_4").style.fontSize="30px";
        // document.querySelector("#state_4").innerText = text +" ---> 28号到现在已下架 "+String(parseInt(text)-180801)+" ---> "+ String((parseInt(text)-180801)/10000).slice(0,4)+"w" + " --->  已删除"+ String((957082-parseInt(text))/10000).slice(0,4)+"w"
    },500)

}catch (e) {
    // ...
}

// ==================店小蜜 优化==================
if (window.location.href.startsWith(dianxiaomi_url)){
    try{
        // <span id="state_4">161900</span>
        setTimeout(()=>{
            text = document.querySelector("#state_4").innerText
            document.querySelector("#state_4").style.color="red";
            document.querySelector("#state_4").style.fontSize="30px";
            document.querySelector("#state_4").innerText = text +" ---> 28号到现在已下架 "+String(parseInt(text)-180801)+" ---> "+ String((parseInt(text)-180801)/10000).slice(0,4)+"w" + " --->  已删除"+ String((957082-parseInt(text))/10000).slice(0,4)+"w"
        },500)

    }catch (e) {
        // ...
    }

}

// ==================虾皮 优化==================
if (window.location.href.startsWith(a_xiapi)){
    if (window.location.href.startsWith(a_xiapi)){
        // 按了 快捷键Ctrl+y 执行js  就会添加链接
        setTimeout(()=>{
            a_l= Array.from(document.querySelectorAll('a.product-name-wrap'))
            a_l = a_l.map((url)=> {return url.getAttribute('href').replace('/portal/product/','')})
            //like_set = Array.from(document.querySelectorAll('div.product-list-item__td.product-variation__sales div.text-overflow2'))
            //for(var i=0;i<like_set.length;i++){                   product-list-item__td product-variation__sales
            //    like = like_set[i]
            //    like.innerText = like.innerText + '---' +a_l[i]
            //}

            tbody = document.querySelectorAll('tbody')[0]
            console.log("tbody", tbody)
            i=0
            tbody.querySelectorAll('tr').forEach(function(tr) {
                // 获取当前行的第二个td元素
                var secondTd = tr.children[1];

                // 创建一个新的div元素
                var newDiv = document.createElement('div');

                // 设置div的内容或属性（例如class、id等）
                newDiv.textContent = a_l[i];
                // 或者
                newDiv.className = 'myDivClass';

                // 将新创建的div元素添加到第二个td内部
                secondTd.appendChild(newDiv);
                i++;
            });
        },4000)

    }
}

// ==================360doc 优化==================
if (window.location.href.startsWith(a_360_doc_url)){
    if (window.location.href.startsWith(a_360_doc_url_edit)){
        // 按了 快捷键Ctrl+y 执行js  就会添加链接
        document.addEventListener('keydown', function(event) {
            if (event.ctrlKey && event.keyCode === 89) { // 89 是 Y 的 ASCII 码
                document.querySelector("#insertlink").click();
            }
        });
    }
}




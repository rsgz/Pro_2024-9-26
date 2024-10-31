/*
下面建立了一些便捷函数
*/

// js字符串包含
function find_ele(where,text){
    // return Array.from(document.querySelectorAll('div.el-form-item__content button')).filter(v => v.textContent.includes('添加'))[0];
    return Array.from(document.querySelectorAll(where)).filter(v => v.textContent.includes(text))[0];
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
  /*
  // 使用示例：
  const searchText = '特定字符串';
  const elementsWithText = findElementsContainingText(searchText);
  // elementsWithText 将是一个包含所有innerText包含'特定字符串'的元素的数组
  */

// 随机值 getRandomInt(21, 25) 
function getRandomInt(a, b) {
	// 确保a和b都为整数
	a = Math.floor(a);
	b = Math.floor(b);
	if (a > b) {
		// 如果a大于b，交换它们的值
		[a, b] = [b, a];
	}
	return Math.floor(Math.random() * (b - a + 1)) + a;
}

// 列表转表格
function  liebiaoTobiaoge(lie1, shuxing){
    /*
        var lie1 = ['shop_level', 'sale', 'shop_level'];
        var shuxing = [shop_level_value_l, sale_value_l, shop_level_value_l];
     */

    // 创建table元素
    var table1 = document.createElement("table");

    // 创建表头行
    var tr1 = document.createElement("tr");
    for (let i = 0; i < lie1.length; i++) {
        var th1 = document.createElement("th"); // 创建th元素
        th1.textContent = lie1[i]; // 设置th元素的文本内容
        tr1.appendChild(th1); // 将th元素添加到tr1元素中
    }
    table1.appendChild(tr1); // 将tr1元素添加到table1元素中

    // 创建数据行
    for (let j = 0; j < shuxing[0].length; j++) {
        var tr2 = document.createElement("tr");
        for (let i = 0; i < shuxing.length; i++) {
            var td1 = document.createElement("td"); // 创建td元素
            td1.textContent = shuxing[i][j]; // 设置td元素的文本内容
            tr2.appendChild(td1); // 将td元素添加到tr2元素中
        }
        table1.appendChild(tr2); // 将tr2元素添加到table1元素中
    }

    //console.log(table1);
    return table1
}

// 列表转表格 横向
function liebiaoTobiaoge_heng(lie1, shuxing){
    /*
        var lie1 = ['shop_level', 'sale', 'shop_level'];
        var shuxing = [shop_level_value_l, sale_value_l, shop_level_value_l];
     */

    // 创建table元素
    var table1 = document.createElement("table");

    for (let i = 0; i < lie1.length; i++) {
        // 创建tr元素
        var tr = document.createElement("tr");
        var th1 = document.createElement("th"); // 创建th元素
        th1.textContent = lie1[i]; // 设置th元素的文本内容
        tr.appendChild(th1); // 将th元素添加到tr元素中

        for (let j = 0; j < shuxing[i].length; j++) {
            var td1 = document.createElement("td"); // 创建td元素
            td1.textContent = shuxing[i][j]; // 设置td元素的文本内容
            tr.appendChild(td1); // 将td元素添加到tr元素中
        }
        table1.appendChild(tr); // 将tr元素添加到table元素中
    }

    return table1;
}

// beep 函数
function beep(duration, frequency, volume){
    /*
    * beep(
    // Set the duration to 0.2 second (200 milliseconds)
    200,
    // Set the frequency of the note to A4 (440 Hz)
    440,
    // Set the volume of the beep to 100%
    100
);
    *
    * */
    const myAudioContext = new AudioContext();

    return new Promise((resolve, reject) => {
        // Set default duration if not provided
        duration = duration || 200;
        frequency = frequency || 440;
        volume = volume || 100;

        try{
            let oscillatorNode = myAudioContext.createOscillator();
            let gainNode = myAudioContext.createGain();
            oscillatorNode.connect(gainNode);

            // Set the oscillator frequency in hertz
            oscillatorNode.frequency.value = frequency;

            // Set the type of oscillator
            oscillatorNode.type= "square";
            gainNode.connect(myAudioContext.destination);

            // Set the gain to the volume
            gainNode.gain.value = volume * 0.01;

            // Start audio with the desired duration
            oscillatorNode.start(myAudioContext.currentTime);
            oscillatorNode.stop(myAudioContext.currentTime + duration * 0.001);

            // Resolve the promise when the sound is finished
            oscillatorNode.onended = () => {
                resolve();
            };
        }catch(error){
            reject(error);
        }
    });
}

// 异常
function trys(block){
    try{
        block
    }catch (e) {

    }
}

// 复制元素函数
function copy(element) {
    // 判断要复制的元素是否存在于文档中
    if (document.contains(element)) {
        // 选择元素内容
        var selection = document.getSelection()
        var range = document.createRange()
        range.selectNodeContents(element)
        selection.removeAllRanges()
        selection.addRange(range)

        // 如果存在，则直接复制元素
        document.execCommand("copy");
    } else {
        // 如果不存在，则将元素添加到文档中再复制
        document.body.appendChild(element);

        // 选择元素内容
        var selection = document.getSelection()
        var range = document.createRange()
        range.selectNodeContents(element)
        selection.removeAllRanges()
        selection.addRange(range)

        document.execCommand("copy");
        // 复制成功后，从文档中删除元素
        document.body.removeChild(element);
    }


}

// 复制文本
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

// content 接受消息 content-->网页
function zhixing(fun1){
    // dongzuo(request, sender, sendResponse)
    chrome.runtime.onMessage.addListener(dongzuo)
}

// popup 发送信息  popup-->content
// 消息发送给当前活动窗口的内容脚本
function send_to_content(message) {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, message, function(response) {
            // 在消息发送成功后执行的操作
            console.log('');
        });
    });
}

function sendText(text) {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, { text: text });
    });
}

// 延迟函数
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// input 输入框 赋值函数
function input_value(input2,value){
    // input2 = $(str_selector)[0]
    input2.value=value;
    var event2 = document.createEvent('HTMLEvents');
    event2.initEvent("input", true, true);
    event2.eventType = 'message';
    input2.dispatchEvent(event2);
}

// textarea 赋值函数
function textarea_value(textarea2,value){
    textarea2.value = value;
    var event2 = document.createEvent('Event');
    event2.initEvent('input', true, true);
    textarea2.dispatchEvent(event2);
}

// select option
function select_option(select,option){
    // select='select[name="condition"][ng-model="vm.data.condition"]'
    // option='option[value="NEW"]'
    // v3(select=select,option=option)
    // select.querySelectorAll(option)[0].selected = true;
    option.selected = true;
    select.dispatchEvent(new Event('change'));
}

// 往下滑动
function xiahua() {
    window.scrollTo(0, document.body.scrollHeight);
}

// move to
var move_to = (ele,y)=>{
    // 获取指定元素的位置
    var elementPosY=ele.offsetTop;
    // 设置页面滚动条位置
    window.scrollTo(0, elementPosY - y);
}

var move_to_ele=(ele)=>{
    ele.scrollIntoView();
}

var xia=(ele)=>{
    return ele.nextElementSibling;
}

var shang=(ele)=>{
    return ele.previousElementSibling;
}

var xia0=(ele)=>{
    return ele.nextSibling;
}
var shang0=(ele)=>{
    return ele.previousSibling;
}

var fu=(ele)=>{
    return ele.parentElement;
}

var fu1=(ele)=>{
    return ele.parentElement;
}

// 选择option
/*
if(request.order_status=="tuikuan_wish"){
    select1 = Array.from(document.querySelectorAll("a[ng-click=\"vm.searchRefund('y')\"]")).filter(v=>v.textContent.includes('已退款'))[0];
    select1_fu = select1.parentNode.parentNode;
    select1.selected = true;
    select1_fu.dispatchEvent(new Event('change'));
}
*/
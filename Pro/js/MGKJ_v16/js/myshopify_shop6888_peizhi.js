// 添加保存按钮点击事件监听器
document.getElementById('save-button').addEventListener('click', saveData)
document.getElementById('delete-button').addEventListener('click', () =>deleteSpecificData(['column1', 'column2', 'column3', 'column4', 'column5', 'column6', 'column7', 'column8', 'column9', 'column10']))
document.getElementById('exportToCSV_button').addEventListener('click', exportToCSV)
document.getElementById('importCSV_button').addEventListener('click', importCSV)
document.addEventListener('DOMContentLoaded', showData);

// 格式转换为为CSV
function convertToCSV(table) {
    var csv = [];
    var rows = table.getElementsByTagName('tr');

    for (var i = 0; i < rows.length; i++) {
        var row = [];
        var cols = rows[i].querySelectorAll('td>input,th');
        console.log(cols)
        for (var j = 0; j < cols.length; j++) {
            if(cols[j].tagName==='INPUT'){
                row.push(cols[j].value.replace(/,/g, ';'));
            }else if(cols[j].tagName==='TH'){
                row.push(cols[j].innerText);
            }
        }
        console.log(row)
        csv.push(row.join(','));
    }
    return csv.join('\n');
}

// 下载逻辑
function downloadCSV(csv, filename) {
    var csvFile = new Blob([csv])
    function createBlob(csvFile) {
        var link = document.createElement('a');
        link.href = URL.createObjectURL(csvFile);
        link.download = filename;
        link.style.display = 'none';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };
    createBlob(csvFile);

}

// 导出 命名
function exportToCSV() {
    var table = document.getElementById('myTable');
    var csv = convertToCSV(table);
    var filename = 'shop6888.csv';
    downloadCSV(csv, filename);
}

// 导入csv逻辑
function importCSV() {
    var fileInput = document.getElementById('csvFileInput');
    console.log('fileInput:',fileInput);
    var file = fileInput.files[0];
    var reader = new FileReader();

    reader.onload = function(e) {
        var contents = e.target.result;
        // 在这里处理 CSV 文件的内容
        parseCSV(contents);
    };

    reader.readAsText(file);
}

// 解析csv文件
function parseCSV(csv) {
    var lines = csv.split('\n');
    // alert(lines)
    // alert(lines[1])
    // alert(lines[1].split(','))
    // alert(typeof lines[1].split(',')[0])

    // 创建几行 放在第一行
    const tbody=document.querySelectorAll('tbody')[0]
    const the_td = tbody.querySelectorAll('td')[0]
    console.log(the_td)
    add_hang_n(numRows=lines.length-1,td=the_td)

    const table = document.querySelectorAll('table')[0]
    tr_set = table.querySelectorAll('tr')

    for (var i = 1; i < lines.length; i++) {  // 一共有多少行
        const heng_str = lines[i]
        const hang=tr_set[i]
        console.log("hang:",hang)  // 页面上的 td input成功生成了
        td_set = hang.querySelectorAll('td')
        for (var j = 0; j < td_set.length; j++) {  // 一共有多少列
            // console.log("td_set[j]:",td_set[j])
            if(td_set[j].tagName==="TD"){
                td_set[j].classList.add('text-center');
                zhi = heng_str.split(';')[j]//.replace(/;/g, ',')
                td_set[j].querySelector('input').value=zhi;
                td_set[j].querySelector('input').classList.add('text-center');
            }
        }
    }
}

// 保存数据的函数
function saveData() {
    // 获取三列输入框的值
    var input1_arr = Array.from(document.querySelectorAll('.column1'), (input) => input.value);
    var input2_arr = Array.from(document.querySelectorAll('.column2'), (input) => input.value);
    var input3_arr = Array.from(document.querySelectorAll('.column3'), (input) => input.value);
    var input4_arr = Array.from(document.querySelectorAll('.column4'), (input) => input.value);
    var input5_arr = Array.from(document.querySelectorAll('.column5'), (input) => input.value);
    var input6_arr = Array.from(document.querySelectorAll('.column6'), (input) => input.value);
    var input7_arr = Array.from(document.querySelectorAll('.column7'), (input) => input.value);
    var input8_arr = Array.from(document.querySelectorAll('.column8'), (input) => input.value);
    var input9_arr = Array.from(document.querySelectorAll('.column9'), (input) => input.value);
    var input10_arr = Array.from(document.querySelectorAll('.column10'), (input) => input.value);

    const data = {
        column1: input1_arr,
        column2: input2_arr,
        column3: input3_arr,
        column4: input4_arr,
        column5: input5_arr,
        column6: input6_arr,
        column7: input7_arr,
        column8: input8_arr,
        column9: input9_arr,
        column10: input10_arr
    };
    console.log("save:",data.column1)
    // console.log("save:",data.column2)
    // console.log("save:",data.column3)

    // 使用 chrome.storage API 保存数据
    chrome.storage.local.set(data, function() {
        console.log('数据已保存');
        alert('数据已保存');
    });
}

// 清空本地所有数据
function deleteData() {
    chrome.storage.local.clear(function() {
        if (chrome.runtime.lastError) {
            console.error('清空数据时发生错误:', chrome.runtime.lastError);
        } else {
            console.log('数据已清空');
            alert('数据已清空!');
            
        }
    });
}

// 清空指定数据
function deleteSpecificData(keysToDelete) {
    chrome.storage.local.remove(keysToDelete, function() {
        if (chrome.runtime.lastError) {
            console.error('清空指定数据时发生错误:', chrome.runtime.lastError);
        } else {
            console.log('指定数据已清空');
            alert('指定数据已清空!');
        }
    });
}

// 示例用法
// 假设你想删除存储中的 'key1' 和 'key2'
// deleteSpecificData(['key1', 'key2']);

// 显示data
// 检索数据的函数
function showData() {
    // 使用 chrome.storage API 检索数据
    chrome.storage.local.get(['column1', 'column2', 'column3','column4','column5','column6','column7','column8','column9','column10'], function(data) {
        // 检查是否成功检索到数据
        if (chrome.runtime.lastError) {
            console.error(chrome.runtime.lastError);
            return;
        }
        console.log('ad_keyword show data.column1:', data.column1);
        console.log('ad_keyword show data.column2:', data.column2);
        const input1_arr = data.column1;
        const input2_arr = data.column2;
        const input3_arr = data.column3;
        const input4_arr = data.column4;
        const input5_arr = data.column5;
        const input6_arr = data.column6;
        const input7_arr = data.column7;
        const input8_arr = data.column8;
        const input9_arr = data.column9;
        const input10_arr = data.column10;

        if(input1_arr){
            if(input1_arr.length>=2){
                const the_td = document.querySelectorAll('tr')[0]
                add_hang_n(numRows=input1_arr.length-2,td=the_td)
            }
        }

        Array.from(document.querySelectorAll('.column1')).forEach((input, index) => {input.value = input1_arr[index]; input.classList.add('text-center');});
        Array.from(document.querySelectorAll('.column2')).forEach((input, index) => {input.value = input2_arr[index]; input.classList.add('text-center');});
        Array.from(document.querySelectorAll('.column3')).forEach((input, index) => {input.value = input3_arr[index]; input.classList.add('text-center');});
        Array.from(document.querySelectorAll('.column4')).forEach((input, index) => {input.value = input4_arr[index]; input.classList.add('text-center');});
        Array.from(document.querySelectorAll('.column5')).forEach((input, index) => {input.value = input5_arr[index]; input.classList.add('text-center');});
        Array.from(document.querySelectorAll('.column6')).forEach((input, index) => {input.value = input6_arr[index]; input.classList.add('text-center');});
        Array.from(document.querySelectorAll('.column7')).forEach((input, index) => {input.value = input7_arr[index]; input.classList.add('text-center');});
        Array.from(document.querySelectorAll('.column8')).forEach((input, index) => {input.value = input8_arr[index]; input.classList.add('text-center');});
        Array.from(document.querySelectorAll('.column9')).forEach((input, index) => {input.value = input9_arr[index]; input.classList.add('text-center');});
        Array.from(document.querySelectorAll('.column10')).forEach((input, index) => {input.value = input10_arr[index]; input.classList.add('text-center');});

        // 获取所有的 td 元素
        const tds = document.querySelectorAll('td');
        // 给每个 td 元素添加右键菜单事件监听器
        Array.from(tds).forEach(td => {
            addContextMenuListener(td);
        })
    });
}

// 给每个 td 元素添加  右键菜单  事件监听器的函数
function addContextMenuListener(td) {
    td.addEventListener('contextmenu', function(event) {
        event.preventDefault(); // 阻止默认的右键菜单弹出
        // 添加您的右键菜单逻辑
        add_odd_hang(td)
    });
    // add_odd_hang(td);

}

// 指定创建几行数据
function add_hang_n(numRows,td){
    /*
    numRows  这个是要添加几行
    td       这个是添加到那个后面
    */
    // const numRows = 5; // 指定要创建的行数
    for (let i = 0; i < numRows; i++) {
        const newRow = document.createElement('tr');
        var td1 = document.createElement('td');
        var td2 = document.createElement('td');
        var td3 = document.createElement('td');
        var td4 = document.createElement('td');
        var td5 = document.createElement('td');
        var td6 = document.createElement('td');
        var td7 = document.createElement('td');
        var td8 = document.createElement('td');
        var td9 = document.createElement('td');
        var td10 = document.createElement('td');

        input1 = document.createElement('input');
        input1.setAttribute("type","text");
        input1.setAttribute("class","column1");
        input1.setAttribute("value","");

        input2 = document.createElement('input');
        input2.setAttribute("type","text");
        input2.setAttribute("class","column2");
        input2.setAttribute("value","");

        input3 = document.createElement('input');
        input3.setAttribute("type","text");
        input3.setAttribute("class","column3");
        input3.setAttribute("value","");

        input4 = document.createElement('input');
        input4.setAttribute("type","text");
        input4.setAttribute("class","column4");
        input4.setAttribute("value","");

        input5 = document.createElement('input');
        input5.setAttribute("type","text");
        input5.setAttribute("class","column5");
        input5.setAttribute("value","");

        input6 = document.createElement('input');
        input6.setAttribute("type","text");
        input6.setAttribute("class","column6");
        input6.setAttribute("value","");

        input7 = document.createElement('input');
        input7.setAttribute("type","text");
        input7.setAttribute("class","column7");
        input7.setAttribute("value","");

        input8 = document.createElement('input');
        input8.setAttribute("type","text");
        input8.setAttribute("class","column8");
        input8.setAttribute("value","");

        input9 = document.createElement('input');
        input9.setAttribute("type","text");
        input9.setAttribute("class","column9");
        input9.setAttribute("value","");

        input10 = document.createElement('input');
        input10.setAttribute("type","text");
        input10.setAttribute("class","column10");
        input10.setAttribute("value","");

        td1.appendChild(input1)
        td2.appendChild(input2)
        td3.appendChild(input3)
        td4.appendChild(input4)
        td5.appendChild(input5)
        td6.appendChild(input6)
        td7.appendChild(input7)
        td8.appendChild(input8)
        td9.appendChild(input9)
        td10.appendChild(input10)

        // 将三个 <td> 元素添加到 <tr> 元素中
        newRow.appendChild(td1);
        newRow.appendChild(td2);
        newRow.appendChild(td3);
        newRow.appendChild(td4);
        newRow.appendChild(td5);
        newRow.appendChild(td6);
        newRow.appendChild(td7);
        newRow.appendChild(td8);
        newRow.appendChild(td9);
        newRow.appendChild(td10);
        td.parentNode.parentNode.appendChild(newRow);
    }
}

// 创建和删除新行
function add_odd_hang(td) {
    // 删除老菜单
    const menus = document.querySelectorAll('ul');

    if (menus.length > 0) {
        menus[0].remove();
    }

    td.addEventListener('contextmenu', function(event) {
        event.preventDefault(); // 阻止默认的右键菜单弹出
    });

    // 创建新菜单
    const menu = document.createElement('ul');
    menu.innerHTML = `
      <li id="addRow">末尾增加一行</li>
      <li id="deleteRow">删除当前行</li>
    `;

    // menu 菜单建立之前判断一下 页面中有没有menu，没有的话才建立，有的话就忽略此次右键

    // 设置菜单的位置
    menu.style.position = 'absolute';
    menu.style.left = event.pageX - 30 + 'px';
    menu.style.top = event.pageY - 15 + 'px';
    console.log("event.pageX:", event.pageX)
    console.log("event.pageY:", event.pageY)
    // 将菜单添加到页面中
    document.body.appendChild(menu);


    // 定义菜单项的点击事件处理逻辑
    const addRow = menu.querySelector('#addRow');
    addRow.addEventListener('click', function() {
        menu.remove()
        // 在当前行的末尾增加一列
        const newRow = document.createElement('tr');
        var td1 = document.createElement('td');
        var td2 = document.createElement('td');
        var td3 = document.createElement('td');
        var td4 = document.createElement('td');
        var td5 = document.createElement('td');
        var td6 = document.createElement('td');
        var td7 = document.createElement('td');
        var td8 = document.createElement('td');
        var td9 = document.createElement('td');
        var td10 = document.createElement('td');

        input1 = document.createElement('input');
        input1.setAttribute("type","text");
        input1.setAttribute("class","column1");
        input1.setAttribute("value","");

        input2 = document.createElement('input');
        input2.setAttribute("type","text");
        input2.setAttribute("class","column2");
        input2.setAttribute("value","");

        input3 = document.createElement('input');
        input3.setAttribute("type","text");
        input3.setAttribute("class","column3");
        input3.setAttribute("value","");

        input4 = document.createElement('input');
        input4.setAttribute("type","text");
        input4.setAttribute("class","column4");
        input4.setAttribute("value","");

        input5 = document.createElement('input');
        input5.setAttribute("type","text");
        input5.setAttribute("class","column5");
        input5.setAttribute("value","");

        input6 = document.createElement('input');
        input6.setAttribute("type","text");
        input6.setAttribute("class","column6");
        input6.setAttribute("value","");

        input7 = document.createElement('input');
        input7.setAttribute("type","text");
        input7.setAttribute("class","column7");
        input7.setAttribute("value","");

        input8 = document.createElement('input');
        input8.setAttribute("type","text");
        input8.setAttribute("class","column8");
        input8.setAttribute("value","");

        input9 = document.createElement('input');
        input9.setAttribute("type","text");
        input9.setAttribute("class","column9");
        input9.setAttribute("value","");

        input10 = document.createElement('input');
        input10.setAttribute("type","text");
        input10.setAttribute("class","column10");
        input10.setAttribute("value","");

        td1.appendChild(input1);
        td2.appendChild(input2);
        td3.appendChild(input3);
        td4.appendChild(input4)
        td5.appendChild(input5)
        td6.appendChild(input6)
        td7.appendChild(input7)
        td8.appendChild(input8)
        td9.appendChild(input9)
        td10.appendChild(input10)

        // 将三个 <td> 元素添加到 <tr> 元素中
        newRow.appendChild(td1);
        newRow.appendChild(td2);
        newRow.appendChild(td3);
        newRow.appendChild(td4);
        newRow.appendChild(td5);
        newRow.appendChild(td6);
        newRow.appendChild(td7);
        newRow.appendChild(td8);
        newRow.appendChild(td9);
        newRow.appendChild(td10);
        td.parentNode.parentNode.appendChild(newRow);

        // 虽然已经新加了 元素 但是新加的元素并没有监听事件
        newRow.querySelectorAll('td').forEach(td => {addContextMenuListener(td);});
    });

    const deleteRow = menu.querySelector('#deleteRow');
    deleteRow.addEventListener('click', function() {
        // 删除当前行
        menu.remove()
        td.parentNode.remove();
        // 虽然已经新加了 元素 但是新加的元素并没有监听事件
    });

    // 当菜单创建出来了
    // 如果鼠标点击的地方不是id="addRow"或者id="deleteRow"  就移除ul菜单
    // 将菜单添加到文档中
    // document.body.appendChild(menu);

    // 点击事件监听器
    document.addEventListener('click', function(event) {
        const target = event.target;
        const isAddRow = target.id === 'addRow';
        const isDeleteRow = target.id === 'deleteRow';

        if (!isAddRow && !isDeleteRow) {
            // 如果点击的不是 addRow 或 deleteRow，则移除菜单
            menu.remove();
        }
    });
}
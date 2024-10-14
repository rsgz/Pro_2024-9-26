

v = "myshopify_tianjia_kucun_xuhao"
url = "https://b08-admin.shop6888.com/#/goods/goodsManagement"
des = "添加库存序号"

popup_html = r"""↓↓↓↓↓↓↓ popup.html ↓↓↓↓↓↓↓
<span class="a" target="_blank" id="{}">{}</span>|
""".format(v,des)

content_js = r"""↓↓↓↓↓↓↓ content.js ↓↓↓↓↓↓↓
if(request.{}==="{}"){{
            console.log("request.{}");
            async function f1() {{
                try {{
                    $("input[value='  Generate  ']").click();
                    await delay(300);
                    $x_span_city = $("p:contains('City, State, Zip: ')").find('span').text();
                    console.log("$x_span_city:", $x_span_city);

                    $x_span_street = $("p:contains('Street: ')").find('span').text();
                    console.log("$x_span_street:", $x_span_street);

                    $x_span_country = $("p:contains('Country: ')").find('span').text();
                    console.log("$x_span_country:", $x_span_country);

                    $x_span_telephone = $("p:contains('Telephone: ')").find('span').text();
                    console.log("$x_span_telephone:", "+1 "+$x_span_telephone);
                    
                    const txt1 = $x_span_city.trim()+','+$x_span_street.trim()+','+$x_span_country.trim()+';'+'+1 '+$x_span_telephone;
                    copyTextToClipboard(txt1);

                }} catch (error) {{
                    console.error("出现错误:", error);
                }}
            }}

            f1();
        }}
""".format(v,v,v)


popup_js = r"""↓↓↓↓↓↓↓ popup.js ↓↓↓↓↓↓↓
// 沟通 ---> content.js
$("#{}").click(()=>{{send_to_content(message={{{}:"{}"}})}});  // {} ---> {}

// 沟通 --->service-worker.js
$("#{}").click(()=>{{chrome.runtime.sendMessage({{{}:"{}"}});}});  // {} ---> {}
""".format(v,v,v,v,"content.js",v,v,v,v,"service-worker.js")

service_worker_js = r"""↓↓↓↓↓↓↓ service-worker.js ↓↓↓↓↓↓↓
    // {}
    if(request.{}==="{}"){{
        chrome.tabs.create({{ url: '{}' }});
        console.log('进入{}')
    }}
""".format(v,v,v,url,url)

print(popup_html)
print(content_js)
print(popup_js)

print(service_worker_js)
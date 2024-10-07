// =============================== 亚马逊脚本 ===============================
/*
 亚马逊比较变态 链接需要预加载才行
*/

delay_time = 600
function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

get_pics=async ()=>{
    // 每个右边图片需要点击切换
    // span[id^='color_name_'] input[name]
    var pic_l=[]
    kuans = Array.from(document.querySelectorAll("span[id^='color_name_'] input[name]"))
    if(kuans.length===0){
        pics = Array.from(document.querySelectorAll("li[data-csa-c-posy] input"))
        console.log("pics:",pics)
        for(pic of pics){
            console.log("pic:",pic)
            try{
                if(!pic.src.includes('thumb')){
                    // 下载每个居中大图
                    // div#imgTagWrapperId.imgTagWrapper img
                    await delay(ms=delay_time)
                    // 创建一个新的鼠标点击事件
                    var clickEvent = new MouseEvent('click', {
                        view: window,
                        bubbles: true,
                        cancelable: true
                    });

                    // 触发点击事件
                    pic.dispatchEvent(clickEvent);
                    pic.click()
                    // img = document.querySelector("div#imgTagWrapperId.imgTagWrapper img")
                    // img = document.querySelector("li.image.item.itemNo0.maintain-height.selected img.a-dynamic-image")
                    // img = document.querySelector("li.image.item.itemNo4.maintain-height.selected div.imgTagWrapper img.a-dynamic-image")
                    imgs = Array.from(document.querySelectorAll("div.imgTagWrapper img.a-dynamic-image"))
                    console.log("imgs:", imgs)
                    imgs_src = imgs.map(img=>img.src);
                    console.log("img√√√√√√:",...imgs_src)
                    pic_l.push(...imgs_src)
                }
            }catch(e){}
        }
    }
    else{
        for(ele of kuans){
            await delay(ms=delay_time)
            ele.click()
            // 每个input 需要点击切换  src 中 去除掉包含这个的thumb  这是视频
            // li[data-csa-c-posy] input
            pics = Array.from(document.querySelectorAll("li[data-csa-c-posy] input"))
            console.log("pics:",pics)
            for(pic of pics){
                console.log("pic:",pic)
                try{
                    if(!pic.src.includes('thumb')){
                        // 下载每个居中大图
                        // div#imgTagWrapperId.imgTagWrapper img
                        await delay(ms=delay_time)
                        // 创建一个新的鼠标点击事件
                        var clickEvent = new MouseEvent('click', {
                            view: window,
                            bubbles: true,
                            cancelable: true
                        });

                        // 触发点击事件
                        pic.dispatchEvent(clickEvent);
                        pic.click()
                        // img = document.querySelector("div#imgTagWrapperId.imgTagWrapper img")
                        // img = document.querySelector("li.image.item.itemNo0.maintain-height.selected img.a-dynamic-image")
                        // img = document.querySelector("li.image.item.itemNo4.maintain-height.selected div.imgTagWrapper img.a-dynamic-image")
                        imgs = Array.from(document.querySelectorAll("div.imgTagWrapper img.a-dynamic-image"))
                        console.log("imgs:", imgs)
                        imgs_src = imgs.map(img=>img.src);
                        console.log("img√√√√√√:",...imgs_src)
                        pic_l.push(...imgs_src)
                    }
                }catch(e){}
            }
        }
    }

    pic_l2 = [...new Set(pic_l)]
    for(e of pic_l2){
        console.log("drag:", e)
    }
    return pic_l2
}

picss = await get_pics()
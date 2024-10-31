var chatgptdemo_url = "https://chat.chatgptdemo.net"

if (window.location.href.startsWith(chatgptdemo_url)) {
    console.log("chatgptdemo.js 被加载")

    var chatgptdemo = (chatgptdemo_url)=>{
        // ======================================== chatgptdemo ========================================
        // chatgptdemo 操作
        if (window.location.href.startsWith(chatgptdemo_url)) {
            // 下面是预加载(网页一加载就执行的默认操作)
            var intervalId = setInterval(myFunction, 3000); // 每隔3秒钟执行一次
            function myFunction() {
                try {
                    // 在这里写你的代码逻辑
                    var ad = document.querySelectorAll("div#ADS-block-detect")[0];
                    console.log("ad:", ad);
                    ad.style.display = "none";
                    console.log("display:",ad.style.display);
                    console.log("-------------------------------------------")
                } catch (error) {
                    console.error("出现错误:", error);
                }

                // 检查是否已经执行了1分钟
                if (new Date() - startTime >= 30000) {
                    clearInterval(intervalId); // 停止定时器
                }
            }
            var startTime = new Date(); // 记录开始执行的时间
        }
    }
}
function click_all2() {
    console.log("1 勾选目标----------->")
    document.querySelectorAll("div.CBX_hasCheckSquare_5-72-0")[1]?.click();
    setTimeout(() => {
        console.log("2 加入发货台")
        document.querySelectorAll("div[class^=shipping-desk]>button[data-tracking-id]>span")[0]?.click();
        console.log("3 确认")
        setTimeout(() => {
            document.querySelectorAll("div[class^=body-module]>div[class^=body-module] button[class^=BTN_outerWrapper]>span")[0]?.click()
            setTimeout(() => {
                console.log("4 确认加入")
                document.querySelectorAll("div[class^=shipping-desk] div[class^=shipping-desk]>button[class^=BTN_outerWrapper]")[0]?.click()
                setTimeout(() => {
                    console.log("5 确认")
                    document.querySelector('div[data-testid="beast-core-portal-main"] button')?.click();
                    setTimeout(() => {
                        console.log("6 回到第二栏")
                        Array.from(document.querySelectorAll('a[data-ddmc-shell-cid="bg-shell-menu"]>div>div>div')).filter(v => v.textContent.includes('发货台'))[0]?.click();
                    }, 1000);
                }, 500);
            }, 1000);
        }, 500);
    }, 500);
}

intervalId = setInterval(click_all2, 10000);
document.addEventListener('keydown', function(event) {
    if (event.key === 's') {
        clearInterval(intervalId);
        console.log('已停止');
    }
});
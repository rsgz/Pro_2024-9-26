function run() {
    function t(t) {
        return new Promise(e => setTimeout(e, t))
    }

    let e = [],
        l = [],
        n = document.querySelector('tbody[data-testid="beast-core-table-middle-tbody"]').querySelectorAll("a");
    for (let t = 0; t < n.length; t++) "加入发货台" !== n[t].innerText || [...n[t].classList].includes("BTN_disabled_5-52-0") || e.push(n[t]);
    (async function () {
        for (let n = 0; n < e.length; n++) if (e[n].click(), l = document.querySelectorAll('div[data-testid="beast-core-portal"]'), n == e.length - 1) for (let e = 0; e < l.length; e++) await t(shiyanr()), l[e].querySelector("button").click()
    })(), 0 === e.length && (alert("没找到可用的加入发货台订单"), clearInterval(_MyInterval), _MyInterval = null, $(".apivStockv3").html("<span>暴力<SUP>+100</SUP>抢库</span>"))
}
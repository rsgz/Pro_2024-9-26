    //控制开关，规则->是否开启替换请求URL参数
    public static RulesOption("是否开启替换请求URL参数")
    BindPref("fiddlerscript.rules.isURL")
    var m_isURL: boolean = false;

    // 修改  来自于掘金
    static function OnBeforeRequest(oSession: Session) {
        // Sample Rule: Color ASPX requests in RED
        // if (oSession.uriContains(".aspx")) {	oSession["ui-color"] = "red";	}

        // Sample Rule: Flag POSTs to fiddler2.com in italics
        // if (oSession.HostnameIs("www.fiddler2.com") && oSession.HTTPMethodIs("POST")) {	oSession["ui-italic"] = "yup";	}

        // Sample Rule: Break requests for URLs containing "/sandbox/"
        // if (oSession.uriContains("/sandbox/")) {
        //     oSession.oFlags["x-breakrequest"] = "yup";	// Existence of the x-breakrequest flag creates a breakpoint; the "yup" value is unimportant.
        // }
        
        
        /*
        例1
        //添加颜色
        if (oSession.HostnameIs("www.zhaokeli.com")) {
            oSession["ui-color"] = "red";
        }
        //把指定主机重定向到另一个主机,并且把请求url给替换下
        if (oSession.HostnameIs("s29.xxxx.cn")||oSession.HostnameIs("s29.xxxx.cn")) {
        oSession.hostname="test.xxxxx.cn";
        oSession.url = oSession.url.Replace("/static/study_h5","");
        oSession.url = oSession.url.Replace("/static/common/js","");
        }
        */
        
        /*
        例2
        // 删除所有的cookie
        oSession.oRequest.headers.Remove("Cookie");
        // 新建新的cookie
        oSession.oRequest.headers.Add("Cookie", "uuid=asdfasdfasdf;key=asdfasdf");
        //修改来源地址
        if (oSession.uriContains("www.xxxx.com")) {       
        oSession.oRequest["Referer"] = "www.xxxx.com"
        }
        //添加随机值强制刷新缓存
        if (oSession.uriContains("s29.9956.cn/static/study_h5")) {
        oSession.url = oSession.url+ "?"+ Math.random()*1000000;
        }
        */
        
        /*
        例3
        //如果url里包含username并且请求头里包含cookie的话就修改cookie
        if(oSession.uriContains('username') &&oSession.oRequest.headers.Contains("Cookie")){
        //取出cookie字符串
        var sCookie = oSession.oRequest["Cookie"];
        //用replace方法或者正则表达式的方法去操作cookie的string
        sCookie = sCookie.Replace("strname", "replacename");
        //设置cookie
        oSession.oRequest["Cookie"] = sCookie;
        }
        */
        
        /*
        
        */
        
        // 替换链接请求  替换请求
        if(m_isURL){
            //这里一般填写Host+?前面的的内容，因为?后面的内容容易变动
            //这里由于问题中的人说会变动，那么我们就直接写host
            if(oSession.fullUrl.Contains("www.fiddler66666.com")){
                try{
                    //问题中是把M6替换，那你就把UpdateCheck替换成M6，而52pojie替换成想替换的字符串
                    oSession.fullUrl = oSession.fullUrl.Replace("UpdateCheck","52pojie")
                }catch(err){
                    FiddlerObject.log("出现异常，错误原因:"+err)
                }
            }
        }
        
        // 检查是否开启了替换功能
        if (m_isURL) {
            // 检查请求的Content-Type是否为application/json
            if (oSession.oRequest["Content-Type"].indexOf("application/json") >= 0&&oSession.fullUrl.Contains("b08-api.shop6888.com/apis/Action")) {
                try {
                    // 获取请求体
                    var requestBody = oSession.GetRequestBodyAsString(); 
                    // 解析 JSON
                    var jsonStr = Fiddler.WebFormats.JSON.JsonDecode(requestBody);
                    // 解析JSON
                    // {"action":"goods.search","data":{"pageIndex":1,"pageSize":20,"keywords":" hat"}}
                    // 修改pageSize值
                    if (jsonStr.JSONObject["action"] === "goods.search") {
                        jsonStr.JSONObject["data"]["pageSize"]= 2000; // 设置新的pageSize值
                    }
                    // 重新序列化JSON
                    var mod_json = Fiddler.WebFormats.JSON.JsonEncode(jsonStr.JSONObject); //封装修改后的JSON，如果需要改变的是Body内容，则不需要封装JSON这步
                    oSession.utilSetRequestBody(mod_json); //将封装后的JSON放入Response中

                } catch (err) {
                    // 如果出现异常，记录到Fiddler的日志中
                    FiddlerObject.log("出现异常，错误原因: " + err);
                }
            }
        }
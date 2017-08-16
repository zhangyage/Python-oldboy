var code = getQueryString("code");

/**
 * 微信获取用户信息
 */
var getWX = {
		init : function(){
//			this.url = window.location.href.replace("wxshare=1",""),
			this.url = window.location.href;
			this.isGetWeiXinUserInfo();
		},
		/**
		 * 获取微信oauth2.0极权地址
		 * @param url{当前网页地址}
		 * @returns
		 */
		getUrl : function (url){
			$.ajax({
				url: path + "/user/getAuthCodeUrl.html",
				type: "post",
				dataType: "json",
				async:false,
				data:{
					"url": url
				},
				success: function(data){
					if(data["url"]){
						window.location.href = data["url"];
					}
				},
				error:function(){
					console.log("获取oauth授权地址异常");
				}
			});
		},
		
		/**
		 * 获取微信Token
		 * @returns
		 */
		getToken : function (){
			//alert("进入getToken");
			var _url ;
			//alert("111111111111111");
			if(this.url){
				_url = this.url.replace("wxshare=1","");//去掉获取微信用户信息标记				
			}else{
				//_url = path + "/common/login.html";
				_url = path + "/common/index.html";
			}
			console.log("openId=="+openId);
			if(openId!=null && openId!="" && typeof(openId)!="undefined"){
				_url = path + "/common/index.html";

			}
			$.ajax({
				url: path + "/user/saveAccessToken.html",
				type: "post",
				dataType: "json",
				async:false,
				data: {
					"code" :code
				},
				success: function(data){
					console.log(data);
					if(data["success"]){
						if(data["loginSuccess"]){
							//alert(data["loginSuccess"]);
							if(data["msg"]["identityType"]=='parent'){
								window.location.href = path + "/common/p_index.html";
							}else{
								window.location.href = path + "/common/t_index.html";
							}
						}else{
/*							openId=data["msg"]["openid"];
							alert(openId);*/
							//alert("00000000000000000");
							//window.location.href = _url;
						}
					}else{
						//alert("11111111111111111___"+data["msg"]+"_______"+data["msg"].length);
						AlertDialog.tip(data["msg"],"login");
/*						if(data["msg"].length>0){
							AlertDialog.tip(data["msg"]);
							alert("---------------");
						}else{
							alert("================");
							window.location.href = _url+"?code="+code;	
						}*/
					}
					
				},
				error:function(){
					console.log("微信获取token异常！")
				}
			});
		},
		
		/**
		 * 是否执行获取微信用户信息
		 */
		isGetWeiXinUserInfo : function (){
			var ua = window.navigator.userAgent.toLowerCase();
			if(ua.match(/MicroMessenger/i) == 'micromessenger'){
				if(code){
					this.getToken();
				}else{
					this.getUrl(this.url.split("#")[0]);
				}
			}
		}
};



//test start
//$(function(){
//	if(code){
//		getWX.getToken();
//	 }
//	$("#loginBtn").unbind("click").click(subLogin);
//});
////登录
//function subLogin(){
///*	if(MValify.loginPhone($("#mobile").val(), "mobile")){
//
//		if(MValify.isNull($("#password").val(), "password", 0, 150)){*/
//			//alert($("#userId").val()+"__________"+$("#password").val());
//		if(openId.length==0){
//			AlertDialog.mtip("openId不能为空");
//		}else{
//			$("#loginBtn").unbind("click").css("background", "#CCC").text("提交中...");
//			$.ajax({
//				url: path + "/user/loginByWeiXin.html",
//				type: "post",
//				dataType: "json",
//				data: {
//						"userId": $("#userId").val(),
//						"password": $("#password").val(),
//						//"valiCode": $("#valiCode").val(),
//						"wapFlag":"0",
//						"openId":openId
//				},
//				success: function(data){
//					if(data["msg"] == "success"){
//						var url = window.localStorage.getItem("goBack");
//						window.localStorage.removeItem("goBack");
//						if(url){
//							window.location.href = url;
//						}else{
//							window.location.href = path + "/common/m-personalCenter.html";
//						}
//					}else{
//						$("#loginBtn").click(subLogin).css("background", "#00a0e6").text("登录");
//						AlertDialog.mtip(data["msg"]);
//					}
//				},
//				error: function(request){
//					console.log("登录异常");
//				}
//			});
//		}
///*		}
//	}*/
//}
//test end

/**
 * 抽奖
 */
var luckDraw = {
		/**
		 * 初始化
		 * @param id{事件绑定ID}
		 */
		init : function (id){
			var _this = this;
			if($("._luckDraw_yhbDiv").length == 0){
				_this.addHtml();//添加页面需要的html元素				
			}
			$("#" + id).unbind("click").click(function(){
				_this.everydayLuckDraw();
			});
		},
		/**
		 * 每天抽奖
		 */
		everydayLuckDraw : function(){
			var _this = this;
			var t,l;
			//检查今天可否抽奖
			$.ajax({
				url: path + "/draw/canDraw.html",
				type: "post",
				dataType: "json",
				async:false,
				success: function(data){
					if(data["success"] == true && data["msg"] > 0){//可抽奖
						$("#luckDrawBgpop").fadeIn(1000);
						$("._luckDraw_yhbDiv").fadeIn(1000,"",function(){
							var obj = $(".drawBtn");
							$("#drawBtn").text("点击抽奖");
							t = ($("._luckDraw_yhbDiv").height() - obj.height())/2;
							l = ($("._luckDraw_yhbDiv").width() - obj.width())/2;
							obj.css({"top":t + "px","left":l + "px"}).fadeIn(1000,function(){
								$("#drawBtn").unbind().click(function(){
									$("#drawBtn").unbind("click").text("抽奖中...");
									_this.lockDraw();
								});
							});
							//关闭抽奖
							$("._luckDraw_yhbDiv a.close").unbind().click(function(){
								$("#noticePanel").animate({
									top:"-155px"
								},1000,function(){
									$("._luckDraw_yhbDiv").fadeOut(1000);
									$("#luckDrawBgpop").fadeOut(1000);
									$(".drawBtn").fadeOut(1000,function(){
										$(this).text("");
									});
								});
							});
						});
					}else{
						$("#luckDrawBgpop").fadeIn(1000);
						$("._luckDraw_yhbDiv").fadeIn(1000,"",function(){
							$("#noticePanel div.div1").html("诶哟，抽奖机会用完了啦<br/>投资1000元可再抽奖一次！");
							$("#noticePanel div.div2").text("立即投资").unbind().click(function(){
								window.location.href = path + "/common/loanList.html";
							});
							$("#noticePanel").animate({
								top:"40%"
							},1000);
							//关闭抽奖
							$("._luckDraw_yhbDiv a.close").unbind().click(function(){
								$("#noticePanel").animate({
									top:"-155px"
								},1000,function(){
									$("._luckDraw_yhbDiv").fadeOut(1000);
									$("#luckDrawBgpop").fadeOut(1000);
								});
							});
						});
					}
				},
				error: function(){
					console.log("判断是否可以摇奖异常");
				}
			});
		},
		
		/**
		 * 抽奖
		 */
		lockDraw : function(){
			$.ajax({
				url: path + "/draw/userDraw.html",
				type: "post",
				dataType: "json",
				async:false,
				success: function(data){
					$("#drawBtnBg").fadeOut(1000);
					$("#drawBtn").fadeOut(1000,function(){
						if(data["success"]){
							$("#prize").html("恭喜您摇出<br/>"+data["msg"]["prizeName"]);
							$("#noticePanel div.div1").html("恭喜您摇到<br/>"+data["msg"]["prizeName"]);
							if(data["msg"]["leftCount"] > 0){
								$("#noticePanel div.div2").text("你还有抽奖机会，点击抽奖").unbind("click").click(function(){
									$(this).unbind("click");
									$("#noticePanel").animate({
										top:"-155px"
									},1000,function(){
										$("#drawBtnBg").fadeIn(1000);
										$("#drawBtn").text("抽奖中...").fadeIn(1000,function(){
											lockDraw();
										});
									});
								});
							}else{
								$("#noticePanel div.div2").text("立即投资").unbind().click(function(){
									window.location.href = path + "/common/loanList.html";
								});
							}
							$("#noticePanel").animate({
								top:"40%"
							},1000);
						}else{
							AlertDialog.tip(data["msg"]);
							$("#noticePanel").animate({
								top:"-155px"
							},1000,function(){
								$("._luckDraw_yhbDiv").fadeOut(1000);
								$("#luckDrawBgpop").fadeOut(1000);
							});
						}
					});
				},
				error: function(){
					console.log("获取注册跳转信息异常");
				}
			}); 
		},
		
		//页面需要用到的HTML
		addHtml : function(){
			var html  = [];
			html.push('<div class="_luckDraw_yhbDiv">');
			html.push('<a class="close" href="javascript:void(0);"></a>');
			html.push('<div id="noticePanel" class="notice">');
			html.push('<div class="div1">');
			html.push('</div>');
			html.push('<div class="div2">');
			html.push('</div>');
			html.push('</div>');
			html.push('<div id="drawBtnBg" class="drawBtn drawBtnBg"></div>');
			html.push('<div id="drawBtn" class="drawBtn"></div>');
			html.push('</div>');
			html.push('<div id="luckDrawBgpop" class="luckDraw_bgpop"></div>');
			$("body").append(html.join(""));
		}
};
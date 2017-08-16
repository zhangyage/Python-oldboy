/**
 * 公共方法
 */
//登录注册提示效果方法
var InputTip = {
	"blurTip": function(id){
		$("#" + id).prev("div").fadeOut().animate({
			marginTop: "-20px"
		},300);
	},
	"focusTip": function(id){
		$("#" + id).prev("div").show().animate({
			marginTop: "10px"
		},300);
	}
};
/**
 * 
 * @param id 获取城市的的省份id
 * @returns {Array} 返回包含省份/城市的name id
 */
function getPro_citys(id){
	var url = id ? "/area/getCity.html" : "/area/getProvince.html";
	var data = id ? {"pid": id} : {};
	var proviceData = [];
	$.ajax({
		url: path + url,
		type: "post",
		dataType: "json",
		data: data,
		async: false,
		success: function(data){
			if(data["success"]){
				data = data["msg"]["rows"], dlength = data.length;
				for(var i=0;i<dlength;i++){
					proviceData.push([data[i]["shortName"], data[i]["id"], data[i]["name"]]);
				}
			}
		},
		error: function(request, status, err){
			console.log("获取省份信息异常");
		}
	});
	return proviceData;
}
/**
 * type: 如果不传值，val为false返回 --
 * type: 如果传0 ，val为false返回0
 * type: 如果传0.0，val为false返回0.0
 * @param val 传入的判断是否存在的值
 */
function null2value(val,type){
	val = type ? (type=="0.0" ? val.toFixed(2) : (val ? val : 0)) : (val ? val : "--");
	return val;
}
//排序显示方法
$.fn.sortList = function(data){
	//上移动态添加数据
	var listStr = '',listArr = [], l = data["text"].length, id = $(this).attr("id");
	$(this).mouseover(function(){
		if($(this).find("div.sortd").length > 0){
			$(this).find("div.sortd").show();
			return false;
		}
		listArr.push('<div class="sortd">');
		for(var i=0;i<l;i++){
			listArr.push('<span class="sorts" sf="'+data["sort"][i]+'">'+data["text"][i]+'</span>');
		}
		listArr.push('</div>');
		listStr = listArr.join("");
		$(this).append($(listStr));
		$(this).find("span").click(function(){
			$("#" + id).children("a").text($(this).text()).attr("sf",$(this).attr("sf"));
			$("#" + id).siblings().removeClass("cur");
			$("#" + id).addClass("cur");
			$(this).parent().hide();
			if(data["callback"]){
				data["callback"](1);
			}
		});
	}).mouseout(function(){
		$(this).find("div.sortd").hide();
	});
};
//公共提示框
var AlertDialog = {
		show: function(text, id, t, l,zindex){
			var thisT = $("#" + id).offset().top-$("#" + id).height()-t, thisL = $("#" + id).offset().left+$("#" + id).width()-l;
			var alertStr = '';
			var zstyle= zindex ? 'style="z-index:'+zindex+'"':"";
			alertStr = '<div id="tip_div" class="tip_div" '+zstyle+'>' + 
						'<span class="tip_z tip_jz">◆</span>' + 
						'<div>'+text+'</div>' + 
						'</div>';
			$("#tip_div").remove();
			$("body").append($(alertStr));
			$("#tip_div").css({"left":thisL+"px","top":thisT+"px"});
			$("#tip_div").show("slow");
		},
		hide: function(){
			$("#tip_div").hide("slow");
		},
		tip: function(content,login){
			$(".bgpop[id!='bigCover']").show();
			var alertStr = '<div class="com_div">' + 
							 '<div class="com_tit">提示<span class="com_close" id="comClse">×</span></div>' + 
							 '<div class="com_content">'+content+'</div>' + 
							 '<div class="com_btn"><span class="s" id="alertSure">确定</span></div>';
							 '</div>' ;
			$("body").append($(alertStr));
			var al = (cv["winW"]-$(".com_div").width())/2, at = (cv["winH"]-$(".com_div").height())/2;
			$(".com_div").show().css({"left":al+"px", "top":at+"px"});
			var tOut = 0;
			clearTimeout(tOut);
			if(login == "login"){
//				alert()
				$("#alertSure").click(function(){
					clearTimeout(tOut);
					$(".bgpop").hide();
					$(".com_div").remove();
				});
				$("#comClse").click(function(){
					clearTimeout(tOut);
					$(".bgpop").hide();
					$(".com_div").remove();
				});
			}else{
				tOut = setTimeout(function(){
					$(".bgpop").hide();
					$(".com_div").remove();
					window.location.reload();
				},2000);
				$("#alertSure").click(function(){
					clearTimeout(tOut);
					$(".bgpop").hide();
					$(".com_div").remove();
					window.location.reload();
				});
				$("#comClse").click(function(){
					clearTimeout(tOut);
					$(".bgpop").hide();
					$(".com_div").remove();
					window.location.reload();
				});
			}
//				tOut = setTimeout(function(){
//					$(".bgpop").hide();
//					$(".com_div").remove();
//					window.location.reload();
//				},2000);
//				$("#alertSure").click(function(){
//					clearTimeout(tOut);
//					$(".bgpop").hide();
//					$(".com_div").remove();
//					window.location.reload();
//				});
//				$("#comClse").click(function(){
//					clearTimeout(tOut);
//					$(".bgpop").hide();
//					$(".com_div").remove();
//					window.location.reload();
//				});
//			var msg=new alertMsg();
//			if(typeof(fn) === "function"){
//				msg.buttons[0].fun = fn;
//			}
//			msg.content=content;//提示内容
//			msg.show();
			
//			$(".bgpop").show();
//			var alertStr = '<div class="alertTip">' + 
//							'<span class="alertClose"></span>' + 
//							'<p>'+str+'</p>' + 
//							'</div>';
//			$("body").append($(alertStr));
//			var al = (cv["winW"]-$(".alertTip").width())/2, at = (cv["winH"]-$(".alertTip").height())/2;
//			$(".alertTip").show().css({"left":al+"px", "top":at+"px"});
//			var tOut = 0;
//			clearTimeout(tOut);
//			tOut = setTimeout(function(){
//				$(".bgpop,.alertTip").hide();
//			},2000);
//			$(".alertClose").click(function(){
//				clearTimeout(tOut);
//				$(".bgpop,.alertTip").hide();
//			});
		},
		mtip: function(str,sureCallback){
			$(".bgpop").show();
			var alertStr = '<div class="com_div">' + 
							 '<div class="com_tit">提示<span class="com_close" id="comClse">×</span></div>' + 
							 '<div class="com_content">'+str+'</div>' + 
							 '<div class="com_btn"><span class="s" id="alertSure">确定</span></div>';
							 '</div>' ;
			$("body").append($(alertStr));
			var al = (cv["winW"]-$(".com_div").width())/2, at = (cv["winH"]-$(".com_div").height())/2;
			$(".com_div").show().css({"left":al+"px", "top":at+"px"});
			var tOut = 0;
			clearTimeout(tOut);
//			tOut = setTimeout(function(){
//				$(".bgpop").hide();
//				$(".com_div").remove();
//			},2000);
			$("#alertSure").click(function(){
				clearTimeout(tOut);
				sureCallback && sureCallback();
				$(".bgpop").hide();
				$(".com_div").remove();
			});
			$("#comClse").click(function(){
				clearTimeout(tOut);
				$(".bgpop").hide();
				$(".com_div").remove();
			});
		},
		
		/**
		 * confirm弹出框
		 * @param fn1: 传入的确定方法
		 * @param fn2: 传入的取消方法
		 * @param text：传入的文字
		 * @param id： 传入的确定方法的参数
		 */
		confirm: function(fn1, fn2, text, btn1Text, btn2Text, arg, arg1){
			$(".bgpop").show();
			var comStr = '<div class="com_div">' + 
						 '<div class="com_tit">提示<span class="com_close" id="comClse">×</span></div>' + 
						 '<div class="com_content">'+text+'</div>' + 
						 '<div class="com_btn"><span class="s" id="comSure">'+btn1Text+'</span><span class="c" id="comClose">'+btn2Text+'</span></div>';
						 '</div>' ;
			$("body").append($(comStr));
			var al = (cv["winW"]-$(".com_div").width())/2, at = (cv["winH"]-$(".com_div").height())/2;
			$(".com_div").show().css({"left":al+"px", "top":at+"px"});
			//关闭事件
			$("#comClose").click(function(){
				if(fn2){
					fn2();
				}else{
					$(".bgpop").hide();
					$(".com_div").remove();
				}
			});
			//确定事件
			$("#comSure").click(function(){
				if(arg){
					$(".bgpop").hide();
					$(".com_div").remove();
					fn1(arg, arg1);
				}else{
					$(".bgpop").hide();
					$(".com_div").remove();
					fn1();
				}
			});
			$("#comClse").click(function(){
				$(".bgpop").hide();
				$(".com_div").remove();
			});
		}
};
//为项目准备公共值
var cv = {
		winW: $(window).width(),
		winH: $(window).height()
};
//文件服务器地址
var fileAddress = "http://img.zuimeifang.cn/";
//var fileAddress = "http://182.92.153.225/upload/meifajiazu/";
//var fileAddress = "http://image.lingbug.com/upload/youeryuan/";

/*
 * 弹出框专声明
 * content : 提示内容
 * inputId : 错误输入框获取焦点
 */
function _alert(content,inputId){
	var msg=new alertMsg();
	msg.buttons = [];
	msg.content=content;//提示内容
	if(inputId || $("#" + inputId).length > 0){
		msg.input=$("#" + inputId);//错误输入框获取焦点
	}
	msg.show();
}
//添加需要的日期方法
var myDate = {
		year: new Date().getFullYear(),
		month: new Date().getMonth()+1,
		day: new Date().getDate(),
		getLastMonthYestdy: function(){ //获取上个月的今天的日期
			var daysInMonth =  new  Array([0],[31],[28],[31],[30],[31],[30],[31],[31],[30],[31],[30],[31]); 
			var year = this.year, month = this.month, day = this.day;
		    if (year%4 == 0 && year%100 != 0){   
		      daysInMonth[2] = 29;   
		    }   
		    if (month - 1 == 0){   
		    	year -= 1;   
		      month = 12;   
		    }else{   
		    	month -= 1;   
		    }   
		    day = daysInMonth[month] >= day ? day : daysInMonth[month];   
		    if (month<10){     
		    	month= "0" +month;     
		    }   
		    if (day<10){     
		    	day= "0" +day;     
		    }   
		    var datastr = year+ "-" +month+ "-" +day;   
		    return  datastr;  
		},
		getTodayDate: function(){
			var dataStr, month = this.month, day = this.day;
			month = month<10 ? "0"+month : month;
			day = day<10 ? "0"+day : day;
			dataStr = this.year + "-" + month + "-" + day;
			return dataStr;
		}
};


/**
 * 跟据Cookie名字获取值
 * @param c_name
 * @returns String
 */
function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1)
                c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}

/**
* 将数值四舍五入(保留2位小数)后格式化成金额形式
*
* @param num 数值(Number或者String)
* @return 金额格式的字符串,如'1,234,567.45'
* @type String
*/
function formatCurrency(num) {
	num = num ? num : 0;
   num = num.toString().replace(/\$|\,/g,'');
   if(isNaN(num))
   num = "0";
   sign = (num == (num = Math.abs(num)));
   num = Math.floor(num*100+0.50000000001);
   cents = num%100;
   num = Math.floor(num/100).toString();
   if(cents<10)
   cents = "0" + cents;
   for (var i = 0; i < Math.floor((num.length-(1+i))/3); i++)
   num = num.substring(0,num.length-(4*i+3))+','+
   num.substring(num.length-(4*i+3));
   return (((sign)?'':'-') + num + '.' + cents);
//   return (((sign)?'':'-') + num);
}
//根据参数名获取参数
function getQueryString(name) { 
	var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i"); 
	var r = window.location.search.substr(1).match(reg); 
	if (r != null) return unescape(r[2]); return ""; 
}
/**
 * 乘法运算  保留两位小数
 * @param arg1  第一位数
 * @param arg2  第二位数
 * @returns   两位数相乘的结果
 */
function multiplication(arg1,arg2){
	if(!arg1){
		arg1 = 0;
	}
	if(!arg2){
		arg2 = 0;
	}
	function accMul(arg1,arg2) 
	{
		var m=0,s1=arg1.toString(),s2=arg2.toString(); 
		try{m+=s1.split(".")[1].length;}catch(e){} 
		try{m+=s2.split(".")[1].length;}catch(e){}
		return Number(s1.replace(".",""))*Number(s2.replace(".",""))/Math.pow(10,m);
	} 
	//给Number类型增加一个mul方法，调用起来更加方便。 
	Number.prototype.mul = function (arg){ 
		return accMul(arg, this); 
	};
	return accMul(arg1,arg2).toFixed(2);
}
//倒计时
function countDown(time, id, overFn){
	time = Number(time);
	var countTime = setInterval(function(){
		time -= 1;
		$("#" + id).text(time + "s");
		if(time == 0){
			clearInterval(countTime);
			overFn();
		}
	},1000);
}
/*
 * jQuery placeholder, fix for IE6,7,8,9
 * 使IE浏览器支持input输入框的placeholder属性
 */
var JPlaceHolder = {
    //检测
    _check : function(){
        return 'placeholder' in document.createElement('input');
    },
    //初始化
    init : function(){
        if(!this._check()){
            this.fix();
        }
    },
    //修复
    fix : function(){
        jQuery(':input[placeholder]').each(function(index, element) {
            var self = $(this), txt = self.attr('placeholder');
            var pos = self.position(), w = self.outerWidth(true), h = self.outerHeight(true), paddingleft = self.css('padding-left'), f = self.css('float');
            if(self.attr("placType") == "ie"){
            	self.wrap($('<div style="display:inline-block; "></div>').css({position:'relative', zoom:'1', border:'none', background:'none', padding:'none', margin:'none', 'display':'inline', 'line-height':'15px', width:w, float:f}));
            }else{
            	self.wrap($('<div style="display:inline-block;"></div>').css({position:'relative', zoom:'1', border:'none', background:'none', padding:'none', margin:'none', width:w, float:f}));
            }
            var holder = $('<span></span>').text(txt).css({position:'absolute', left:"0px", top:"2px",width:"auto","min-width":"10px", height:h, lienHeight:h, margin:0, paddingLeft:paddingleft, color:'#aaa',"text-align":"left"}).appendTo(self.parent());
            self.focusin(function(e) {
                holder.hide();
            }).focusout(function(e) {
                if(!self.val()){
                    holder.show();
                }
            });
            holder.click(function(e) {
                holder.hide();
                self.focus();
            });
        });
    }
};
//执行
jQuery(function(){
    JPlaceHolder.init();    
});

//替换Js的Array的push方法
Array.prototype.npush = function(html,data){
	if(!data || data.length == 0){
		this.push(html);
	}else{
		for(var i = 0 ; i < data.length;i++){
			var exp = "#"+i;
			if(data[i]){
				html = html.replace(exp,data[i]);
			}else{
				html = html.replace(exp,"--");
			}
		}
		this.push(html);
	}
};

//如果是IOS，进行样式修改
$(function(){
	var iosSource = getQueryString("source");
	var storage = window.localStorage;
	if(iosSource == "ios"){
	 storage.setItem("source",iosSource);
	}
	 if(storage.getItem("source") == "ios"){
		  $("body").css("padding-top","30px");
//		 	$(".indlogo").css("top", "50px");
//			$(".person").css("top", "50px");
//			$(".person_1").css("top", "50px");
//			$(".head").css("height","120px")
//			$(".search_div").css("margin","57px auto");
//			$(".back").css("background-position-y", "33px");
//			$(".head_top").css({"height":"70px","line-height":"80px"});
//			$(".company").css("line-height", "120px");
	 }
});

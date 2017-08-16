function alertMsg(params){
	var _this=this;
	this.buttons=[{title:'确&nbsp;认',css:{},fun:function(){_this.hide();}}]
	if(params!=null){
		if(params.width!=null){
			this.width=params.width;
		}
		if(params.height!=null){
			this.height=params.height;
		}
		if(params.title!=null){
			this.title=params.title;
		}
		if(params.content!=null){
			this.content=params.content;
		}
		if(params.buttons!=null){
			this.buttons=params.buttons;
		}
		if(params.closed!=null){
			this.closed=params.closed;
		}
		if(params.bodyCss!=null){
			this.bodyCss=params.bodyCss;
		}
		if(params.headCss!=null){
			this.headCss=params.headCss;
		}
		
		if(params.iconCss!=null){
			this.iconCss=params.iconCss;
		}
		if(params.bottomCss!=null){
			this.bottomCss=params.bottomCss;
		}
		if(params.closeIcon!=null){
			this.closeIcon=params.closeIcon;
		}
		if(params.input!=null){
			this.input=params.input;
		}
		if(params.msgLevel!=null){
			if(params.msgLevel=="warn"){
				this.icon=path + "/images/warn_min.png";
			}
			if(params.msgLevel=="ok"){
				this.icon=path + "/images/ok_min.png";
			}
			if(params.msgLevel=="error"){
				this.icon=path + "/images/error_min.png";
			}
			
		}
		if(params.icon!=null){
			if(params.icon=="no"){

				this.icon=null;
			}else{
				this.icon=params.icon;	
			}
		}
		if(params.btnPosition!=null){
			this.btnPosition=params.btnPosition;
		}
	}
};



alertMsg.prototype.minimizable=null;
alertMsg.prototype.maximizable=null;
alertMsg.prototype.minCss=null;
alertMsg.prototype.maxCss=null;
alertMsg.prototype.clsCss=null;

alertMsg.prototype.bg=null;
alertMsg.prototype.msg=null;
alertMsg.prototype.msgbg=null;
alertMsg.prototype.head=null;
alertMsg.prototype.body=null;
alertMsg.prototype.bottom=null;
alertMsg.prototype.cache=null;
alertMsg.prototype.msgLevel='warn';
alertMsg.prototype.isInit=false;
alertMsg.prototype.closed=true;
alertMsg.prototype.icon=path + "/images/warn_min.png";
alertMsg.prototype.closeIcon=path + "/images/close_min.png";
alertMsg.prototype.iconCss={};
alertMsg.prototype.bodyCss={};
alertMsg.prototype.headCss={};
alertMsg.prototype.bottomCss={};
alertMsg.prototype.title="温馨提示";
alertMsg.prototype.content="欢迎使用";
alertMsg.prototype.width=400;
alertMsg.prototype.height=210;
alertMsg.prototype.buttons=null;
alertMsg.prototype.input=null;
alertMsg.prototype.btnPosition="center";


alertMsg.prototype.init=function(){
	this.initBg();
	this.initMsg();
};
alertMsg.prototype.setTitle=function(title){
	if(!this.isInit){
		this.title=title;
	}else{
		this.head.find("#alert_title").html(title);
	}
	
	
};
alertMsg.prototype.setParams=function (params){
	var _this=this;
	if(params!=null){
		if(params.width!=null){
			this.width=params.width;
		}
		if(params.height!=null){
			this.height=params.height;
		}
		if(params.title!=null){
			this.title=params.title;
		}
		if(params.content!=null){
			this.content=params.content;
		}
		if(params.buttons!=null){
			this.buttons=params.buttons;
		}
		if(params.closed!=null){
			this.closed=params.closed;
		}
		if(params.bodyCss!=null){
			this.bodyCss=params.bodyCss;
		}
		if(params.headCss!=null){
			this.headCss=params.headCss;
		}
		if(params.iconCss!=null){
			this.iconCss=params.iconCss;
		}
		if(params.bottomCss!=null){
			this.bottomCss=params.bottomCss;
		}
		if(params.closeIcon!=null){
			this.closeIcon=params.closeIcon;
		}
		if(params.msgLevel!=null){
			if(params.msgLevel=="warn"){
				this.icon=path + "/images/warn_min.png";
			}
			if(params.msgLevel=="ok"){
				this.icon=path + "/images/ok_min.png";
			}
			if(params.msgLevel=="error"){
				this.icon=path + "/images/error_min.png";
			}
			
		}
		if(params.icon!=null){
			if(params.icon=="no"){

				this.icon=null;
			}else{
				this.icon=params.icon;
			}
		}
		if(params.btnPosition!=null){
			this.btnPosition=params.btnPosition;
		}
	}
	
	return _this;
};
alertMsg.prototype.initMsg=function(){
	this.msg=$("<div>");
	var msg=this.msg;
	var winw=$(window).width();
	var winh=$(window).height();
	var msgTop=(winh - this.height) / 2;
	var msgLeft=(winw - this.width) / 2;
	msg.css({
		"position": "fixed",
		"z-index": 10003,
		width:this.width,
		height:this.height,
		"background-color":"#ffffff",
		"overflow": "hidden",
		display: "block",
		top:msgTop,
		left:msgLeft,
		"font-family":"微软雅黑"
	});
	var msgHeight=this.height;
	var msgWidth=this.width;
	var isIE6 = !$.support.opacity && !$.support.style && window.XMLHttpRequest==undefined;
	if(isIE6){
		msg.css("position","absolute");
		msg.css("top",($(document).scrollTop()+($(window).height() - msg.height())/2)+"px");
		msg.css("left",msgLeft+"px");
		$(window).scroll(function () {
    		msg.css("top",($(document).scrollTop()+($(window).height() - msg.height())/2)+"px");
    	});
	}
	
	
	
	this.initHead(msg);
	this.initBody(msg);
	this.initBottom(msg);
	
	
	var msg_bg=$("<div>");
	msg_bg.css({
		width:msg.width()+10,
		height:msg.height()+10,
		"position": "fixed",
		"z-index": 10002,
		"background": "#000",
		"filter": "alpha(opacity=20)",
		"opacity": 0.2,
		"-moz-opacity": 0.2,
		top:msgTop-5,
		left:msgLeft-5,
		'border-radius':'5px'
	});
	if(isIE6){
		msg_bg.css("position","absolute");
		msg_bg.css("top",($(document).scrollTop()+($(window).height() - msg_bg.height())/2)+"px");
		msg_bg.css("left",(($(window).width() - msg_bg.width())/2)+"px");
		$(window).scroll(function () {
			msg_bg.css("left",($(window).width() - msgWidth-10)/2)+"px";
    		msg_bg.css("top",($(document).scrollTop()+($(window).height() - msg_bg.height())/2)+"px");
    	});
	}
	this.msgbg=msg_bg;
	var bg =this.bg;
	var _this=this;
	$(window).resize(function(){
		winw=$(window).width();
		winh=$(window).height();
		docw=$(document).width();
		doch=$(document).height();
		docw=docw<winw?winw:docw;
		doch=doch<winh?winw:doch;
		bg.css({"width":docw,"height":doch});
		msgTop=(winh - _this.height) / 2;
		msgLeft=(winw - _this.width) / 2;
		msg.css({"top":msgTop,"left":msgLeft});
		msg_bg.css({"top":msgTop-5,"left":msgLeft-5});
	});
	$("body").append(msg_bg);
	$("body").append(msg);
}

alertMsg.prototype.initBottom=function(msg){
	var _this=this;
	_this.bottom=$("<div>");
	var bottom=_this.bottom;
	bottom.css({
		width:'100%',
		height:'60px',
		"z-index": 10002
	});
	bottom.css(this.bottomCss);
	msg.append(bottom);
	var center=$("<div>");
	center.css({"width:":"100%","height":"100%","margin":"0px auto"});
	var _right="left";	
	if(_this.btnPosition=="right"){
		_right="right";
	}
	center.attr("id","alert_btn_center");
	bottom.append(center);
	
	var btn_div=$("<div>");
	btn_div.attr("id","alert_btn_div");
	btn_div.css("float",_right);
	center.append(btn_div);
	btnCss={"width":'125px',height:'33px','font-size':'16px','background-color':'#1086d2','float':"left",'margin':'0px 16px 0px 0px','color':'#fff','text-align':'center','border-radius':'5px','cursor':'pointer'};
	$.each(this.buttons,function(index,button){
		var _button=$("<div>");
		_button.css(btnCss);
		_button.css(button.css);
		_button.click(function(){button.fun()});
		_button.css('line-height',_button.height()+'px');
		_button.html(button.title);
		_button.mouseover(function(){
			_button.css("background-color","#48ADEE");
		});
		_button.mouseout(function(){
			_button.css("background-color","#1086d2");
		})
		btn_div.append(_button);
	});
	
};

alertMsg.prototype.initBody=function(msg){
	this.body=$("<div>");
	var _body=$("<div>");
	this.body.append(_body);
	var body=_body;
	_body.attr("id","alert_body2");
	body.css({
		"padding-top":20,
		'line-height':'62px',
		"padding-left":10,
		height:90,
		"z-index": 0
	});
	if(this.icon!=null){
		body.css({
			"padding-left":15
		});
	}
	body.css(this.bodyCss);
	
	if(this.icon!=null){
		var icon=$("<div>");
		icon.attr("id","alert_icon");
		icon.css({
			background:"url('"+this.icon+"') no-repeat",
			width:70,
			height:60,
			float:'left'
		});
		icon.css(this.iconCss);
		body.append(icon);
	}
	
	var span=$("<div>");
	span.css({
		float:'left',
		'margin-left':'10px',
		'white-space':'nowrap'
	});
	
	if(this.icon!=null){
		span.css({
			'font-size':'16px'
		});
	}
	span.attr("id","alert_span");
	span.html(this.content);
	body.append(span);
	this.body=body;
	msg.append(body);
};




alertMsg.prototype.initHead=function(msg){
	if(this.title==null){
		return ;
	}
	this.head=$("<div>");
	var head=this.head;
	head.css({
		height:45,
		width:"100%",
//		'background-color':'#f9f9f9',
		'font-size':'16px',
		"overflow": "hidden",
		'padding-left':'20px',
		"line-height":'45px',
		'border-bottom':'1px solid #d7d7d7'
	});
	head.css(this.headCss);
	msg.append(head);
	var title=$("<span>");
	title.attr("id","alert_title");
	title.html(this.title);
	head.append(title);
	if(this.closed){
		var closeDiv=$("<div>");
		closeDiv.css({
			width:"34px",
			height:"27px",
			'float':'right',
			"position": "absolute",
			background:"url('"+this.closeIcon+"') no-repeat",
			'cursor':'pointer',
			right:'5px'
		});
		var closeTop=(head.outerHeight()-closeDiv.height())/2;
		closeDiv.css({top:closeTop});
		var _this=this;
		
		closeDiv.click(function(){
			_this.hide();
		});
		head.append(closeDiv);
	}
};

alertMsg.prototype.initBg=function(){
	this.bg=$("<div>");
	var winw=$(window).width();
	var winh=$(window).height();
	var docw=$(document).width();
	var doch=$(document).height();
	docw=docw<winw?winw:docw;
	doch=doch<winh?winw:doch;
	var isIE6 = !$.support.opacity && !$.support.style && window.XMLHttpRequest==undefined;
	if(isIE6){
		docw=$("body").width()+25;
		doch=$("body").height()+60;
	}
	var css= {
		"background": "#000",
		"filter": "alpha(opacity=60)",
		"opacity": 0.6,
		"-moz-opacity": 0.6,
		"width": docw,
		"height": doch,
		"position": "absolute",
		"left": 0,
		"top": 0,
		"z-index": 10001,
		"overflow": "hidden"
	};
	this.bg.css(css);
	this.bg.css("display","none");
	$("body").css("padding","0px");
	$("body").append(this.bg);
}
alertMsg.prototype.show=function(speed ,callback ){
	if(!this.isInit){
		this.init();
		this.isInit=true;
	}
	var _this=this;
	if(speed==null){
		speed=0;
	}
	this.msg.show(speed,function(){
		_this.setContent(_this.content);
		if(_this.btnPosition=="center"){
			_this.initBtn();
		}
		callback;
	});
	this.bg.show();
	this.msgbg.show(speed);
	return this;
};



alertMsg.prototype.hide=function(speed ,callback ){
	if(this.cache!=null){
		this.width=this.cache;
		this.msg.width(this.width);
		this.msgbg.width(this.width+10);
		this.cache=null;
	}
	if(speed==null){
		speed=0;
	}
	var _this=this;
	this.bg.hide(speed,function(){
		if(_this.input!=null){
			_this.input.focus();
		}
		callback;
	});
	this.msg.hide(speed);
	this.msgbg.hide(speed);
	return this;
};
alertMsg.prototype.destroy=function(){
	this.msg.remove();
	this.msgbg.remove();
	this.bg.remove();
	this.minimizable=null;
	this.maximizable=null;
	this.minCss=null;
	this.maxCss=null;
	this.clsCss=null;
	this.bg=null;
	this.msg=null;
	this.msgbg=null;
	this.head=null;
	this.body=null;
	this.bottom=null;
	this.cache=null;
	this.msgLevel='warn';
	this.isInit=false;
	this.closed=true;
	this.icon=path + "/images/warn_min.png";
	this.closeIcon=path + "/images/close_min.png";
	this.iconCss={};
	this.bodyCss={};
	this.headCss={};
	this.bottomCss={};
	this.title="温馨提示";
	this.content="欢迎使用";
	this.width=400;
	this.height=210;
	this.buttons=null;
	this.btnPosition="center";
	this.input=null;
	var _this=this;
	this.buttons=[{title:'确&nbsp;认',css:{},fun:function(){_this.hide();}}];
	if(_this.input!=null){
		_this.input.focus();
	}
	return this;
};
alertMsg.prototype.fadeIn=function(speed ,callback ){
	if(!this.isInit){
		this.init();
		this.isInit=true;
	}
	this.bg.fadeIn(speed,callback);
	this.msg.fadeIn(speed);
	this.msgbg.fadeIn(speed);
	return this;
};
alertMsg.prototype.fadeOut=function(speed ,callback ){
	this.bg.fadeOut(speed,callback);
	this.msg.fadeOut(speed);
	this.msgbg.fadeOut(speed);
	return this;
};
alertMsg.prototype.setContent=function(content){
	if(!this.isInit){
		this.content=content;
	}else{
		var _this=this;
		_this.content=content;
		var body=_this.msg.find("#alert_body2");
		var span=body.find("#alert_span");
		var icon=body.find("#alert_icon");
		span.html(content);
		var isIE6 = !$.support.opacity && !$.support.style && window.XMLHttpRequest==undefined;
		var isIE7 = !$.support.opacity && !$.support.style && window.window.XMLHttpRequest!=undefined;
		if((span.width()+icon.width())>(body.width()-56)){
			_this.cache=_this.msg.width();
			var w=80;
			if(isIE6){
				w=40;
			}
			_this.width=span.width()+icon.width()+w;
			_this.msg.width(_this.width);
			_this.msgbg.width(_this.width+10);
		}
		var left=(_this.width-span.width()-icon.width())/2-16;
		if(isIE6||isIE7){
			left-=20;
		}
		if (left<0){
			left=4;
		}
		if(this.icon!=null){
			icon.css("margin-left",left);
			icon.css(this.iconCss);
		}else{
			if(isIE6||isIE7){
				left-=10;
			}else{
				left=left;
			}
			span.css("margin-left",left+5);
			span.css(this.iconCss);
		}
	}
	return _this;
}

alertMsg.prototype.initBtn=function(){
	var _this = this;
	var center=_this.bottom.find("#alert_btn_center");
	var width=center.find("#alert_btn_div").width();
	
	if(width<0){
		width=0;
	}
	center.css("padding-left","16px");
	center.css("width",width);
	return _this;
}


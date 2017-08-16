$(function(){
	var $tab = $("#menuList li>a");
	$.each($tab,function(k,v){
		$(v).click(function(){
			$tab.siblings("dl").slideUp();//隐藏
			if($(v).hasClass("have_menu")){
				$(v).siblings("dl").slideDown(); //显示
			}else{
				$("#menuList a").removeClass("cur");
				$(v).addClass("cur");
				var code = $(v).attr("code"); 
				$("#helpArticle").html($("#"+code+"Div").html());
			}
		});
	});
	$tab.first().click();
	var $tabA = $("#menuList dd>a");
	$.each($tabA,function(k,v){
		$(v).click(function(){
			$("#menuList a").removeClass("cur");
			 $(v).addClass("cur");
			 var code = $(v).attr("code"); 
			$("#helpArticle").html($("#"+code+"Div").html());
		});
	});
	$("#menuList dd").first().children("a:first-child").click();
});
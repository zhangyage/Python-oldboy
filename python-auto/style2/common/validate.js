/*
 * 公共验证方法
 */
var Valify = {
		//检验是否为空
		isNull: function(str, id){
			if(!str){
				AlertDialog.show($("#" + id).attr("nullMessage"), id, 10, 90);
				return false; 
			}
			AlertDialog.hide();
			return true;
		},
		//验证用户名
		username: function(str, result, id){
			var $inputt;
			if($("#" + id).parent()[0].tagName == "LI"){
				$inputt = $("#" + id).parent().children(".inputf");
			}else{
				$inputt = $("#" + id).parent().parent().parent().children(".inputf");
			}
			if(/\s+/g.test(str)){
				$inputt.css("display", "inline-block").text("用户名不能含有空格");
				return false;
			}
			str = str.replace(/^\s\s*/, '').replace(/\s\s*$/, '');//去掉收尾空格
			if(!str){
				$inputt.css("display", "inline-block").text("用户名不能为空");
				return false;
			}else if(/[\u4E00-\u9FA5]/i.test(str)){
				$inputt.css("display", "inline-block").text("用户名不能含有中文");
				return false;
			}else if(!isNaN(str)){
				$inputt.css("display", "inline-block").text("用户名不能为纯数字");
				return false;
			}else if(str.length < 6 || str.length > 16){
				$inputt.css("display", "inline-block").text("用户名应该是6到16位");
				return false;
			}else{
				//如果验证用户名格式通过，验证是否重复
				$.ajax({
					url: path + "/user/validateUserId.html",
					type: "post",
					dataType: "json",
					async: false,
					data: {"userId": str},
					success: function(data){
						if(data["msg"] == "success"){
							$inputt.css("display", "none");
							result = true;
						}else{
							$inputt.css("display", "inline-block").text(data["msg"]);
							result = false;
						}
					},
					error: function(){
						console.log("检查用户名异常");
					}
				});
				return result;
			}
		},
		//验证注册密码
		password: function(str,id,ctype){
			var $inputt = $("#" + id).parents("li").children(".inputf");
			if(!str){
				if(ctype == "ctype"){
					AlertDialog.show("密码长度应该为6~16位", id, 0, 20);
				}else{
					$inputt.css("display", "inline-block").text("密码长度应该为6~16位");
				}
				return false;
			}
			if(!/^(\w){6,16}$/.exec(str)){
				if(ctype == "ctype"){
					AlertDialog.show("密码长度应该为6~16位", id, 0, 20);
				}else{
					$inputt.css("display", "inline-block").text("密码长度应该为6~16位");
				}
				return false;
			}else{
				if(ctype == "ctype"){
					AlertDialog.hide();
				}else{
					$inputt.css("display", "none");
				}
				return true;
			}
		},
		//验证密码强度
		passStrength: function(str){
			if (str==null||str==''){
				$("#pwds").hide();
			}else{
				var S_level = checkStrong(str);
				switch(S_level) {
					case 1:
						$("#pwds").removeClass("inputf").html('<span class="s">弱</span><span>中</span><span>强</span>');
						break;
					case 2:
						$("#pwds").removeClass("inputf").html('<span class="s">弱</span><span class="s">中</span><span>强</span>');
						break;
					case 3:
						$("#pwds").removeClass("inputf").html('<span class="s">弱</span><span class="s">中</span><span class="s">强</span>');
						break;
					default:
						$("#pwds").removeClass("inputf").html('<span class="s">弱</span><span>中</span><span>强</span>');
				}
			}
			//返回密码强度级别
			function checkStrong(sPW){
				if (sPW.length < 6){
					$("#pwds").hide();
					return 0; //密码太短
				}
				$("#pwds").show();//显示 密码强度提示
				var Modes=0;
				for (var i=0;i<sPW.length;i++){
					//测试每一个字符的类别并统计一共有多少种模式.
					Modes|=CharMode(sPW.charCodeAt(i));
				}
				return bitTotal(Modes);
			}
			//计算当前密码一共有多少种模式
			function bitTotal(num){
				modes=0;
				for (var i=0;i<4;i++){
					if (num & 1) modes++;
					num>>>=1;
				}
				return modes;
			}
			//计算字符的charcode
			function CharMode(iN){
				if (iN>=48 && iN <=57) //数字
					return 1;
				if (iN>=65 && iN <=90) //大写字母
					return 2;
				if (iN>=97 && iN <=122) //小写
					return 4;
				else
					return 8; //特殊字符
			}
		},
		//验证重复密码
		rePass: function(str, str1, id, ctype){
			var $inputt = $("#" + id).parents("li").children(".inputf");
			if(!str1){
				if(ctype == "ctype"){
					AlertDialog.show("密码不能为空", id, 0, 20);
				}else{
					$inputt.css("display", "inline-block").text("密码不能为空");
				}
				return false;
			}
			if(str != str1){
				if(ctype == "ctype"){
					AlertDialog.show("两次输入密码不一致", id, 0, 20);
				}else{
					$inputt.css("display", "inline-block").text("两次输入密码不一致");
				}
				return false;
			}else{
				if(ctype == "ctype"){
					AlertDialog.hide();
				}else{
					$inputt.css("display", "none");
				}
				return true;
			}
		},
		//验证码验证
		valiCode: function(str, result, id, isAjax, ctype){
			var $tip = $("#" + id).parents("li").children(".inputf");
			if(!str){
				if(ctype == "ctype"){
					$tip.css("display", "inline-block").text("图片验证码不能为空");
				}else{
					AlertDialog.show("图片验证码不能为空", id, 0, 20);
				}
				$("#valishow").removeClass("t").addClass("f");
				return false;
			}else{
				if(ctype == "ctype"){
					$tip.css("display", "inline-block");
				}else{
					AlertDialog.hide();
				}
			}
			
			if(isAjax == false){
				if(ctype == "ctype"){
					$tip.css("display", "inline-block");
				}else{
					AlertDialog.hide();
				}
				return result;
			}
			$.ajax({
				url: path + "/user/validateVerifyCode.html",
				type: "post",
				async: false,
				dataType: "json",
				data: {"valiCode": str},
				success: function(data){
					if(data["msg"] == "success"){
						if(ctype == "ctype"){
							$tip.css("display", "none");
						}else{
							AlertDialog.hide();
						}
						$("#valishow").css("display","inline-block");
						$("#valishow").removeClass("f").addClass("t");
						result = true;
					}else{
						if(ctype == "ctype"){
							$tip.css("display", "none");
							$tip.css("display", "inline-block").text("图片验证码错误");
						}else{
							AlertDialog.hide();
							AlertDialog.show("图片验证码错误", id, 0, 20);
						}
						$("#valishow").css("display","inline-block");
						$("#valishow").removeClass("t").addClass("f");
						$("#imgYzm").click();
						result = false;
					}
				},
				error: function(){
					console.log("获取邀请码异常");
				}
			});
			return result;
		},
		//验证手机号码
		phone: function(phone, id, ctype){
			var $tip = $("#" + id).parents("li").children(".inputf");
			var isPhoneReg = /^(0|86|17951)?(13[0-9]|15[012356789]|17[0678]|18[0-9]|14[57])[0-9]{8}$/;
//			if(!data["success"]){
//				$("#" + id).next().css("display", "inline-block").text("手机号不正确");
//				return false;
//			}
			if(!phone){
				if(ctype == "f"){
					$tip.css("display", "inline-block").text("手机号不能为空");
				}else{
					AlertDialog.show("手机号不能为空", id, 0, 20);
				}
				return false;
			}
			if(isPhoneReg.exec(phone)){
				if(ctype == "f"){
					$tip.css("display", "none");
				}else{
					AlertDialog.hide();
				}
				return true;
			}else{
				if(ctype == "f"){
					$tip.css("display", "inline-block").text("手机号不正确");
				}else{
					AlertDialog.show("手机号不正确", id, 0, 20);
				}
				return false;
			}
		},
		//验证手机验证码
		phoneValiCode: function(code, id , ctype){
			var $inputt = $("#" + id).parents("li").children(".inputf");
			if(!code){
				if(ctype == "f"){
//					$inputt.show().text("验证码不能为空");
					$inputt.css("display", "inline-block").text("验证码不能为空");
				}else{
					AlertDialog.show("验证码不能为空", id, 0, 20);
				}
				return false;
			}
			if(code.length != 6){
				if(ctype == "f"){
//					$inputt.show().text("验证码不能为空");
					$inputt.css("display", "inline-block").text("验证码应该为6位数字");
				}else{
					AlertDialog.show("验证码应该为6位数字", id, 0, 20);
				}
//				$inputt.show().text("验证码应该为6位数字");
				return false;
			}
			if(!isNaN(code)){
				if(ctype == "f"){
					$inputt.css("display", "none");
				}else{
					AlertDialog.hide();
				}
//				$inputt.hide();
				return true;
			}else{
				if(ctype == "f"){
//					$inputt.show().text("验证码不能为空");
					$inputt.css("display", "inline-block").text("验证码应该为纯数字");
				}else{
					AlertDialog.show("验证码应该为纯数字", id, 0, 20);
				}
//				$inputt.show().text("验证码应该为纯数字");
				return false;
			}
		},
		//验证邮政编码
		postCode: function(code, id){
			var $inputt = $("#" + id).parent().children(".inputf");
			if(!code){
				AlertDialog.show("请输入邮编", id, 0, 20);
//				$inputt.text("请输入邮编").show();
				return false;
			}
			if(code.length != 6){
				AlertDialog.show("请输入正确的邮编", id, 0, 20);
//				$inputt.text("请输入正确的邮编").show();
				return false;
			}
			if(!isNaN(code)){
				AlertDialog.hide();
				return true;
			}else{
				AlertDialog.show("请输入正确的邮编", id, 0, 20);
//				$inputt.show().text("请输入正确的邮编").show();
				return false;
			}
		},
		email: function(str, id){
			var $inputt = $("#" + id).parent().children(".inputf");
			if(!str){
				AlertDialog.show("邮箱不能为空", id, 0, 20);
				return false;
//				$inputt.text("请输入电子邮箱").show();
//				return false;
			}
			var isEmailReg = /^(\w-*\.*)+@(\w-?)+(\.\w{2,})+$/;
			if(isEmailReg.test(str)){
				AlertDialog.hide();
				return true;
			}else{
				AlertDialog.show("请输入正确的电子邮箱", id, 0, 20);
				return false;
//				$inputt.text("请输入正确的电子邮箱").show();
//				return false;
			}
		},
		//真实姓名
		realName: function(name, id){
			var l, nameCharCode, chNameStr = '', enNameStr = '';
			if(!name){
				AlertDialog.show("真实姓名不能为空", id, 0, 50);
				return false;
			}
			l = name.length;
			for(var i=0;i<l;i++){
				nameCharCode = name.charAt(i).charCodeAt();
				if((nameCharCode > 255 && nameCharCode < 40869) || nameCharCode == 183){//中文
					chNameStr += name.charAt(i);
				}else if(nameCharCode >= 65 && nameCharCode <= 90 || nameCharCode >= 97 && nameCharCode <= 122 || nameCharCode == 32){//英文
					enNameStr += name.charAt(i);
				}else{
					AlertDialog.show("真实姓名输入不正确", id, 0, 50);
					return false;
				}
			}
			if(chNameStr == name || enNameStr == name){
				if(chNameStr.charAt(0).charCodeAt() > 255 && (chNameStr.length > 15 || chNameStr.length < 2)){//中文姓名格式
					AlertDialog.show("真实姓名输入不正确", id, 0, 50);
					return false;
				}else if(((enNameStr.charAt(0).charCodeAt() >= 65 && enNameStr.charAt(0).charCodeAt() <= 90) || (enNameStr.charAt(0).charCodeAt() >= 97 && enNameStr.charAt(0).charCodeAt() <= 122)) && (enNameStr.length > 30 || enNameStr.length < 4)){//英文格式
					AlertDialog.show("真实姓名输入不正确", id, 0, 50);
					return false;
				}else{
					AlertDialog.hide();
					return true;
				}
			}else{
				AlertDialog.show("真实姓名输入不正确", id, 0, 50);
				return false;
			}
		},
		//身份证号码
		cardCode: function(code, id){
			if(!code){
				AlertDialog.show("证件号码不能为空", id, 10, 90);
				return false;
			}else{
				var num = code.toUpperCase();  
				//身份证号码为15位或者18位，15位时全为数字，18位前17位为数字，最后一位是校验位，可能为数字或字符X。
				if (!(/(^\d{15}$)|(^\d{17}([0-9]|X)$)/.test(num))) {
					AlertDialog.show("身份证号码不正确", id, 10, 90);
					return false;
				}
				//校验位按照ISO 7064:1983.MOD 11-2的规定生成，X可以认为是数字10。
				//下面分别分析出生日期和校验位
				var len, re;
				len = num.length;
				if (len == 15) {
					re = new RegExp(/^(\d{6})(\d{2})(\d{2})(\d{2})(\d{3})$/);
					var arrSplit = num.match(re);
					
					//检查生日日期是否正确
					var dtmBirth = new Date('19' + arrSplit[2] + '/' + arrSplit[3] + '/' + arrSplit[4]);
					var bGoodDay,goodyear;
					bGoodDay = (dtmBirth.getYear() == Number(arrSplit[2])) && ((dtmBirth.getMonth() + 1) == Number(arrSplit[3])) && (dtmBirth.getDate() == Number(arrSplit[4]) && (thisYear >= dtmBirth.getFullYear()));
					if (!bGoodDay) {
						AlertDialog.show("身份证号码不正确", id, 10, 90);
						return false;
					} else {
						//验证是否为成年人（大于18周岁）
//		            	if(thisYear > (dtmBirth.getFullYear() + 17)){
//		            		return 0;
//		            	}
						//将15位身份证转成18位
						//校验位按照ISO 7064:1983.MOD 11-2的规定生成，X可以认为是数字10。
						var arrInt = new Array(7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2);
						var arrCh = new Array('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2');
						var nTemp = 0, i;
						num = num.substr(0, 6) + '19' + num.substr(6, num.length - 6);
						for (i = 0; i < 17; i++) {
							nTemp += num.substr(i, 1) * arrInt[i];
						}
						num += arrCh[nTemp % 11];
						AlertDialog.hide();
						return true;
					}
				}
				if (len == 18) {
					re = new RegExp(/^(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)$/);
					var arrSplit = num.match(re);
					
					//检查生日日期是否正确
					var dtmBirth = new Date(arrSplit[2] + "/" + arrSplit[3] + "/" + arrSplit[4]), bGoodDay,thisYear = new Date().getFullYear();
					bGoodDay = (dtmBirth.getFullYear() == Number(arrSplit[2])) && ((dtmBirth.getMonth() + 1) == Number(arrSplit[3])) && (dtmBirth.getDate() == Number(arrSplit[4]));
					if (!bGoodDay) {
						AlertDialog.hide();
						return true;
					} else if(dtmBirth.getFullYear() > new Date().getFullYear()){//判断出生年份是否大于当前年份
						AlertDialog.show("身份证号码不正确", id, 10, 90);
						return false;
					}else if(dtmBirth.getFullYear() < 1900){
						AlertDialog.show("身份证号码不正确", id, 10, 90);
						return false;
					}else{
						//验证是否为成年人（大于18周岁）
//		          if(thisYear > (dtmBirth.getFullYear() + 17)){
//		        		return 0;
//		        	}
						//检验18位身份证的校验码是否正确。
						//校验位按照ISO 7064:1983.MOD 11-2的规定生成，X可以认为是数字10。
						var valnum;
						var arrInt = new Array(7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2);
						var arrCh = new Array('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2');
						var nTemp = 0, i;
						for (i = 0; i < 17; i++) {
							nTemp += num.substr(i, 1) * arrInt[i];
						}
						valnum = arrCh[nTemp % 11];
						if (valnum != num.substr(17, 1)) {
							AlertDialog.show("身份证号码不正确", id, 10, 90);
							return false;
						}
						AlertDialog.hide();
						return true;
					}
				}
				AlertDialog.show("身份证号码不正确", id, 10, 90);
				return false; 
			}
		}
};

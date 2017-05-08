//alter 就是一个弹窗
//alert('理解')


//name = 'zhangyage'    全局变量
//var name = 'panyuanqing'   局部变量

/*  函数
function Foo(name){
	var arg2 = arguments[1]   //arguments[1]是获取执行行数传递的第二个参数
	console.log(name);
	console.log(arg2);
}

Foo('zhangyage','pan')
*/

//自值型函数   切记写的时候不要写函数名字
(function(name){
	console.log(name.trim());  //obj.trim()去除字符串两遍的空格
	console.log(name);
})('    old boy     ')


test = 'thisisatest'
console.log(test.charAt(3))       //obj.charAt(index)   通过索引找字符
console.log(test.substring(3,6))  //obj.substring(3,6)  处理字符串根据指定索引切片 
console.log(test.indexOf('s'))    //obj.indexOf('s')    获得指定字符的索引
console.log(test.length)          //obj.length          获取字符串的长度

var arry = [1,2,3,4]
arry.push('zhangyage');           //在数组后插入一个元素
console.log(arry);
arry.unshift('panyuanqing');      //在数组开头插入一个元素
console.log(arry);
arry.splice(1,0,'liguang');       //在第一个元素后插入一个元素
console.log(arry);


arry.pop()                       //删除数组中最后一个元素
console.log(arry);
arry.shift()                     //删除数组中第一个元素
console.log(arry);
arry.splice(0,2)                 //删除数组元素，从第一个元素开始往后删除两个
console.log(arry);

console.log(arry.slice(0,2))    //arry.slice(start,count)截取元素，从第一个元素开始带后面两个

arry1=['this','is','a','test']
console.log(arry.concat(arry1)) //合并数组

console.log(arry1.reverse())    //逆序输出

console.log(arry1.join(' '))    //使用空格合并数组

console.log(arry1.length)       //计算数组的长度
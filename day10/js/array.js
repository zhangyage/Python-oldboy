var array = [11,22,33,44,55,66]
var dict = {'name':'alex','age':19}

//循环输出索引
for(var item in array){
	console.log(item)
}

//循环输出数组元素
for(var item in array){
	console.log(array[item])
}

//循环输出key
for(var item in dict){
	console.log(item)
}

//循环输出value
for(var item in dict){
	console.log(dict[item])
}


for(var i=0;i<10;i++){
	console.log(array[i]);
}

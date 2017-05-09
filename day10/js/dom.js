var tag = document.createElement('a'); 
//创建标签
tag.href = 'http://autohome.com.cn';

tag.innerText = '点我啊';


var id1 = document.getElementById('t1');
id1.appendChild(tag);


//方法二
var tag = "<a href='http://baidu.com'>看一看</a>"
var id2 = document.getElementById('t2');
id1.innerHTML = tag ;
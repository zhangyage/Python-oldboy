#!/usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

year = [1911,1912,1913,1914]
pop = [1.7,3,7,10]

#plt.plot(year,pop)    #画折线图
#plt.scatter(year,pop)  #画散点图  
plt.fill_between(year, pop, 0, color='green')   #人性化显示 有绿色图块


plt.xlabel('Year')       #X轴的标签
plt.ylabel('Population')
plt.title("world Population Projection")   #标题
plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11])  #Y轴的刻度


plt.show()

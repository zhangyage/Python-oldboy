#!/usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

year = [1911,1912,1913,1914]
pop = [1.7,2.5,3.1,3.9]
#plt.plot(year,pop)    #画折线图
plt.scatter(year,pop)  #画散点图
plt.show()

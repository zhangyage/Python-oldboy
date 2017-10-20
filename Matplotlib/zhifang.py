#!/usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

values = [0,0.5,0.7,1,0.4,6,4,5.5,5,3.2,3.3]
plt.hist(values,bins=3)
plt.show()
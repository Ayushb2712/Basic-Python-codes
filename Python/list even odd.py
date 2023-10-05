# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 08:40:48 2022

@author: ayush
"""

import random
list1=[]
for ii in range(0,8):
    list1.append(random.randint(0,ii))
print("List =" , list1)
for ii in range(0,8):
    if list1[ii]%2==0:
        print(list1[ii] , " is even")
    else:
        print(list1[ii] , " is odd")

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 08:20:22 2022

@author: ayush
"""

import random
list1=[]
for i in range(0,25):
    list1.append(random.randint(0,i))
print("List = ", list1)
min=list1[0]
max=list1[0]
for i in range(0,25):
    if list1[i]>max:
        max=list1[i]
    elif list1[i]<min:
        min=list1[i]
print("Max value = ", max)
print("Min value =" , min)
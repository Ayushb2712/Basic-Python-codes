# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 08:27:11 2022

@author: ayush
"""

import random
list1=[]
a=int(input("Enter number you want to find "))
for ii in range(0,25):
    list1.append(random.randint(0,ii))
print("List = " , list1)
l=list1.index(a)
if l in list1:
    print("Number found at index =" , a)
else:
    print("Number not found")
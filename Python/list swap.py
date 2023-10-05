# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:20:18 2022

@author: ayush
"""
import random
a=int(input("Enter element position 1 for swap "))
b=int(input("Enter element position 2 for swap "))
list1=[]
for ii in range(0,25):
    list1.append(random.randint(0,ii))
print("Original list ",list1)
temp=list1[a]
list1[a]=list1[b]
list1[b]=temp
print("New list ", list1)
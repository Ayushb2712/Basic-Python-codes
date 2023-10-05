# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:55:31 2022

@author: ayush
"""


list1=[]
sum=0
prod=1
for i in range(0,25):
    a=int(input())
    list1.append(a)
    sum+=a
    prod*=a
print("Sum =" ,sum)
print("Product =", prod)
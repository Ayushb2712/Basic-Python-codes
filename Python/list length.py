# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:25:43 2022

@author: ayush
"""
import random
list1=[]
for ii in range(0,25):
    list1.append(random.randint(0,ii))
sum=0
for a in list1:
    sum+=1
print("Length through loop is ", sum)
print("length through function ",len(list1))

    
    
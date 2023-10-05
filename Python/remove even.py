# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 17:45:31 2022

@author: ayush
"""

#remove all even number from a list
import random
list1=[]
for ii in range(0,10):
    list1.append(random.randint(0,ii))
print("Original list =" , list1)
list2=[]

for ii in range(0,10):
    if list1[ii]%2==0:
        continue
    else:
        list2.append(list1[ii])
print("New list after removing even numbers = ",list2)
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:10:20 2022

@author: ayush
"""
#print index of number if negative or zero
list1=[]
n=int(input("Enter number of elements in list"))

for ii in range(0,n):
    a=input("Enter element " )
    list1.append(a)
for ii in range(0,n):
    if int(list1[ii])<=0:
        print("Index = " , ii)

      
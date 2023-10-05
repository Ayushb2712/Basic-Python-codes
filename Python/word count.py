# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 18:15:13 2022

@author: ayush
"""
#word count
str1=input("Enter a string : ")
count=1
l=len(str1)
for ii in range(0,l):
    if str1[ii]==' ':
        count+=1
print(count)
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 07:39:05 2022

@author: ayush
"""

str1=input("Enter string 1 ")
str2=input("Enter string 2 ")
c=0
list1=str1.split(" ")
list2=str2.split(" ")
for i in list1:
    if i in list2:
        c+=1
print(c)
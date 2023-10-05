# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 18:22:27 2022

@author: ayush
"""

#print even length word
str1=input("Enter a string : ")
n=len(str1)
s=str1.split(" ")
for ii in s:
    if len(ii)%2==0:
        print(ii)
    
   
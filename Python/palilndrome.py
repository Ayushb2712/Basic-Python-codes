# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 21:25:41 2022

@author: ayush
"""

str1=input("Enter a string : ")
str2=''.join(reversed(str1))
n=len(str1)
count=0
for ii in range(0,n):
    if str1[ii]!=str2[ii]:
        count+=1
if count==0:
    print("Is palindrome")
else:
    print("Not palindrome")
    
    
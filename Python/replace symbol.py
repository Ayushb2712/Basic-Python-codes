# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 18:18:01 2022

@author: ayush
"""

#replace character
str1=input("Enter a string : " )
n=input("Enter character to replace : ")
l=len(str1)
str2=""
for ii in range(0,l):
    if str1[ii]==n:
        z=int(ii+1)
        str2+=str1[:ii]+str1[z:]
        break
 
print(str2)        
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:49:32 2022

@author: ayush
"""

#remove nth character
str1=input("Enter string :")
n =int( input("Enter character index to remove :"))
l=len(str1)
z=int(n+1)
str2=str1[:n]+str1[z:]
print(str2)
                   

     
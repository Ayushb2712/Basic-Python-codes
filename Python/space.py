# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:30:27 2023

@author: ayush
"""

str1=input("Enter a string :")
str2=" "
str3="..."
for ii in str1:
    if ii==" ":
        str2+=str3
    else:
        str2+=ii
print(str2)
        
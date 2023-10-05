# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 11:03:56 2022

@author: ayush
"""

a=input("Enter string :")
b=""+a[0]
alphastr="abcdefghijklmnopqrstuvwxyz"
for i in a[1:len(a)]:
    b+=alphastr[25-alphastr.index(i)]
print(b)
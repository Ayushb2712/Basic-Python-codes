# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 09:58:32 2022

@author: ayush
"""

l=int(input("Enter how many numbers you want in the series "))
a=0
b=1
count=1
while count<=4:
    print(a)
    
    c=a+b
    a=b
    b=c
    count+=1
    
  
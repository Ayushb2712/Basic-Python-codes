# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 17:51:14 2022

@author: ayush
"""

l=int(input("Enter a year"))
if l%100==0 and l%400==0:
    print("It is a leap year")
elif l%4==0 and l%100!=0 :
    print("It is a leap year") 
else:
    print("It is not a leap year")
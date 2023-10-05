# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 18:07:15 2022

@author: ayush
"""

a=int(input("Enter number whose table you want to see "))
b=int(input("Enter number upto which you want to see table "))
z=b+1
for i in range(1,z):
    print(i ," x ", a , (" = "), a*i)
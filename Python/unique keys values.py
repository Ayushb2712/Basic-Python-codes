# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 10:56:18 2022

@author: ayush
"""

dict1={}
for i in range(5):
    a=input("Enter key ")
    b=input("Enter value ")
    dict1[a]=b
c=list(sorted({ele for val in dict1.values() for ele in val}))
d=list(sorted({ele for val in dict1.keys() for ele in val}))
print("Unique values =" , c)
print("Unique keys=" , d)
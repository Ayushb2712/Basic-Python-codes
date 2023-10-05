# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 17:54:03 2022

@author: ayush
"""

l1=int(input("Enter number 1 "))
l2=int(input("Enter number 2 "))
l3=int(input("Enter number 3 "))
if l1>l2 and l1>l3:
    print("Biggest number is" , l1)
elif l2>l1 and l2>l3:
    print("Biggest number is " , l2)
elif l3>l1 and l3>l2:
    print("Biggest number is " , l3)
else:
    print("All three numbers are equal")
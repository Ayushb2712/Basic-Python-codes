# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 18:31:48 2022

@author: ayush
"""

a=float(input("Enter co-efficient of x^2 "))
b=float(input("Enter  co-efficent of x "))
c=float(input("Enter constant term "))
s1=(-b+(b**2-4*a*c)**0.5)/(2*a)
s2=(-b-(b**2-4*a*c)**0.5)/(2*a)
print("Root 1= " , s1)
print("Root 2= " , s2)
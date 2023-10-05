# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 18:07:59 2022

@author: ayush
"""

a=float(input("Enter a number"))
i=2
ctr=0
while i<a:
    if a%i==0:
        ctr+=1
    i+=1
if ctr==0:
    print("Number is prime")
else: 
    print("Number is composite")
    
    
    

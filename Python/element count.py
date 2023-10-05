# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:26:53 2022

@author: ayush
"""

#count number of times each element occurs in a list
list1=[]
n=int(input("Enter number of elements in list "))
for ii in range(0,n):
    a=input("Enter element ")
    list1.append(a)
bl=[]
for ii in list1:
    if ii not in bl:
        count=0
        for jj in list1:
            if ii==jj:
                count+=1
                bl.append(jj)
        print("number of times " , ii , "occurs" , count)
    
    
  
   
        
        
    
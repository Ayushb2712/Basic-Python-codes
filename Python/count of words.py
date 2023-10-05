# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 18:37:33 2022

@author: ayush
"""

#print count of matching words from 2 strings
str1=input("Enter  string 1 : ")
str2=input("Enter  string 2 : ")
count=0
bl=[]
s=str1.split(" ")
k=str2.split(" ")
for ii in s:
    count=1
    if ii in bl:
        continue
    else:
        for jj in k:
            if ii==jj:
                count+=1
                bl.append(jj)
    if count>1:
        print("Number of times repeated word occurs is : " , count)
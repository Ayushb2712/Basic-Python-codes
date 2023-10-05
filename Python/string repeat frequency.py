# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 19:07:52 2022

@author: ayush
"""

#count duplicate in string
str1=input("Enter a string : ")
count=0
bl=""
s=str1.split(" ")
for ii in s:
    count=0
    if ii not in bl:
        for jj in s:
            if ii==jj:
                count+=1
                bl+=jj
    if count>1:
        print ("The number of times " , ii , "occurs is " , count)
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 09:29:32 2022

@author: ayush
"""

str1=input("Enter string ")
list1=str1.split(" ")
list2=[]
list3=[]
bl=[]
for i in list1:
    if i not in bl:
        count=0
        for j in list1:
            if i==j:
                count+=1
                bl.append(j)
        list2.append(count)
        list3.append(i)
maxima=list2[0]
for i in list2:
    if i>maxima:
        maxima=i
print("Maximum frequency word is ")
for ii in range(len(list2)):
    if list2[ii]==maxima:
        print(list3[ii])
        
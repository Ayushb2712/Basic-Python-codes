# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:51:40 2022

@author: ayush
"""

#print max and min frequency character in string
str1=input("Enter a string : ")
bl=""
list1=[]
list2=[]
n=len(str1)
for ii in range(0,n):
    count=0
    if str1[ii] not in bl:
        for jj in range(0,n):
            if str1[ii]==str1[jj]:
                count+=1
                bl+=str1[jj]
           
        list1.append(count)
        list2.append(str1[ii])
    
maxi=list1[0]
mini=list1[1]
for ii in list1:
    if ii>maxi:
        maxi=ii
    elif ii<mini:
        mini=ii
print("Max frequency char are ")
for ii in range(len(list1)):
    if list1[ii]==maxi:
        print(list2[ii])    
print("Min frequency char are ")
for ii in range(len(list1)):
    if list1[ii]==mini:
        print(list2[ii])
          
    
     
  
        
                
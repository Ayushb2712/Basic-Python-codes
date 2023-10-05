# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 12:22:17 2022

@author: ayush
"""

l1=eval(input())
l2=eval(input())
la=[]
lb=[]
ld=[]
summ=0
for ii in range(len(l1)):
    la=l1[ii]
    lb=l2[ii]
    lc=[]
    for jj in range(len(la)):
        summ+=la[jj]+lb[jj]
        lc.append(summ)
        summ=0
        
    ld.append(lc)
for j in ld:
    print(j)


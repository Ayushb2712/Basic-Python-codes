# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 19:01:32 2022

@author: ayush
"""
ul=int(input("Enter upper limit"))
ll=int(input("Enter lower limit"))

for i in range(ll,ul):
    ctr=0
    if i==1 or i==0:
        continue
    else:
        for num in range(2,i):
            if i%num==0:
                ctr+=1 
                break
    if ctr==0: 
        print(i)

              

   

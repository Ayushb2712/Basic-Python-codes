# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 18:19:00 2022

@author: ayush
"""

a=input()
b=int(a)
l=len(a)

x1=lambda x,y:print("yes") if sum(int(i)**y for i in x)==b else print("no")
x1(a,l)

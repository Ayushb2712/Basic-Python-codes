# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n=int(input())
def fact1(d):
    if d==1 or d==0:
        return 1
    else:
        return d*fact1(d-1)
a=fact1(n)
print(a)
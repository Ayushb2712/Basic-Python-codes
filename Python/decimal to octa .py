# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 18:47:40 2022

@author: ayush
"""

de=int(input("Enter a number "))
print(bin(de))
print(hex(de))
print(oct(de))
print("{0:d}--->{1:b}".format(de,de))
print("{0:d}--->{1:o}".format(de,de))
print("{0:d}--->{1:x}".format(de,de))
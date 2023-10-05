# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:38:32 2022

@author: ayush
"""

#to generate a string equivalent to the given string
import string
import random
str1=string.ascii_uppercase
str2=string.ascii_lowercase
str3=string.digits
str4="!@#$%^&*I(OOIY"
str5=str1+str2+str3+str4
strg=input("Enter a string ")
n=len(strg)
flag=True
str_a=""
while flag:
    str_a=""
    for ii in range(n):
        str_a+=random.choice(str5)
    if str_a==strg:
        print("Generated string " , str_a)
        flag=False
        



# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 17:48:46 2022

@author: ayush
"""

def is_leapyear():
    n=int(input("Enter year: "))
    if n%4==0:
        if n%100==0:
            if n%400==0:
                return True
            else:
                return False
       
        
    else:
        return False
a=is_leapyear()
print(a)
      

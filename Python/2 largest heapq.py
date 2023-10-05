# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 18:43:18 2022

@author: ayush
"""

import heapq
list1=eval(input())
l1=heapq.nlargest(2,list1)
l2=heapq.nsmallest(2,list1)
print(l1)
print(l2)
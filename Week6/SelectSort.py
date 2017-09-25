# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:57:35 2017

@author: quang
"""

def select_sort (L):
    len_L = len (L)
    for i in range (len_L - 1):
        print (L)
        minIndx = i
        minVal = L[i]
        j = i + 1
        while j < len_L:
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        L[i], L[minIndx] = L[minIndx], L[i]
        
L = [3, 4, 2, 5, 1]
select_sort (L)
print (L)
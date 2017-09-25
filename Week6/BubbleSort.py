# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:47:32 2017

@author: quang
"""

def bubble_sort (L):
    swap = False
    len_L = len (L)
    while not swap:
        swap = True
        for i in range(1, len_L):
            if L[i - 1] > L[i]:
                swap = False
                L[i - 1], L[i] = L[i], L[i - 1]
                
L = [3, 4, 2, 5, 1]
bubble_sort (L)
print (L)
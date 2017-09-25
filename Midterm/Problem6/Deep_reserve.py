# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 18:04:04 2017

@author: quang
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    Fox exp. if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]
    """
    if type (L) == list:
        lenL = len(L)
        for i in range (lenL // 2):
            L[i], L[lenL - 1 - i]  = L[lenL - 1 - i], L[i]
        for i in range (lenL):
            deep_reverse(L[i])
    

L = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L)
print (L)
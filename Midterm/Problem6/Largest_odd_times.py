# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:03:50 2017

@author: quang
"""
L = [2, 3, 2, 2, 4, 3, 5, 6, 2]
'''def sort (L):
    """ L is a non-empty list of ints, Use bouble sort algorithm 
    Sort from high to low
    """
    l = len (L)
    for i in range (l):
        for j in range (l - 1, i - 1, -1):
            if L[j] > L[j - 1]:
                (L[j], L[j - 1]) = (L[j - 1], L[j])
    return L'''
def isOdd (n):
    return (n % 2 == 1)
def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """      
    #L2 = sort(L)
    L2 = sorted(L)
    l2 = len (L2)
    num = 1
    for i in range (l2):
        if i == l2 - 1:
            if isOdd (num) == True:
                return L2[i]
        elif L2[i] == L2[i + 1]:
            num += 1
        else:
            if isOdd (num) == True:
                return L2[i]
            num = 1

num = largest_odd_times(L)
print (num)
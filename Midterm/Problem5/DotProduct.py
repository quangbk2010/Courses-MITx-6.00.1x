# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 17:58:43 2017

@author: quang
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    lenA = len (listA)
    lenB = len (listB)
    sum = 0
    for i in range(lenA):
        sum += listA[i] * listB[i]
        '''for j in range (lenB):
            if j == i:
                sum += listA[i] * listB[j]
                break'''
    return sum

listA = [1, 2, 3]
listB = [4, 5, 6]
print (dotProduct(listA, listB))
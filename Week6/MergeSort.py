# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 09:38:05 2017

@author: quang
"""

def merge (left, right):
    '''
        left, right: sorted lists to be merged
        Returns: the merged list
    '''
    result = []
    i = j = 0
    len_left = len (left)
    len_right = len(right)
    while i < len_left and j < len_right:
        if left[i] < right[j]:
            result.append (left[i])
            i += 1
        else:
            result.append (right[j])
            j += 1
    while i < len_left:
        result.append (left[i])
        i += 1
    while j < len_right:
        result.append (right[j])   
        j += 1
    return result
    
def merge_sort (L):
    len_L = len (L)
    if len_L < 2:
        return L
    else:
        middle = len_L // 2
        left = merge_sort (L[:middle])
        right = merge_sort (L[middle:])
        return merge (left, right)
        
L = [3, 4, 2, 5, 1]
sorted_L = merge_sort (L)
print (sorted_L)
        
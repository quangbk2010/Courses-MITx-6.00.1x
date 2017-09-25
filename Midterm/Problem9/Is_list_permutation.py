# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 17:32:11 2017

@author: quang
"""

def compare_2_dict (d1, d2):
    '''
    d1, d2: Assumes 2 non-empty dictionaries contain interger -> interger
    Returns True if d1==d2, else False
    '''
    for key in d1.keys():
        val2 = d2.get (key, None)
        if val2 == None or d1[key] != val2:
            return False
    return True
    
'''def sort (L):
    """ L is a non-empty list of ints, Use bouble sort algorithm 
    Sort from low to high
    """
    l = len (L)
    for i in range (l):
        for j in range (l - 1, i - 1, -1):
            if L[j] < L[j - 1]:
                (L[j], L[j - 1]) = (L[j - 1], L[j])
    return L

def convert_list_to_dict(L):
    """ Assumes L is a non-empty list of ints
        Returns the dictionary that contains entry: from interger -> the number of times that this interger appears """      
    dup_L = detach_list (L)
    ret_d = {}
    
    for lst in dup_L:
        sorted_lst = sort(lst)
        l = len (sorted_lst)
        num = 1
        d = {}
        for i in range (l):
            if i == l - 1:
                d[sorted_lst[i]] = num
                break
            if sorted_lst[i] == sorted_lst[i + 1]:
                num += 1
            else:
                d[sorted_lst[i]] = num
                num = 1
        ret_d.update (d)
    return ret_d
''' 
def convert_list_to_dict(L):
    """ Assumes L is a non-empty list of ints
        Returns the dictionary that contains entry: from interger -> the number of times that this interger appears """      
    d = {}
    for item in L:
        d[item] = d.get (item, 0) + 1
    return d

def find_max_val (d):
    '''
    Assumes d is a non-empty dictionary, return the first finding key that has the biggest value
    '''
    maxVal = 0
    ret_key = None
    for key in d.keys():
        if d[key] > maxVal:
            ret_key = key
            maxVal = d[key]
    return (ret_key, maxVal)
    
'''def detach_list (L):
    int_L = []
    str_L = []
    for item in L:
        if type (item) == int:
            int_L.append (item)
        else:
            str_L.append (item)            
    return (int_L, str_L)
'''
        
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    len1 = len (L1)
    len2 = len (L2)
    if len1 == 0 and len2 == 0:
        return (None, None, None)
    # Otherwise
    if len1 != len2:
        return False
    d1 = convert_list_to_dict(L1)
    d2 = convert_list_to_dict(L2)
    #print (d1)
    #print (d2)
    #print (find_max_val (d1))
    if compare_2_dict (d1, d2) == True:
        tup = find_max_val (d1)
        return tup + (type(tup [0]), )
    else:
        return False
        
    
L1 = [1, 2, '5', 2, 5, 3, 4, 4, 5, 5, 6]
L2 = [1, 2, '5', 2, 5, 3, 4, 4, 5, 5, 6]
#print (convert_list_to_dict (L1))
print (is_list_permutation(L1, L2))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 10:32:57 2017

@author: quangbk2010
"""

def find_commonkeys (d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a list of keys that are keys in both d1 and d2
    '''
    if len (d1) == 0 or len (d2) == 0:
        return []
    L = []
    ''' 1st way
    for k1 in d1.keys():
        for k2 in d2.keys():
            if (k2 == k1) and (k2 not in L):
                L.append (k2)
                
    return L
    '''
    # 2nd way:
    ret_L = []
    for k in d1.keys():
        if k not in L:
            L.append (k)
    for k in d2.keys():
        if k in L:
            ret_L.append (k)    
    return ret_L
    

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of 2 dictionaries:
    - intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2. To get the values of the intersect dictionary, look at the common keys in d1 and d2 and apply the function f to these keys' values -- the value of the common key in d1 is the first parameter to the function and the value of the common key in d2 is the second parameter to the function. Do not implement f inside your dict_interdiff code -- assume it is defined outside.
    - difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears only in d1 and not in d2 or (b) every key-value pair in d2 whose key appears only in d2 and not in d1.
    
    Exp.
    If f(a, b) returns a + b
    d1 = {1:30, 2:20, 3:30, 5:80}
    d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
    then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
    
    If f(a, b) returns a > b
    d1 = {1:30, 2:20, 3:30}
    d2 = {1:40, 2:50, 3:60}
    then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})
    '''
    L = find_commonkeys (d1, d2)
    tup = ()
    inter_d = {}
    diff_d = {}
    for item in L:
        inter_d[item] = f(d1[item], d2[item])
    tup += (inter_d,)
    
    for k in d1.keys():
        if k not in L:
            diff_d[k] = d1[k]
    for k in d2.keys():
        if k not in L:
            diff_d[k] = d2[k]
    tup += (diff_d,)
    return tup

def f(a, b):
    return a > b

d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print (dict_interdiff(d1, d2))

    
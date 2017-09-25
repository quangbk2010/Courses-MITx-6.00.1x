# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:07:50 2017

@author: quang
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    Here are two examples:
        If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
        If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
        If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
    '''
    if len (d) == 0:
        return d
    # Otherwise
    inv_d = {} # A dictionary used to contain the inverted dictionary
    val_L = [] # A list used to store unique values of dictionary d.
    
    # Store the remain dictionary (except the inspecting entry)
    remain_d = d.copy ()
    # Go through all values in dictionary d
    for key in d.keys():
        key_L = [] # A list used to store all keys of d that those values equal to val0
        # Backup the inspecting value and then remove the inspecting entry
        temp_val = remain_d[key]
        del remain_d[key]
        if temp_val not in val_L:
            key_L.append (key)
            # Append an inverted entry into inv_d
            inv_d[temp_val] = find_match (temp_val, val_L, key_L, remain_d)
    return inv_d

def sort (L):
    ''' L is a non-empty list of ints, Use bouble sort algorithm 
    Sort from low to high
    '''
    l = len (L)
    for i in range (l):
        for j in range (l - 1, i - 1, -1):
            if L[j] < L[j - 1]:
                (L[j], L[j - 1]) = (L[j - 1], L[j])
    return L
    
def find_match (val0, val_L, key_L, d):
    ''' 
    val0: any type
    val_L: A list contains all the inspected values and we will not examine again
    key_L: A list that contains all keys of d that those values equal to val0
    d: dictionary - store the remain dictionary
    Returns a dictionary that have 1 entry with key is val0, value is a list of key in d that have value is val0
    '''
    # if d is empty or the reference value val0 is inspected before then don't examine anymore
    if (len (d) == 0) or (val0 in val_L):
        return key_L
    # Otherwise
    # Go through all values in dictionary d to check if an entry has value equal to val0
    for key in d.keys():
        if d[key] == val0:
            key_L.append (key)
    # append val0 into the list val_L
    val_L.append (val0)
    return sort (key_L)
        
d = {8: 6, 2: 6, 4: 6, 6: 6} #{1: 0, 2: True, 3: True, 4: True}
dic = dict_invert(d)
print ('***')
print (dic)        
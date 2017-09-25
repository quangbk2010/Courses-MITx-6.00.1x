#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 16:12:50 2017

@author: quangbk2010
"""

def flat(aList):
    
    global ret_L
    if type (aList) != list:
        ret_L.append (aList)
        return ret_L
    if len (aList) == 0:
        return []
    for L in aList:
        flat (L)
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    For example, 
    [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5]
    '''
    if len (aList) == 0:
        return []
    
    global ret_L 
    ret_L = []
    flat (aList)
    return ret_L

L = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print (flatten (L))
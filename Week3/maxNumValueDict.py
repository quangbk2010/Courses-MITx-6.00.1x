#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 22:58:56 2017

@author: quangbk2010
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    preNum = 0
    keyList = aDict.keys()
    retKey = None
    for key in keyList:
        num = len (aDict[key])
        print (num)
        if num > preNum:
            preNum = num
            retKey = key
        
    return retKey 
'''    preNum = 0
    keyList = aDict.keys()
    retVal = None
    retKey = None
    for key in keyList:
        num = len (aDict[key])
        if num > preNum:
            preNum = num
            retKey = key
    if preNum > 0:
        retVal = preNum
        
    return retKey 
(retKey, retVal)'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 22:35:44 2017

@author: quangbk2010
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    num = 0
    valList = aDict.values()
    for value in valList:
        num += len (value)
    return num

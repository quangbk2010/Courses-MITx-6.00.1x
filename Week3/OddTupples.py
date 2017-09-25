#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 01:02:22 2017

@author: quangbk2010
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    lenTup = len (aTup)
    i = 0
    oddTup = ()
    while i < lenTup:
        oddTup = oddTup + (aTup[i],)
        i += 2
    return oddTup

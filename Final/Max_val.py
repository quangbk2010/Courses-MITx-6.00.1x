#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 10:40:33 2017

@author: quangbk2010
"""

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t 
    For example,

        max_val((5, (1,2), [[1],[2]])) returns 5.
        max_val((5, (1,2), [[1],[9]])) returns 9.    
    """ 
    L = []
    
    def inspect_seq(element):
        if type (element) == int:
            L.append (element)
        else:
            for e in element:
                inspect_seq (e)
            
    inspect_seq (t)
    if len (L) > 0:
        return max (L)
    
    
print (max_val(() ) )
print (max_val((5, (1,2), [[1],[9]])) )
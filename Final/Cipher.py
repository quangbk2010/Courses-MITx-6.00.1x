#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 10:57:33 2017

@author: quangbk2010
"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. 
    Exp.
            cipher("abcd", "dcba", "dab") returns (order of entries in dictionary may not be 
            the same) ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')
    """
    d = {}
    decoded = ''
    
    length = len (map_from)
    for i in range (length):
        d[map_from[i]] = map_to [i]
    
    for c in code:
        for key in d.keys():
            if d[key] == c:
                decoded += key
    return (d, decoded)

print (cipher("abcd", "dcba", "dab"))
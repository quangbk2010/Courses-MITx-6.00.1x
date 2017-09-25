#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:36:33 2017

@author: quangbk2010
"""

def sum_digits(s):
    ''' Assumes s is a string
        Returns: an int that is the sum of all digits in s.
            If there are no digits in s, it raises a ValueError exception.
    '''
    digits = '0123456789'
    sum = 0
    len_s = len (s)
    error = True
    
    if len_s > 0:
        for c in s:
            if c in digits:
                sum += int (c)            
                error = False
    
    if error == True:
        raise ValueError
    
    return sum
              
s1 = ''
s2 = '123.,po9l'
s3 = '0'
s4 = 'cds'
s5 = '52734'
            
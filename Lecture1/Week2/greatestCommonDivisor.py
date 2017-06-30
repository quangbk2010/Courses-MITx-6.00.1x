#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 18:00:17 2017

@author: quangbk2010
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:

    If b = 0, then the answer is a

    Otherwise, gcd(a, b) is the same as gcd(b, a % b) 
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

"""
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == 1 or b == 1:
        return 1
    elif a > b:
        test = b
    else:
        test = a
    while test >= 1:
        if a % test == 0 and b % test == 0:
            return test
        else:
            test -= 1
"""
    
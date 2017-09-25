# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 15:46:39 2017

@author: quang
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def f (x):
        sum = 0
        n = len (L)
        for i in range(n):
            sum += L[i] * (x ** (n - 1 - i))
        return sum
    return f


            
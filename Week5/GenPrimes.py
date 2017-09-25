#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 15:07:03 2017

@author: quangbk2010
"""
# First way
#==============================================================================
# def isPrime(n):
#     for i in range (2, n // 2 + 1):
#         if n % i == 0:
#             return False
#     return True
# def genPrimes():
#     n = 2
#     yield n
#     while True:
#         n += 1
#         if isPrime(n):
#             yield n
# 
#==============================================================================
def genPrimes():
    n = 2
    yield n
    while True:
        n += 1
        L = []
        for i in range (2, n // 2 + 1):
            L.append (n % i != 0)
        if all (L):
            yield n
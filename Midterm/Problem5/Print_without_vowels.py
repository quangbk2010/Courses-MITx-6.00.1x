# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 13:51:38 2017

@author: quang
"""

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    lowVowels = 'aeiou'
    upVowels = 'AEIOU'
    returnStr = ''
    if len(s) != 0:
        for c in s:
            if (c not in lowVowels) and (c not in upVowels):
                returnStr += c
    print (returnStr)
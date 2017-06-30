# -*- coding: utf-8 -*-
"""
NNQuang - 12/June/2017

Input: Assume s is a string of lower case characters.

Output: counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 

For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
"""

s = 'aaaaaaaa'
num = 0
for c in s:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
       num += 1

print ("Number of vowels: " + str (num))
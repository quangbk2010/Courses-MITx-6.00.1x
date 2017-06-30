# -*- coding: utf-8 -*-
"""
NNQuang - 12/June/2017

Input: Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""

s = 'bobob'
num = 0
l = len (s)
for i in range (l):
    if (i + 2) <= (l - 1) and s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b':
       num += 1
       

print ("Number of vowels: " + str (num))
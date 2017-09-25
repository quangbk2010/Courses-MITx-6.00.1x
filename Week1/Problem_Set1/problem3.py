# -*- coding: utf-8 -*-
"""
NNQuang - 12/June/2017

Input: Assume s is a string of lower case characters.

Output: Write a program that prints the longest substring of s in which the letters occur 
in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. 
If you've spent more than a few hours on this problem, we suggest that you move on to 
a different part of the course. If you have time, come back to this problem after you've had 
a break and cleared your head.
"""

s = 'azcbobobegghakl'
"s = 'az'"
s = 'abcbcd'
num = 1
index = 0
maxi = 1
temp_max = 1
l = len (s)
for i in range (l):
    if (i + 2) <= l and s[i] <= s[i + 1]:
        num += 1
        print (str(num) +  "--" + str (i))
    else:
        temp_max = num  
        num = 1
        print ("-----------")
    if temp_max > maxi:
            maxi = temp_max
            index = i - maxi + 1
            print ("maxi = " + str(maxi) + " index = " + str (index) + " i = " + str (i)) 
            
    

print ("Longest substring in alphabetical order is: " + s [index:(index + maxi)])
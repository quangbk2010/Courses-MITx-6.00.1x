# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 13:38:49 2017

@author: quang
"""

def is_triangular(k):
    """
    k: a positive integer
    returns True if k is triangular and False if not
    """
    if k == 1:
        return True
    else:
        n = round (k / 2) + 2
        sum = 0
        for i in range (1, n):
            sum += i
            if (sum == k):
                return True
            elif (sum > k):
                return False

for i in range(100):
    check = is_triangular (i)
    if check == True:
        print (str(i) + ': 1')
    elif check == False:
        print (str(i) + ': 0')
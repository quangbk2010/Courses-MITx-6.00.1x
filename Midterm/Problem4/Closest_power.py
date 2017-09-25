# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 17:18:24 2017

@author: quang
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    if num < base:
        return 0
    power = base
    temp_power = power
    num = int (num)
    for i in range (1, num):
        power *= base
        if power - num > 0:
            if abs(power - num) < abs(temp_power - num):
                return (i + 1)
            return i
        temp_power = power

cp = closest_power(4,1)
print (cp)
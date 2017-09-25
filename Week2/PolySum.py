#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 00:33:33 2017

@author: quangbk2010
"""

from math import tan, pi

def polysum (n, s):
    '''
    Regular Polygons: polysum

    A regular polygon has 'n' number of sides. Each side has length 's'.

    * The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
    * The perimeter of a polygon is: length of the boundary of the polygon

    Write a function called 'polysum' that takes 2 arguments, 'n' and 's'. 
    This function should sum the area and square of the perimeter of 
    the regular polygon. The function returns the sum, rounded to 4 decimal places.
    '''
    'Area of a regular polygon'
    area = (0.25 * n * (s ** 2)) / (tan(pi/n))
    
    'The perimeter of a polygon is: length of the boundary of the polygon'
    perimeter = n * s
    perimeter2 = perimeter ** 2
    
    'Return the sum, rounded to 4 decimal'
    return round ((area + perimeter2), 4)
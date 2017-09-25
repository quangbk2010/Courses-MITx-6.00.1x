#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 10:57:23 2017

@author: quangbk2010
"""

def inputInterger ():
    while True:
        try:
            enter = input ('Enter an interger: ')
            i = int (enter)
            break
        except ValueError:
            print ('Input is not an interger, please reenter!')
    print ('Input correctly an interger!')

inputInterger ()
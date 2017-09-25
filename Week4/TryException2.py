#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 11:00:16 2017

@author: quangbk2010
"""
data = []
def controlInput ():    
    filename = input ('Provide a filename: ')
    try:
        f = open (filename, 'r')
    except IOError:
        print ('Cannot open', filename)     
    else:
        for line in f:
            if line != '\n':
                listData = line[:-1].split (',') # don't care the last character
                data.append (listData)
    #finally:
        f.close()
        print ('Close file', filename)

controlInput ()          
print (data)      

gradeData = []

for student in data:
    try:
        name = student[:-1]
        grade = int (student[-1])
        gradeData.append ([name, [grade]])
    except ValueError:
        gradeData.append ([student[:], []])

print (gradeData)
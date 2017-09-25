#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:22:33 2017

@author: quangbk2010
"""

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

''' Write class Bag:
 For example,

    d1 = Bag()
    d1.insert(4)
    d1.insert(4)
    print(d1)
    d1.remove(2)
    print(d1)

 prints

    4:2
    4:2

 For example,

    d1 = Bag()
    d1.insert(4)
    d1.insert(4)
    d1.insert(4)
    print(d1.count(2))
    print(d1.count(4))

 prints

    0
    3

 For example,
    
    a = Bag()
    a.insert(4)
    a.insert(3)
    b = Bag()
    b.insert(4)
    print(a+b)
    
 prints
    
    3:1
    4:2


'''

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        try:
            self.vals[e] -= 1
        except:
            pass

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        
        for key in self.vals.keys():
            if key == e:
                return self.vals[key]
        
        return 0
    def __add__ (a, b):
        c = Bag()
        for key in a.vals.keys():
            c.vals[key] = a.vals[key]
        
        for key in b.vals.keys():
            '''if key not in c.vals.keys():
                c.vals[key] = b.vals[key]
            else:
                c.vals[key] += b.vals[key]'''
            try:
                c.vals[key] += b.vals[key]
            except:
                c.vals[key] = b.vals[key]
            
            return c

'''
    Write a class:
 For example,

    d1 = ASet()
    d1.insert(4)
    d1.insert(4)

    d1.remove(2)
    print(d1)

    d1.remove(4)
    print(d1)

 prints

    4:2 # from d1.remove(2) print

        # (empty) from d1.remove(4) print

 For example,

    d1 = ASet()
    d1.insert(4)
    print(d1.is_in(4))
    d1.insert(5)
    print(d1.is_in(5))
    d1.remove(5)
    print(d1.is_in(5))

 prints

    True
    True
    False


'''

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        try:
            self.vals.pop (e)
        except:
            pass

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        for key in self.vals.keys():
            if e == key:
                return True
        
        return False
    
d1 = ASet()
d1.insert(4)
print(d1.is_in(4))
d1.insert(5)
print(d1.is_in(5))
d1.remove(5)
print(d1.is_in(5))

        
        
        
        
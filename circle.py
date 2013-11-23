#!/usr/bin/env python

"""
Circle lab 2, 2013-11-19

Extend your Circle class:
Add __str__ and __repr__ methods
Write an __add__ method so you can add two circles (and multiply by a number....)
In [22]: c1 = Circle(3)
In [23]: c2 = Circle(4)
In [24]: c3 = c1+c2
In [25]: c3.radius
Out[25]: 7
In [26]: c1*3
Out[26]: Circle(9)
If you have time: compare them... (c1 > c2, etc) code/circle.py and code/test_circle2.py
"""

import math

class Circle(object):
    def __init__(self, radius):
    	self.radius = radius

    def _get_diameter(self):
    	return self.radius * 2

    def _set_diameter(self, diameter):
    	self.radius = diameter / 2

    diameter = property(_get_diameter, _set_diameter, doc = "Diameter")

    def _get_area(self):
    	return math.pi*(self.radius**2)

    area = property(_get_area, doc = "Area")

    def d_to_r(klass, diameter):
    	return klass (diameter / 2)
    	d_to_r = classmethod(d_to_r)

    def __str__(self):
        return "Circle with radius: %f"%self.radius

    def __repr__(self):
        return "Circle(%d)"%self.radius

    def __add__(self, new):
        return Circle(self.radius + new.radius)

    def __mul__(self, number):
        return Circle(self.radius * number)

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius


    


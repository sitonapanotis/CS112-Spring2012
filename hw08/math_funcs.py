#!/usr/bin/env python

import math

# Distance formula
#   calculate a function called "distance" to calculate the distance between two points.
#   http://www.purplemath.com/modules/distform.htm
#   ex: 
#      >>> distance((0,0), (3,4))
#      5

def distance(a, b):
    vert = a[0] - b[0]
    horz = a[1] - b[1]
    dist = math.sqrt(vert**2 + horz**2)
    print "the distance b/w point %s and point %s is %i" % (a , b, dist)
    return dist

distance((1,1),(2,1))
# ADVANCED
# Normalizing Vectors
#   normalize a vector of length N.  If given all zeros, just spit back the same vector
#   http://www.fundza.com/vectors/normalize/index.html

#   ex:
#     >>> normalize((1,1))
#     [0.70710678118654746, 0.70710678118654746]
#     >>> normalize([0,0,0])
#     [0,0,0]
#     >>> normalize([1,1,1,1])
#     [0.25, 0.25, 0.25, 0.25]

# def normalize(vec):

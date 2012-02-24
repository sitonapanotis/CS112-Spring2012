#!/usr/bin/env python

# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements
#
#  ex:
#   >>> greeter("paul")
#   hello, paul
#   >>> greeter(3)
#   hello, 3
#   >>> greeter("WORLD")
#   hello, world

def greeter(name):
    name = str(name)
    name = name.lower()
    print "hello, %s" % name
    return

greeter("otis")


# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements
#
#  ex:
#    >>> box("apples", -3)
#    Error: Invalid Dimensions
#    >>> box(1,1)
#    +
#    >>> box(4,2)
#    +--+
#    +--+
#    >>> box(3,3)
#    +-+
#    | |
#    +-+

def box(w,h):
    width = w
    height = h
    
    if type(width) == int and type(height) == int:
        itr = height-2
        dash = "-"*(width-2)
        if width > 1 and height > 1:
        
        
            if width >= 2:
                print "+%s+" % dash
            else:
                print "+"
            while itr > 0:
                space = " "*(w-2)
                print "|%s|" % space
                itr -= 1
            if width >= 2:
                print "+%s+" % dash
    
            else:
                print
        elif width == 1:
            print "+"
            while itr > 0:
                print "|"
                itr -= 1
            if height > 1:
                print "+"
        elif height == 1:
            print "+%s+" % dash
        else:
            print "Error: Invalid Dimensions"
    else:
        print "Error: Invalid Dimensions"
    return
box(1,3)

# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

# def tree()


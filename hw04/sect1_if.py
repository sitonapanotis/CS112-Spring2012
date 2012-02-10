#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)
x = n % 2

if x == 0:
    print "1.", n, "is even"

else:
    print "1.", n, "is odd"




# 2. If n is odd, double it

if x > 0:
    dub = 2 * n
    print "2.", n,"doubled is", dub

else:
    print "2.", n,"is even, so no function was performed"


# 3. If n is evenly divisible by 3, add four

toAdd = n % 3

if toAdd == 0:
    toAdd = n + 4
    print "3.", n, "is devisible by three.", n,"+ 4 =", toAdd

else:
    print "3.", n,"is not divisible by three"


# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)

if grade > 89:
    print "4.", grade, "is an A"
elif grade > 79:
    print "4.", grade, "is a B"
elif grade > 69:
    print "4.", grade, "is a C"
elif grade > 64:
    print "4.", grade, "is a D"
else:
    print "4.", grade, "is a F"


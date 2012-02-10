#!/usr/bin/env python
from hwtools import *

print "Section 2:  Loops"
print "-----------------------------"

# 1. Keep getting a number from the input (num) until it is a multiple of 3.
mod = 1

while mod > 0:
    num = int(raw_input("enter a number: "))
    mod = num % 3


print "1.", num, "is a multipule of 3"

# 2. Countdown from the given number to 0 by threes. 
#    Example:
#      12...
#      9...
#      6...
#      3...
#      0

print "2. Countdown from", num, "by threes"
print str(num) + "..."
while num > 3:
    num -= 3
    print str(num) + "..."
print "0"

# 3. [ADVANCED] Get another num.  If num is a multiple of 3, countdown 
#    by threes.  If it is not a multiple of 3 but is even, countdown by 
#    twos.  Otherwise, just countdown by ones.

# num = int(raw_input("3. Countdown from: "))


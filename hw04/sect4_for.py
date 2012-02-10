#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?
total = 0
for x in nums:
    total = total + x
print total


# 2. Print every even number in nums
print "2. even numbers"
evens = [ ]
mod = 1
for x in nums:
    mod = x % 2
    if mod == 0:
        print x
        evens.append(x)

# 3. Does nums only contain even numbers? 
only_even = False
levens = len(evens)
ltot = len(nums)
if levens == ltot:
    only_even = True
    

print "3.",
if only_even == True:
    print "only even"
else:
    print "some odd"


# 4. Generate a list every odd number less than 100. Hint: use range()
print "4.", __
odds = range(1, 101, 2)
print odds
# 5. [ADVANCED]  Multiply each element in nums by its index
print "5.", __

#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

nums = input_nums()
nums = sorted(nums)
print "I have sorted your numbers", nums
xFind = int(raw_input("Which number should I find: "))
lom = 0
lenM = len(nums)-1

while lenM >= lom:
    md = lenM + lom/2
    if nums[md] == xFind:
        break
    elif xFind > nums[md]:
        lom = md+1
    else:
        lenM -= 1
if nums[md] == xFind:
    print "Found", xFind, "at position", md
else:
    print "Could not find", xFind

#!/usr/bin/env python
from random import randint
s=1
inNumber = int(raw_input("type"))
rr=[]
for num in range(inNumber):
    rr.append(randint(0,20))
print rr
"""
while s:
    s=0
    for var in range(1,inNumber):
        if rr[var-1]>rr[var]:
            t1=rr[var-1]
            t2=rr[var]
            rr[var-1]=t2
            rr[var]=t1
            s=1
print rr
"""

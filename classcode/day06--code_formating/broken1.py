#!/usr/bin/env python

total = 0
inputList = []
inputNumber = None

#get list of numbers from user
while inputNumber != "":
    inputNumber = raw_input("type")
    if inputNumber.isdigit():
        inputList.append(float(inputNumber))

#total the list of numbers
for num in inputList:
    total += num

#print average of list
print total/len(inputList)

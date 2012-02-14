#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""

stoneNumb = int(raw_input("input total stones: "))
maxTake = int(raw_input("input max number of stones to take per turn: "))
pTurn = 1
lessTotal = 0
print "started a new game"
print "number of sto es in the pile:", stoneNumb
print "the max number of stones a player can take each turn is:", maxTake

while stoneNumb > 0:
    inPrompt = str(stoneNumb) + " stones left. player " + str(pTurn) + " [1-" + str(maxTake) + "]:"
    while lessTotal == 0:
        pInput = int(raw_input(inPrompt))
        if maxTake >= pInput >= 1:
            lessTotal = pInput    
        else:
            print "you cant take more than " + str(maxTake) + " stones"
    if stoneNumb >= lessTotal:
        stoneNumb -= lessTotal
        lessTotal = 0
        if pTurn == 1:
            pTurn = 2
        else:
            pTurn = 1
    else:
        print "not enough stones remain"
        lessTotal = 0
    

print "no stones remain, player " + str(pTurn) + " wins"        

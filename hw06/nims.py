#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""
# defines the total number of stones and the maximum amont of stones that can be take per turn and set player turn
stoneNumb = int(raw_input("input total stones: "))
maxTake = int(raw_input("input max number of stones to take per turn: "))
pTurn = 1
lessTotal = 0
print "started a new game"
print "number of stones in the pile:", stoneNumb
print "the max number of stones a player can take each turn is:", maxTake

# continue getting input till all stones are gone
while stoneNumb > 0:
    inPrompt = "%i stones left. player %i [1-%i]:" % (stoneNumb, pTurn, maxTake)
    #inPrompt = str(stoneNumb) + " stones left. player " + str(pTurn) + " [1-" + str(maxTake) + "]:"
# make sure the number input by player is not more than the max take
    while lessTotal == 0:
        pInput = int(raw_input(inPrompt))
        if maxTake >= pInput >= 1:
            lessTotal = pInput    
        else:
            #print "you cant take more than " + str(maxTake) + " stones"
            print "you cant take more than %i stones" % maxTake
# checks that there are enough stones left in the pile
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
    
# announce the winner
#print "no stones remain, player " + str(pTurn) + " wins"
print "no stones remain, player %i wins" % pTurn

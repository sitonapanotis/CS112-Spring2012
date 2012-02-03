#!/usr/bin/env python
"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""

# Step 1:
# -----------------------
# Program the following.
# 
#    $ python prissybot.py
#    Enter your name:  Paul
#   
#    PrissyBot: Hello there, Paul
#    Paul: hi bot
#    PrissyBot: You mean, "hi bot, sir!"
# 
# Make sure the user inputs their own name and responses.



# Step 2:
# -----------------------
# Keep adding to the conversation. Make sure that your program 
# includes the following:
# 
#  * get and use input from the user
#  * 3 math problems
#     * at least one should get numbers from the user
#  * at least 3 insults


# Advanced
# -------------------------
# Make sure your prissy bot uses string formatting throughout.  
# Also, create new programs for the following:
#  
#  1. draw some kind of ascii art based on user input
#  2. print a decimal/binary/hexidecimal conversion table 
#     * well formated and labeled
#     * reads 5 numbers from the input (all less than 256)
#  3. reduce a fraction
#     * read a numerator and denominator from the user
#     * ex.  6/4 = 1 2/4


userName = raw_input("Enter your name: ")

print " "

print "Prissybot: hello there,", userName

rawInputPrompt = str(userName) + ": "

response = raw_input(rawInputPrompt)

print "Prissybot: you mean", response, "sir!"

print "Prissybot: so how about some math, slug"

print "Prissybot: type yes or no, DO IT!"

yesNo = raw_input(rawInputPrompt)

if yesNo == ("yes"):
    print "Prissybot: ok greaaaaat"
elif yesNo == ("no"):
    print "Prissybot: smart one huh? well we're doing math anyway"
else:
    print "Prissybot: what? you cant even follow my simple istructions? anyway, math"
      
print "Prissybot: enter a number"

firstNumber = int(raw_input(rawInputPrompt))

print "Prissybot: you entered", firstNumber

print "Prissybot: now enter another number"

seccondNumber = int(raw_input(rawInputPrompt))

print "Prissybot: you entered", seccondNumber

print "Prissybot: hovel on the ground like the cur you are as i show you my true power!"

print "Prissybot: watch as i add these numbers together!"

print "Prissybot:", firstNumber, "+", seccondNumber, "=", firstNumber + seccondNumber

print "Prissybot: now, i will multiply them!"

print "Prissybot:", firstNumber, "*", seccondNumber, "=", firstNumber * seccondNumber

print "Prissybot: and now i will exponetiate them!"

print "Prissybot:", firstNumber, "to the power of", seccondNumber, "=", firstNumber ** seccondNumber

print "Prissybot: and for my final mathematical feat i will perform a highly complex function"

print "Prissybot: f(" + str(firstNumber) + ") = yourmomisahoe"

response = raw_input(rawInputPrompt)

print "Prissybot:", "\"" + response + "\"" "... is that so?"

print "Prissybot: smell ya later"

print "bleep bloop"


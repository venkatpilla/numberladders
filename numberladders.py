#!/usr/bin/env python3

from random import randint
import sys

"""
def createLadder(lowrange,hirange):

    number = randint(lowrange,hirange)

    for i in range(1,5):
        print i * number,

    nextnumber
"""

def simpleNumbers():
    sequence = range(1,20)



def findMissingLetter():
    alphabet = [chr(c) for c in list(range(97,123))]
    missingletterindex = randint(0,25)
    missingletter = alphabet[missingletterindex]
    alphabet[missingletterindex] = '?'
    s=" "
    print (s.join(alphabet))
    guessed_letter = input('Guess the missing letter :')
    if guessed_letter in missingletter:
       print ("Well done, you guessed correctly")
        return True
    else:
        print ("Sorry, you guessed incorrectly")
        return False




if __name__ == '__main__':
    points = 0
    #createLadder(1,5)
    while points < 10:
        givepoint = findMissingLetter()
        if givepoint:
            points += 1
        print ("You have %d points." % points)

    print ("Well done you have all the points!")
    sys.exit(0)



#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys
import re

def roll_dice():
    from random import randint
    diceNumber=randint(0,6)
    print("Your dice number is " + str(diceNumber))
    return

def another_roll():
    newNumber = raw_input("Would you like to get a new number? ")
    response = re.match('yes', newNumber, re.I)
    return response

# Gather our code in a main() function
def main():
    print("Random Dice Number Generator")
    print("\nThis program will randomly print out a number (1-6) and then ask if you want to re-roll\n")
    askAgain = True
    while askAgain:
        roll_dice()
        askAgain = another_roll()
        if not askAgain:
            break

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
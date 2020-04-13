#program to guess a number in a given range
#Author: Theresa
#07 April

from random import randint
import sys, traceback
print("Guess a number from 0 to 15")
def guess(numTrials,answer):
    if int(input())==answer:
        print("Correct.")
        print("--------SECRET NUMBER: "+ str(answer)+ " ---------")
    else:
        print("Oops. That's Incorrect.")
        if numTrials>1:
            print("Would you like to try again? Type y/n")
            if input()=="y":
                numTrials=numTrials-1
                print("Guess a number from 0 to 15. You have "+ str(numTrials)+" chances")
                guess(numTrials,answer)
            else:
                sys.exit(0)
        else:
            print("GAME OVER")
            print("The secret number is "+ str(answer))

answer = randint(0, 15)
numTrials = 3
guess(numTrials,answer)

#program to guess a word given a dictionary with a list of words
#Author: Theresa
#05 April 2020

import random
from random import seed
from random import randint
import sys, traceback

file = open("AnimalDictionary.txt","r")
list = []
for line in file.readlines():
    list.append(line.rstrip())

def playGame():
    random.shuffle(list)
    #list.reverse() #shuffle the list????keeps repeating words
    mysteryWord = random.choice(list) #generate a random word from the list   
    if len(mysteryWord)== 3:
        print(mysteryWord[0]+"_"+mysteryWord[2])
    elif len(mysteryWord)>=5: 
        mysteryIndex = randint(2, len(mysteryWord)-2) #CALCULATES NUMBER OF DASHES as mysteryIndex
        #print("number of dashes are:"+ str(mysteryIndex)) 
        seed(1)
        dashIndexes=[]
        for i in range(mysteryIndex):
            value = randint(2, len(mysteryWord)-1) #generates indexes of where dashes will appear in the word
            dashIndexes.append(value)
        
        dashIndexes.sort()
        mysteryWordArray=[]
        for p in mysteryWord:
            mysteryWordArray.append(p)
            # print("letters of mysteryWord: "+ p)
        for h in dashIndexes:
            #print("Index to be replaced: "+ str(h))
            mysteryWordArray[h]="_" 
        print(mysteryWordArray)
    else: #length of mysteryWord will be 4
        print(mysteryWord[0]+"_"+mysteryWord[2]+"_")
    guessing(3,mysteryWord)


def guessing(count,mysteryWord):
    
    print("Guess the word. You have "+ str(count) + " trials") #to decrement trials as user inputs.. ie you have 2 trials left
    userGuess = input()
    if userGuess == mysteryWord:
        print("--------Hooray you guessed correctly!!!--------")
        print()
        tryAgain()
        print("Would you like to try another word? Type y/n")
        if input()=="y":
            playGame()
            guessing(3,mysteryWord)
        else:
            sys.exit(0)
    else:
        if count>1:
            print("That's incorrect! Would you like to try again? Type y/n")
            if input()=="y":
                count = count - 1
                guessing(count,mysteryWord)
            else: 
                print("The mystery word is: "+ mysteryWord)
                sys.exit(0)
        else:
            print("--------Ooops you lose!!!!!--------")
            print("The mystery word is: "+ mysteryWord)
            print()
            tryAgain()
            

def tryAgain():
        print("Would you like to try another word? Type y/n")
        if input()=="y":
            playGame()
            guessing(3,mysteryWord)
        else:
            sys.exit(0)

playGame()


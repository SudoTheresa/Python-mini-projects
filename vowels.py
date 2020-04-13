#program to count the number of vowels in a word given by the user
#04 April 2020
#Author: Theresa Banda

import sys, traceback
word = input("Enter the word: ") #user enters the word to be checked


def vowelChecker(wordc): #checks if the word is a vowel
    count = 0
    for x in range(0, len(wordc)):
        if ((wordc[x]=="a") or (wordc[x]=="e") or (wordc[x]=="i") or (wordc[x]=="o") or (wordc[x]=="u")): #traverses through each letter in the word to check if its a vowel
            count= count + 1 #increments the counter
    print("The number of vowels in "+ wordc + " are "+ str(count)) #print the number of vowels in the word

vowelChecker(word)
while True:
    proceed = int(input ("Press 1 to try another word or 2 to abort: ")) #if the user wants to keep on trying more words 
    if proceed == 1: 
        newWord = input("Enter another word: ")
        vowelChecker(newWord)
    else:
        sys.exit(0)

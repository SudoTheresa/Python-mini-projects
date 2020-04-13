#program to mimick a lotto game
#author: Theresa
#08 April 2020

from random import randint
from random import seed

seed(1)
lottoNumbers=[]
for x in range(6): #we need 6 lotto numbers
    num = randint(0,52)
    lottoNumbers.append(num)       

print("-------------------------------------------------")
print("     WELCOME TO THE EPIC AND FAMOUS LOTTO DRAW      ")
print("-------------------------------------------------") 
print()
print("Please type in your lucky 6 numbers")

guessedNums=[]
for i in range(6):
    num=input()
    guessedNums.append(num)

#print(guessedNums)
count=0
correctNums=[]
for h in guessedNums:
    for p in lottoNumbers:
        if str(h)==str(p):
            count=count+1
            correctNums.append(h)
print("Number of correct guesses is:   "+ str(count))
print("The numbers you got correct are:      " )
print(correctNums)
print("--------------------------------------")
print()
print("THE OFFICIAL LOTTO NUMBERS DRAWN ARE:  ")
print(lottoNumbers)
print("The powerball is: "+ str(lottoNumbers[len(lottoNumbers)-1]))
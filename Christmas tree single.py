from random import randint
from time import sleep
from colorama import Fore, Back, Style
md2 = randint (1,30)

print('\033c')
for x in range(1,30,2):
    md1 =randint(1,md2)
    if x==1:
        ch= '*'
        print(Style.BRIGHT + Fore.YELLOW +"{:^40}".format(ch))
    elif md1%4==0:
        ch= 'o'
        print(Fore.RED +"{:^40}".format(ch))
    elif md1%3==0:
        ch='i'
        print(Fore.GREEN +"{:^40}".format(ch))
    else:
        ch='*'
        print(Fore.WHITE+"{:^40}".format(ch*x))
print("{:^33}".format("|||"))
print("{:^33}".format("|||"))
sleep(.75)

            

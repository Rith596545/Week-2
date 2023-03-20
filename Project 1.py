print("0. Rock\n" "1. Papper\n" "2. Scissors\n")

import random
Computer_sign =random.randint(0,3)
val=int(input("Please input your sign :"))
if val==0 and Computer_sign==1:
    print("Computer sign is :",Computer_sign)
    print(" You lost")
if val==0 and Computer_sign==2:
    print("Computer sign is :",Computer_sign)
    print(" You win")
if val==1 and Computer_sign==0:
    print("Computer sign is :",Computer_sign)
    print(" You win")
if val==1 and Computer_sign==2:
    print("Computer sign is :",Computer_sign)
    print(" You lost")
if val==2 and Computer_sign==0:
    print("Computer sign is :",Computer_sign)
    print(" You lost")
if val==2 and Computer_sign==1:
    print("Computer sign is :",Computer_sign)
    print(" You win")
if val== Computer_sign:
    print("Computer sign is :",Computer_sign)
    print(" We're equal!!!")
if val>2:
    print(" You're enter the wrong sign")
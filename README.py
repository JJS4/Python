# Python code
import random
a=random.randint(0,2)
b=input("what do you choose? type 0 for rock, 1 for papre or 2 for scissors.\n")
if b==0:
    if a==0:
        print("Draw")
    elif a==1:
        print("you loose")
    else:
        print("you win")
elif b==1:
    if a==0:
        print("you win")
    elif a==1:
        print("Draw")
    else:
        print("you loose")    
else:
    if a==0:
        print("you loose")
    elif a==1:
        print("you win")
    else:
        print("draw")                 

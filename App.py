from asyncio.windows_events import NULL
import random, sys, time, Game, Role1, Role2
role1 = Role1.Description()
challenge1_1 = Game.Challenge1_1()
print("Welcome to the game")
print(" ")
pick = int(input("Choose one role: "))
if pick == 1:
    print("\nYour choice is", Role1.name)
    role1.description()
    print("\n Are you ready to proceed to the operation?\n Type [1] if Yes or [2] if No")
    proceed = int(input())
    if proceed == 1 :
        challenge1_1.introduction()
        attempt = int(input())
        if attempt == 1:
            print("nice")
        elif attempt == 2:
            print("bad")
        else:
            print("Error")
    elif proceed == 2:
        quit()
    else:
        print("Error")
elif pick == 2:
    print("cool")
else:
    print("Error")


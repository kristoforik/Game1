from asyncio.windows_events import NULL
import random, sys, time, Game, Role1, Role2
role1 = Role1.Description()
challenge1_1 = Game.Challenge1_1()
challenge2_1 = Game.Challenge2_1()
challenge3_1 = Game.Challenge3_1()
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
        dice_roll = int(input())
        if dice_roll == 1:
            challenge1_1.success()
            print("Now, moving to the next part of the operation")
            challenge2_1.introduction()
            dice_roll = int(input())
            if dice_roll == 1:
                challenge2_1.success()
                print("Proceeding to the last task...")
                challenge3_1.inroduction()
                dice_roll = int(input())
                if dice_roll == 1:
                    challenge3_1.succes()
                elif dice_roll == 2:
                    challenge3_1.full_success()
                elif dice_roll == 3:
                    challenge3_1.fail()
                elif dice_roll == 4:
                    challenge3_1.full_fail()
            elif dice_roll == 2:
                challenge2_1.full_success()
            elif dice_roll == 3:
                challenge2_1.fail()
            elif dice_roll == 4:
                challenge2_1.full_fail()
            else:
                print("Error") 
        elif dice_roll == 2:
            challenge1_1.full_success()
        else:
            challenge1_1.fail()
    elif proceed == 2:
        quit()
    else:
        print("Error")
elif pick == 2:
    print("cool")
else:
    print("Error")


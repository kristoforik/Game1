import random, sys, time, Game, Role1, Role2
def print_slowly(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.09)
role1 = Role1.Description()
role2 = Role2.Description()
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
        roll = int(input())
        if roll == 1:
            attempt = random.randint(1,4)
            print_slowly("Your dice number is: ")
            print(attempt)
            if attempt == 1:
                challenge1_1.success()
                print("Now, moving to the next part of the operation")
                challenge2_1.introduction()
                roll = int(input())
                if roll == 1:
                    attempt = random.randint(1,4)
                    print_slowly("Your dice number is: ")
                    print(attempt)
                    if attempt == 1:
                        challenge2_1.success()
                        print("Proceeding to the last task...")
                        challenge3_1.inroduction()
                        roll = int(input())
                        if roll == 1:
                            attempt = random.randint(1,4)
                            print_slowly("Your dice number is: ")
                            print(attempt)
                            if attempt == 1:
                                challenge3_1.succes()
                            elif attempt == 2:
                                challenge3_1.full_success()
                            elif attempt == 3:
                                challenge3_1.fail()
                            else:
                                challenge3_1.full_fail()
                        else:
                            print("You left the game")
                    elif attempt == 2:
                        challenge2_1.full_success()
                        print("Proceeding to the last task...")
                        challenge3_1.inroduction()
                        roll = int(input())
                        if roll == 1:
                            attempt = random.randint(1,4)
                            print_slowly("Your dice number is: ")
                            print(attempt)
                            if attempt == 1:
                                challenge3_1.succes()
                            elif attempt == 2:
                                challenge3_1.full_success()
                            elif attempt == 3:
                                challenge3_1.fail()
                            elif attempt == 4:
                                challenge3_1.full_fail()
                        else:
                            print("You left the game")
                    elif attempt == 3:
                        challenge2_1.fail()
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
                        elif dice_roll == 3:
                            challenge2_1.full_fail()
                        else:
                            print("You left the game")
                    elif attempt == 4:
                        challenge2_1.full_fail()
                    else:
                        print("Error")
                else:
                    print("You left the game") 
            elif attempt == 2:
                challenge1_1.full_success()
                print("Now, moving to the next part of the operation\n")
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
                elif dice_roll == 3:
                    challenge2_1.fail()
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
                    elif dice_roll == 3:
                        challenge2_1.full_fail()
                elif dice_roll == 4:
                    challenge2_1.full_fail()
                else:
                    print("Error") 
            elif attempt == 3:
                challenge1_1.fail()
            else:
                print("You lef the game")
                quit()
        else:
            print("You left the game")
    elif proceed == 2:
        print("You left the game")
        quit()
    else:
        print("Error")
elif pick == 2:
    print("cool")
else:
    print("Error")


'''This module is the main module for this game. All user interaction with the game happens here.'''
import random, sys, time, Game, Role1, Role2
def print_slowly(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.07)
def print_slowly2(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.3)
'''Both functions print_slowly and print_slowly2 are dedicated to create the illusion of the text being printed real-time during this game.'''
role1 = Role1.Description() #This is a reference variable of a Decription class in Role1 module
role2 = Role2.Description() #This is a reference variable of a Decription class in Role2 module
phrases = Game.Phrases() #This is a reference variable of a Phrases class in Game module
challenge1_1 = Game.Challenge1_1() #This is a reference variable of a Challenge1_1 class in Game module
challenge2_1 = Game.Challenge2_1() #This is a reference variable of a Challenge2_1 class in Game module
challenge3_1 = Game.Challenge3_1() #This is a reference variable of a Challenge3_1 class in Game module
challenge1_2 = Game.Challenge1_2() #This is a reference variable of a Challenge1_2 class in Game module
challenge2_2 = Game.Challenge2_2() #This is a reference variable of a Challenge2_2 class in Game module
challenge3_2 = Game.Challenge3_2() #This is a reference variable of a Challenge3_2 class in Game module
print_slowly2("\u001b[1mWELCOME TO THE")
time.sleep(1)
print('''
\u001b[33m███████╗\u001b[34m██████╗░\u001b[37m██╗\u001b[34m  ░██████╗██╗███╗░░░███╗██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
\u001b[33m██╔════╝\u001b[34m██╔══██╗\u001b[37m██║\u001b[34m  ██╔════╝██║████╗░████║██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
\u001b[33m█████╗░░\u001b[34m██████╦╝\u001b[37m██║\u001b[34m  ╚█████╗░██║██╔████╔██║██║░░░██║██║░░░░░███████║░░░██║░░░██║░\u001b[37m\u001b[34m░██║██████╔╝
\u001b[33m██╔══╝░░\u001b[34m██╔══██╗\u001b[37m██║\u001b[34m  ░╚═══██╗██║██║╚██╔╝██║██║░░░██║██║░░░░░██╔══██║░░░██║░░░\u001b[31m██║\u001b[30m░░\u001b[34m██║██╔══██╗
\u001b[33m██║░░░░░\u001b[34m██████╦╝\u001b[37m██║\u001b[34m  ██████╔╝██║██║░╚═╝░██║╚██████╔╝███████╗██║░░██║░░░██║░\u001b[31m░░╚███\u001b[30m█\u001b[37m\u001b[34m█╔╝██║░░██║
\u001b[33m╚═╝░░░░░\u001b[34m╚═════╝░\u001b[37m╚═╝\u001b[34m  ╚═════╝░╚═╝╚═╝░░░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝░░░\u001b[31m╚═╝░░░░╚════╝░╚═╝░░╚═╝
\u001b[0m''')
'''phrases.rules()
time.sleep(2)'''
time.sleep(3)
phrases.plot()
time.sleep(2)
phrases.operators()
time.sleep(0.5)
pick = int(input("Choose one role: ")) #a variable for choosing a role
if pick == 1:
    print("\nYour choice is", Role1.name)
    role1.description()
    print_slowly("\n Are you ready to proceed to the operation?\n Type [1] if Yes or [2] if No ")
    proceed = int(input())
    if proceed == 1 :
        challenge1_1.introduction()
        roll = int(input())
        if roll == 1:
            attempt = random.randint(1,4)
            phrases.number()
            print(attempt)
            if attempt == 1:
                challenge1_1.success()
                phrases.next()
                challenge2_1.introduction()
                roll = int(input())
                if roll == 1:
                    attempt = random.randint(1,4)
                    phrases.number()
                    print(attempt)
                    if attempt == 1:
                        challenge2_1.success()
                        phrases.proceeding()
                        challenge3_1.inroduction()
                        roll = int(input())
                        if roll == 1:
                            attempt = random.randint(1,4)
                            phrases.number()
                            print(attempt)
                            if attempt == 1:
                                challenge3_1.succes()
                            elif attempt == 2:
                                challenge3_1.full_success()
                                Role1.defusing += 1
                                time.sleep(2)
                                role1.fdescription()
                            elif attempt == 3:
                                challenge3_1.fail()
                            else:
                                challenge3_1.full_fail()
                        else:
                            phrases.leaving()
                    elif attempt == 2:
                        challenge2_1.full_success()
                        Role1.shooting += 1
                        phrases.proceeding()
                        challenge3_1.inroduction()
                        roll = int(input())
                        if roll == 1:
                            attempt = random.randint(1,4)
                            phrases.number()
                            print(attempt)
                            if attempt == 1:
                                challenge3_1.succes()
                                role1.fdescription()
                            elif attempt == 2:
                                challenge3_1.full_success()
                                Role1.defusing += 1
                                role1.fdescription()
                            elif attempt == 3:
                                challenge3_1.fail()
                            elif attempt == 4:
                                challenge3_1.full_fail()
                        else:
                            phrases.leaving()
                    elif attempt == 3:
                        challenge2_1.fail()
                        Role1.shooting -= 1
                        roll = int(input())
                        if roll == 1:
                            attempt = random.randint(1,4)
                            phrases.number()
                            print(attempt)    
                            if attempt == 1:
                                challenge2_1.success()
                                phrases.proceeding()
                                challenge3_1.inroduction()
                                roll = int(input())
                                if roll == 1:
                                    attempt = random.randint(1,4)
                                    phrases.number()
                                    print(attempt)
                                    if attempt == 1:
                                        challenge3_1.succes()
                                        role1.fdescription()
                                    elif attempt == 2:
                                        challenge3_1.full_success()
                                        Role1.defusing += 1
                                        role1.fdescription()
                                    elif attempt == 3:
                                        challenge3_1.fail()
                                    elif attempt == 4:
                                        challenge3_1.full_fail()
                            elif attempt == 2:
                                challenge2_1.full_success()
                                Role1.shooting += 1
                                phrases.proceeding()
                                challenge3_1.inroduction()
                                roll = int(input())
                                if roll == 1:
                                    attempt = random.randint(1,4)
                                    phrases.number()
                                    print(attempt)
                                    if attempt == 1:
                                        challenge3_1.succes()
                                        role1.fdescription()
                                    elif attempt == 2:
                                        challenge3_1.full_success()
                                        Role1.defusing += 1
                                        role1.fdescription()
                                    elif attempt == 3:
                                        challenge3_1.fail()
                                    elif attempt == 4:
                                        challenge3_1.full_fail()
                            elif attempt == 3 or attempt == 4:
                                challenge2_1.full_fail()
                            else:
                                phrases.leaving()
                    elif attempt == 4:
                        challenge2_1.full_fail()
                    else:
                        print("Error")
                else:
                    phrases.leaving()
            elif attempt == 2:
                challenge1_1.full_success()
                Role1.hacking += 1
                phrases.next()
                challenge2_1.introduction()
                roll = int(input())
                if roll == 1:
                    attempt = random.randint(1,4)
                    phrases.number()
                    print(attempt)
                    if attempt == 1:
                        challenge2_1.success()
                        phrases.proceeding()
                        challenge3_1.inroduction()
                        roll = int(input())
                        if roll == 1:
                            attempt = random.randint(1,4)
                            phrases.number()
                            print(attempt)
                            if attempt == 1:
                                challenge3_1.succes()
                                role1.fdescription()
                            elif attempt == 2:
                                challenge3_1.full_success()
                                Role1.defusing += 1
                                role1.fdescription()
                            elif attempt == 3:
                                challenge3_1.fail()
                            elif attempt == 4:
                                challenge3_1.full_fail()
                        else: 
                            phrases.leaving()
                    elif attempt == 2:
                        challenge2_1.full_success()
                        Role1.shooting += 1
                        phrases.proceeding()
                        challenge3_1.inroduction()
                        roll = int(input())
                        if roll == 1:
                            attempt = random.randint(1,4)
                            phrases.number()
                            print(attempt)
                            if attempt == 1:
                                challenge3_1.succes()
                                role1.fdescription()
                            elif attempt == 2:
                                challenge3_1.full_success()
                                Role1.defusing += 1
                                role1.fdescription()
                            elif attempt == 3:
                                challenge3_1.fail()
                            elif attempt == 4:
                                challenge3_1.full_fail()
                        else:
                            phrases.leaving()
                    elif attempt == 3:
                        challenge2_1.fail()
                        Role1.shooting -= 1
                        roll = int(input())
                        if roll == 1:
                            attempt = random.randint(1,4)
                            phrases.number()
                            print(attempt)
                            if attempt == 1:
                                challenge2_1.success()
                                phrases.proceeding()
                                challenge3_1.inroduction()
                                roll = int(input())
                                if roll == 1:
                                    if attempt == 1:
                                        challenge3_1.succes()
                                        role1.fdescription()
                                    elif attempt == 2:
                                        challenge3_1.full_success()
                                        Role1.defusing += 1
                                        role1.fdescription()
                                    elif attempt == 3:
                                        challenge3_1.fail()
                                    elif attempt == 4:
                                        challenge3_1.full_fail()
                                else:
                                    phrases.leaving()
                            elif attempt == 2:
                                challenge2_1.full_success()
                                Role1.shooting += 1
                                phrases.proceeding()
                                challenge3_1.inroduction()
                                roll = int(input())
                                if roll == 1:
                                    attempt = random.randint(1,4)
                                    phrases.number()
                                    print(attempt)
                                    if attempt == 1:
                                        challenge3_1.succes()
                                        role1.fdescription()
                                    elif attempt == 2:
                                        challenge3_1.full_success()
                                        Role1.defusing += 1
                                        role1.fdescription()
                                    elif attempt == 3:
                                        challenge3_1.fail()
                                    elif attempt == 4:
                                        challenge3_1.full_fail()
                                else:
                                    phrases.leaving()
                            elif attempt == 3 or attempt == 4:
                                challenge2_1.full_fail()
                    elif attempt == 4:
                        challenge2_1.full_fail()
                    else:
                        print("Error") 
                else:
                    phrases.leaving()
            elif attempt == 3 or attempt == 4:
                challenge1_1.fail()
            else:
                phrases.leaving()
                quit()
        else:
            phrases.leaving
            quit()
    elif proceed == 2:
        phrases.leaving()
        quit()
    else:
        print("Error")
elif pick == 2:
    print("\nYour choice is", Role2.name)
    role2.description()
    print_slowly("\n Are you ready to proceed to the operation?\n Type [1] if Yes or [2] if No ")
    proceed = int(input())
    if proceed == 1 :
        challenge1_2.introduction()
        roll = int(input())
        if roll == 1:
            attempt = random.randint(1,4)
            phrases.number()
            print(attempt)
            if attempt == 1:
                challenge1_1.success()
                phrases.next()
                challenge2_1.introduction()
                roll = int(input())
                if roll == 1:
                    attempt = random.randint(1,4)
                    phrases.number()
                    print(attempt)
                    if attempt == 1:
                        challenge2_1.success()
                        phrases.proceeding()
                        challenge3_1.inroduction()
                        roll = int(input())
                        if roll == 1:
                            attempt = random.randint(1,4)
                            phrases.number()
                            print(attempt)
                            if attempt == 1:
                                challenge3_1.succes()
                            elif attempt == 2:
                                challenge3_1.full_success()
                                Role2.defusing +=  1
                                role2.fdescription()
                            elif attempt == 3:
                                challenge3_1.fail()
                            else:
                                challenge3_1.full_fail()
                        else:
                            phrases.leaving()
                    elif attempt == 2:
                        challenge2_1.full_success()
                        Role2.shooting += 1
                        phrases.proceeding()
                        challenge3_1.inroduction()
                        roll = int(input())
                        if roll == 1:
                            attempt = random.randint(1,4)
                            phrases.number()
                            print(attempt)
                            if attempt == 1:
                                challenge3_1.succes()
                                role2.fdescription()
                            elif attempt == 2:
                                challenge3_1.full_success()
                                Role2.defusing += 1
                                role2.fdescription()
                            elif attempt == 3:
                                challenge3_1.fail()
                            elif attempt == 4:
                                challenge3_1.full_fail()
                        else:
                            phrases.leaving()
                    elif attempt == 3:
                        challenge2_1.fail()
                        roll = int(input())
                        if roll == 1:
                            attempt = random.randint(1,4)
                            phrases.number()
                            print(attempt)    
                            if attempt == 1:
                                challenge2_1.success()
                                phrases.proceeding()
                                challenge3_1.inroduction()
                                roll = int(input())
                                if roll == 1:
                                    attempt = random.randint(1,4)
                                    phrases.number()
                                    print(attempt)
                                    if attempt == 1:
                                        challenge3_1.succes()
                                    elif attempt == 2:
                                        challenge3_1.full_success()
                                    elif attempt == 3:
                                        challenge3_1.fail()
                                    elif attempt == 4:
                                        challenge3_1.full_fail()
                            elif attempt == 2:
                                challenge2_1.full_success()
                                phrases.proceeding()
                                challenge3_1.inroduction()
                                roll = int(input())
                                if roll == 1:
                                    attempt = random.randint(1,4)
                                    phrases.number()
                                    print(attempt)
                                    if attempt == 1:
                                        challenge3_1.succes()
                                    elif attempt == 2:
                                        challenge3_1.full_success()
                                    elif attempt == 3:
                                        challenge3_1.fail()
                                    elif attempt == 4:
                                        challenge3_1.full_fail()
                            elif attempt == 3 or attempt == 4:
                                challenge2_1.full_fail()
                            else:
                                phrases.leaving()
                    elif attempt == 4:
                        challenge2_1.full_fail()
                    else:
                        print("Error")
                else:
                    phrases.leaving()
            elif attempt == 2:
                challenge1_1.full_success()
                Role2.hacking += 1
                phrases.next()
                challenge2_1.introduction()
                roll = int(input())
                if roll == 1:
                    attempt = random.randint(1,4)
                    phrases.number()
                    print(attempt)
                    if attempt == 1:
                        challenge2_2.success()
                        phrases.proceeding()
                        challenge3_2.inroduction()
                        roll = int(input())
                        if roll == 1:
                            attempt = random.randint(1,4)
                            phrases.number()
                            print(attempt)
                            if attempt == 1:
                                challenge3_2.succes()
                                role2.fdescription()
                            elif attempt == 2:
                                challenge3_2.full_success()
                                Role2.defusing += 1
                                role2.fdescription()
                            elif attempt == 3:
                                challenge3_2.fail()
                            elif attempt == 4:
                                challenge3_2.full_fail()
                        else: 
                            phrases.leaving()
                    elif attempt == 2:
                        challenge2_2.full_success()
                        Role2.shooting += 1
                        phrases.proceeding()
                        challenge3_2.inroduction()
                        roll = int(input())
                        if roll == 1:
                            attempt = random.randint(1,4)
                            phrases.number()
                            print(attempt)
                            if attempt == 1:
                                challenge3_2.succes()
                                role2.fdescription()
                            elif attempt == 2:
                                challenge3_2.full_success()
                                Role2.defusing += 1
                                role2.fdescription()
                            elif attempt == 3:
                                challenge3_2.fail()
                            elif attempt == 4:
                                challenge3_2.full_fail()
                        else:
                            phrases.leaving()
                    elif attempt == 3:
                        challenge2_2.fail()
                    elif attempt == 4:
                        challenge2_2.full_fail()
                else:
                    phrases.leaving()
            elif attempt == 3:
                challenge1_2.fail()
                Role2.hacking -= 1
                roll = int(input())
                if roll == 1:
                    attempt = random.randint(1,4)
                    phrases.number()
                    print(attempt)
                    if attempt == 1:
                        challenge1_2.success()
                        phrases.next()
                        challenge2_2.introduction()
                        roll = int(input())
                        if roll == 1:
                            attempt = random.randint(1,4)
                            phrases.number()
                            print(attempt)
                            if attempt == 1:
                                challenge2_2.success()
                                phrases.proceeding()
                                challenge3_2.inroduction()
                                roll = int(input())
                                if roll == 1:
                                    attempt = random.randint(1,4)
                                    phrases.number()
                                    print(attempt)
                                    if attempt == 1:
                                        challenge3_2.succes()
                                        role2.fdescription()
                                    elif attempt == 2:
                                        challenge3_2.full_success()
                                        Role2.defusing += 1
                                        role2.fdescription()
                                    elif attempt == 3:
                                        challenge3_2.fail()
                                    else:
                                        challenge3_2.full_fail()
                                else:
                                    phrases.leaving()
                            elif attempt == 2:
                                challenge2_2.full_success()
                                Role2.shooting += 1
                                phrases.proceeding()
                                challenge3_2.inroduction()
                                roll = int(input())
                                if roll == 1:
                                    attempt = random.randint(1,4)
                                    phrases.number()
                                    print(attempt)
                                    if attempt == 1:
                                        challenge3_2.succes()
                                        role2.fdescription()
                                    elif attempt == 2:
                                        challenge3_2.full_success()
                                        Role2.defusing += 1
                                        role2.fdescription()
                                    elif attempt == 3:
                                        challenge3_2.fail()
                                    elif attempt == 4:
                                        challenge3_2.full_fail()
                                else:
                                    phrases.leaving()
                            elif attempt == 3:
                                challenge2_2.fail()
                            elif attempt == 4:
                                challenge2_2.fail()
                            else:
                                print("Error")
                        else:
                            phrases.leaving()
                    elif attempt == 2:
                        challenge1_2.full_success()
                        Role2.hacking += 1
                        phrases.next()
                        challenge2_1.introduction()
                        roll = int(input())
                        if roll == 1:
                            attempt = random.randint(1,4)
                            phrases.number()
                            print(attempt)
                            if attempt == 1:
                                challenge2_1.success()
                                phrases.proceeding()
                                challenge3_1.inroduction()
                                roll = int(input())
                                if roll == 1:
                                    attempt = random.randint(1,4)
                                    phrases.number()
                                    print(attempt)
                                    if attempt == 1:
                                        challenge3_1.succes()
                                        role2.fdescription()
                                    elif attempt == 2:
                                        challenge3_1.full_success()
                                        Role2.defusing += 1
                                        role2.fdescription()
                                    elif attempt == 3:
                                        challenge3_1.fail()
                                    elif attempt == 4:
                                        challenge3_1.full_fail()
                                else: 
                                    phrases.leaving()
                            elif attempt == 2:
                                challenge2_1.full_success()
                                Role2.shooting += 1
                                phrases.proceeding()
                                challenge3_1.inroduction()
                                roll = int(input())
                                if roll == 1:
                                    attempt = random.randint(1,4)
                                    phrases.number()
                                    print(attempt)
                                    if attempt == 1:
                                        challenge3_1.succes()
                                        role2.fdescription()
                                    elif attempt == 2:
                                        challenge3_1.full_success()
                                        Role2.defusing += 1
                                        role2.fdescription()
                                    elif attempt == 3:
                                        challenge3_1.fail()
                                    elif attempt == 4:
                                        challenge3_1.full_fail()
                                else:
                                    phrases.leaving()
                            elif attempt == 3 or attempt == 4:
                                challenge2_2.fail()
                    elif attempt == 3 or attempt == 4:
                        challenge2_2.fail()
                    else:
                        print("Error") 
                else:
                    phrases.leaving()
            elif attempt == 4:
                challenge1_2.full_fail()
        else:
            phrases.leaving
            quit()
    elif proceed == 2:
        phrases.leaving()
        quit()
    else:
        print("Error")
else:
    print("Error")


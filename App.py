import random, sys, time, Game, Role1, Role2
def print_slowly(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.09)
def print_slowly2(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.5)
role1 = Role1.Description()
role2 = Role2.Description()
phrases = Game.Phrases()
challenge1_1 = Game.Challenge1_1()
challenge2_1 = Game.Challenge2_1()
challenge3_1 = Game.Challenge3_1()
challenge1_2 = Game.Challenge1_2()
challenge2_2 = Game.Challenge2_2()
challenge3_2 = Game.Challenge3_2()
print_slowly2("WELCOME TO THE GAME")
time.sleep(2)
phrases.rules()
time.sleep(2)
pick = int(input("Choose one role: "))
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
            elif attempt == 3:
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
                            elif attempt == 3:
                                challenge3_1.fail()
                            else:
                                challenge3_1.full_fail()
                        else:
                            phrases.leaving()
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
                            elif attempt == 2:
                                challenge3_2.full_success()
                            elif attempt == 3:
                                challenge3_2.fail()
                            elif attempt == 4:
                                challenge3_2.full_fail()
                        else: 
                            phrases.leaving()
                    elif attempt == 2:
                        challenge2_2.full_success()
                        phrases.proceeding()
                        challenge3_2.inroduction()
                        roll = int(input())
                        if roll == 1:
                            attempt = random.randint(1,4)
                            phrases.number()
                            print(attempt)
                            if attempt == 1:
                                challenge3_2.succes()
                            elif attempt == 2:
                                challenge3_2.full_success()
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


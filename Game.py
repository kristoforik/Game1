'''This module provides all the text and phrases required for the game.'''
import sys, time
def print_slowly(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
def print_slowly2(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.8)
'''Both functions print_slowly and print_slowly2 are dedicated to create the illusion of the text being printed real-time during this game.'''
class Challenge1_1:
    def introduction(self):
        print_slowly("The operation has started...\nThe first task is to hack the electrical system and cut the power of the building\nRoll the dice to hack the system. Type [1] to roll ")
    def success(self):
        print_slowly("Well done! You hacked electricity and now terrorists don't have light. ")
    def fail(self):
        time.sleep(1)
        print_slowly("You lost! You did not manage to hack electricity and time is out. ") 
    def full_success(self):
        print_slowly("Well done! You hacked electricity and improved your hacking abilities by 1 so that now terrorists don't have light. ")
class Challenge2_1:
    def introduction(self):
        print_slowly("Get ready your rifle! Your next task is to enter a building and kill all terrorists there...\nRoll the dice to begin an anti-terror sweep. Type [1] to roll ")
    def success(self):
        print_slowly("Good job! All terrorists are dead. ")
    def fail(self):
        time.sleep(1)
        print_slowly("Unfortunatelly, while entering the building you got injured and your ability was reduced by 1. However, due to your experience, you have the second chance to continue the mission. Type [1] to roll again ")
    def full_success(self):
        print_slowly("Great job! You killed all terrorists and improved your shooting abilities by 1. ")
    def full_fail(self):
        time.sleep(1)
        print_slowly("Unfortunatelly, you were killed and mission is lost.")
class Challenge3_1:
    def inroduction(self):
        print_slowly("You are almost there! Your final task is to crack the door and defuse the bomb attached to the hostage\nRoll the dice to begin cracking and defusing. Type [1] to roll ")
    def succes(self):
        print_slowly("YOU WON! Terrorists are dead and hostage is saved. Mission is done successfully.")
    def fail(self):
        time.sleep(1)
        print_slowly("YOU LOST! You didn't manage to defuse the bomb and exploded together with a hostage(")
    def full_success(self):
        print_slowly("YOU WON! Terrorists are dead and hostage is saved. Mission is done successfully and you improved your defusing abilities by 1.")
    def full_fail(self):
        time.sleep(1)
        print_slowly("YOU LOST! You didn't even manage to crack the door, so the building blew up")
class Challenge1_2:
    def introduction(self):
        print_slowly("The operation has started...\nThe first task is to hack electrical system and cut the power of the building\nRoll the dice to hack the system. Type [1] to roll ")
    def success(self):
        print_slowly("Well done! You hacked electricity and now terrorists don't have light. ")
    def fail(self):
        time.sleep(1)
        print_slowly("Unfortunatelly, you didn't manage to hack the system this time and your hacking abilities were reduced by 1. However, you got a new device which might help you to shut power down, you have the second chance to continue the mission. Type [1] to roll ")
    def full_fail(self):
        time.sleep(1)
        print_slowly("You lost! You did not manage to hack electricity and time is out. ") 
    def full_success(self):
        print_slowly("Well done! You hacked electricity and improved your hacking abilities by 1 so that now terrorists don't have light. ")
class Challenge2_2:
    def introduction(self):
        print_slowly("Get ready your rifle! Your next task is to enter a building and kill all terrorits there...\nRoll the dice to begin an anti-terror sweep. Type [1] to roll ")
    def success(self):
        print_slowly("Good job! All terrorists are dead.")
    def full_success(self):
        print_slowly("Great job! You killed all terrorists and improved your shooting abilities by 1. ")
    def fail(self):
        time.sleep(1)
        print_slowly("Unfortunatelly, you were killed and mission is lost. ")
    def full_fail(self):
        time.sleep(1)
        print_slowly("Unfortunatelly, you were killed and mission is lost. ")
class Challenge3_2:
    def inroduction(self):
        print_slowly("You are almost there! Your final task is to crack the door and defuse the bomb attached to the hostage\nRoll the dice to begin cracking and defusing. Type [1] to roll ")
    def succes(self):
        print_slowly("YOU WON! Terrorists are dead and hostage is saved. Mission is done successfully.")
    def fail(self):
        time.sleep(1)
        print_slowly("YOU LOST! You didn't manage to defuse the bomb and exploded together with a hostage(")
    def full_success(self):
        print_slowly("YOU WON! Terrorists are dead and hostage is saved. Mission is done successfully and you improved your defusing abilities by 1.")
    def full_fail(self):
        time.sleep(1)
        print_slowly("YOU LOST! You didn't even manage to crack the door, so the building blew up")
class Phrases:
    def leaving(self):
        print("You left the game")
    def number(self):
        print_slowly("Your dice number is: ")
        print_slowly2("... .. . ")
    def proceeding(self):
        print_slowly(" Proceeding to the last task...\n")
    def next(self):
        print_slowly("Now, moving to the next part of the operation\n")
    def rules(self):
        print_slowly("\nRules of the game:\n")
        print_slowly("Initially, you are provided with the main plot and quest for this game. Then you can choose one role to begin the game. Each role has 3 attributes, which are the same for both roles. However, each role excels at one particular attribute and has a higher value by 1, thereby having one more chance to pass the challenge.")
        print_slowly("\nYou WIN this game only if you pass all 3 tasks")
        time.sleep(2)
        print_slowly("\nAll possible outcomes of a dice are 1, 2, 3, 4... Victory is 1 & 2. Defeat is 3 & 4. By having 2, you increase your abilities by 1, by having 3 you decrease your abilities by 1.")
        time.sleep(1)
        print_slowly("\nGameplay:\n")
        print_slowly("The main inputs for this game are [1] and [2]. Firstly, you will be asked to choose a role by typing 1 or 2. Then before each task you will be asked to type [1] to roll the dice and get your number.\n")
    def plot(self):
        print_slowly("\nStory:\n")
        time.sleep(1)
        print_slowly("Washington, D.C.\n")
        time.sleep(0.5)
        print_slowly("Terrorists have broken into an Amazon office and captured one hostage, the head of the office.")
        print_slowly("\nThe goal of the operation is to enter a building, sweep it from terrorists and save the hostage.")
    def operators(self):
        print_slowly("\nYou can choose one between two FBI operators to start the operation")
        time.sleep(0.5)
        print_slowly("\n[1] John (rifleman) ")
        print_slowly("\n[2] Roger (hacker) \n")
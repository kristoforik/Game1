class Challenge1_1:
    def introduction(self):
        print("The operation has started...\nThe first task is to hack electrical system and cut the power of the building\nRoll the dice to hack the system. Type [1] to roll")
    def success(self):
        print("Well done! You hacked electricity and now terrorists don't have light.")
    def fail(self):
        print("You lost! You did not manage to hack electricity and time is out.") 
    def full_success(self):
        print("Well done! You hacked electricity and improved your hacking abilities by 1 so that now terrorists don't have light.")
class Challenge2_1:
    def introduction(self):
        print("Get ready your rifle! Your next task is to enter a building and kill all terrorits there...\nRoll the dice to begin an anti-terror sweep. Type [1] to roll")
    def success(self):
        print("Good job! All terrorists are dead.")
    def fail(self):
        print("Unfortunatelly, while entering the building you got injured and your ability was reduced by 1. However, due to your experience, you have the second chance to continue the mission.")
    def full_success(self):
        print("Great job! You killed all terrorists and improved your shooting abilities by 1.")
    def full_fail(self):
        print("Unfortunatelly, you were killed and mission is lost.")
class Challenge3_1:
    def inroduction(self):
        print("You are almost there! Your final task is to crack the door and defuse the bomb attached to the hostage\nRoll the dice to begin cracking and defusing. Type [1] to roll")
    def succes(self):
        print("Awesome, YOU WON! Terrorists are dead and hostage is saved. Mission is done successfully.")
    def fail(self):
        print("YOU LOST! You didn't manage to defuse the bomb and exploded together with a hostage(")
    def full_success(self):
        print("YOU WON! Terrorists are dead and hostage is saved. Mission is done successfully and you improved your defusing abilities by 1.")
    def full_fail(self):
        print("YOU LOST! You didn't even manage to crack the door, so the building blew up")
    
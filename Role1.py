'''This module is all about Role1 and provides all the information about it. The module contains some variables related to the first role
and functions dedicated to display its description.'''
import sys, time
def print_slowly(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
'''The function print_slowly is dedicated to create the illusion of the text being printed real-time.'''
name = 'John' #A variable for the name of the operator
age = 39 #A variable for the age of the operator
shooting = 2 #A variable for the shooting abilities of the operator
hacking = 1 #A variable for the hacking abilities of the operator
defusing = 1 #A variable for the defusing abilities of the operator
class Description:
    def description(self): #a function to display operator's description
        print_slowly("Operator's description:\n")
        print_slowly("   Name: John\n")
        print_slowly("   Age: 39\n")
        print_slowly("   Hacking: 1\n")
        print_slowly("   Shooting accuracy: 2\n")
        print_slowly("   Defusing: 1")
    def fdescription(self): #a function to display operator's final description
        print_slowly("\nOperator's final overview:\n")
        print("   Name:", name)
        print("   Age:", age)
        print("   Shooting accuracy:", shooting)
        print("   Shooting accuracy:", hacking)
        print("   Defusing:", defusing)
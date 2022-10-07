'''This module is all about Role2 and provides all the information about it. The module contains some variables related to the second role
and functions dedicated to display its description.'''
import sys, time
def print_slowly(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
'''The function print_slowly is dedicated to create the illusion of the text being printed real-time.'''
name = 'Roger'
age = 43
shooting = 1
hacking = 2
defusing = 1
class Description:
    def description(self):
        print_slowly("Operator's description:\n")
        print_slowly("   Name: Roger\n")
        print_slowly("   Age: 43\n")
        print_slowly("   Hacking: 2\n")
        print_slowly("   Shooting accuracy: 1\n")
        print_slowly("   Defusing: 1")
    def fdescription(self):
        print_slowly("\nOperator's final overview:\n")
        print("   Name:", name)
        print("   Age:", age)
        print("   Shooting accuracy:", shooting)
        print("   Shooting accuracy:", hacking)
        print("   Defusing:", defusing)
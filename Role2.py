import sys, time
def print_slowly(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
name = 'Roger'
age = 43
shooting = 1
hacking = 2
cracking = 1
class Description:
    def description(self):
        print_slowly("Operator's description:\n")
        print_slowly("   Name: Roger\n")
        print_slowly("   Age: 43\n")
        print_slowly("   Hacking: 2\n")
        print_slowly("   Shooting accuracy: 1\n")
        print_slowly("   Cracking: 1")
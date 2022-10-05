import sys, time
def print_slowly(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)
name = 'John'
age = 39
shooting = 2
hacking = 1
defusing = 1
class Description:
    def description(self):
        print_slowly("Operator's description:\n")
        print_slowly("   Name: John\n")
        print_slowly("   Age: 39\n")
        print_slowly("   Hacking: 1\n")
        print_slowly("   Shooting accuracy: 2\n")
        print_slowly("   Defusing: 1")
    def fdescription(self):
        print_slowly("\nOperator's final overview:\n")
        print("   Name:", name)
        print("   Age:", age)
        print("   Shooting accuracy:", shooting)
        print("   Shooting accuracy:", hacking)
        print("   Defusing:", defusing)
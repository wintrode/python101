import sys
import os

import adder

print("Adder: ", adder.__version__)

def main() :

    sys.stdout.write("Enter a list of numbers to add: ")
    sys.stdout.flush()
    for l in sys.stdin :
        l = l.strip()
        if len(l) == 0 :
            break

        print("Got:", l.encode('ASCII'))

        a = l.split(" ")

        print("Have:", a)

        sum = adder.add(a)
        print("Sum: ", sum)
        sys.stdout.write("Enter a list of numbers to add: ")
        sys.stdout.flush()


if __name__ == "__main__": 
    main()

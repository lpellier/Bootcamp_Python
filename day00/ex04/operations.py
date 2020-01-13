import sys
import re

def do_nothing():
    return ;

def operations(fnu, snu):
    print("Sum: ", (fnu + snu))
    print("Difference: ", (fnu - snu))
    print("Product: ", (fnu * snu))
    if snu == 0:
        print("Quotient: ERROR (div by zero)")
        print("Remainder: ERROR (modulo by zero)") 
    else:
        print("Quotient: ", (fnu / snu))
        print("Remainder: ", (fnu % snu))

if __name__ == "__main__":
    for arg in range(1, len(sys.argv)):
        if sys.argv[arg].isnumeric() == False:
            print("InputError: only numbers")
            exit(0);
        else:
            continue
    if (len(sys.argv) > 3):
        print("InputError: too many arguments")
    elif (len(sys.argv) < 3):
        print("InputError: not enough arguments")
    else: 
        operations(int(sys.argv[1]), int(sys.argv[2]))
    exit(0);

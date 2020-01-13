import sys

def main(string):
    if string.isnumeric() == False:
        print("ERROR")
    else:
        res = int(string)
        if res == 0:
            print("I'm Zero.")
        elif res % 2 == 0:
            print("I'm Even.")
        elif res % 2 != 0:
            print("I'm Odd.")

if __name__ == "__main__":
    main(sys.argv[1])

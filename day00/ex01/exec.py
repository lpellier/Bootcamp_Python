import sys

def reverse(string):
    return(string[::-1])

def char_reverse(string):
    str = ""
    for a in string:
        if a.isupper():
            str += a.lower()
        elif a.islower():
            str += a.upper()
        else:
            str += a
    return (str);

def main(string):
    tab = ""
    for arg in range(1, len(string)):
            tab += reverse(string[-arg]) + ' '
    tab = char_reverse(tab)
    print(tab[:-1])

if __name__ == '__main__':
    main(sys.argv)

import sys
import re

def sos(string):
    MORSE_CODE_DICT = { 
            'A':'.-', 'B':'-...', 
            'C':'-.-.', 'D':'-..', 'E':'.', 
            'F':'..-.', 'G':'--.', 'H':'....', 
            'I':'..', 'J':'.---', 'K':'-.-', 
            'L':'.-..', 'M':'--', 'N':'-.', 
            'O':'---', 'P':'.--.', 'Q':'--.-', 
            'R':'.-.', 'S':'...', 'T':'-', 
            'U':'..-', 'V':'...-', 'W':'.--', 
            'X':'-..-', 'Y':'-.--', 'Z':'--..', 
            '1':'.----', '2':'..---', '3':'...--', 
            '4':'....-', '5':'.....', '6':'-....', 
            '7':'--...', '8':'---..', '9':'----.', 
            '0':'-----', ', ':'--..--', '.':'.-.-.-', 
            '?':'..--..', '/':'-..-.', '-':'-....-', 
            '(':'-.--.', ')':'-.--.-'
            }


    chaine = ""
    for i in range(len(string)):
        key = string[i].upper()
        chaine += MORSE_CODE_DICT[key] + ' '
    print(chaine[:-1], "/")

if __name__ == "__main__":
    if (len(sys.argv) >= 2):
        lst = ""
        for arg in range(1, len(sys.argv)):
            lst += sys.argv[arg]
        liste = lst.split(' ')
        for i in range(len(liste)):
            sos(liste[i])
    else:
        exit(0)

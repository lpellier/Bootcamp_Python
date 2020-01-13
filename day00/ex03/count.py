import sys
import re

def output(up, lo, pu, sp):
    print("The text contains ", (up + lo + pu + sp), " characters:")
    print ("- ", up, " upper letters")
    print ("- ", lo, "lower letters")
    print ("- ", pu, "punctuation marks")
    print ("- ", sp, " spaces")

def count(string):
    upper = "[A-Z]"
    lower = "[a-z]"
    punct = "[,.?!-_]"
    spaces = "[ ]"
    up = len(re.findall(upper, string))
    lo = len(re.findall(lower, string))
    pu = len(re.findall(punct, string))
    sp = len(re.findall(spaces, string))
    output(up, lo, pu, sp)

def text_analyzer(string):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a give text.
    """
    if (len(sys.argv) != 2):
        string = input("What is the text to analyse?\n")
    if not string:
        output(0, 0, 0, 0)
    else:
        count(string)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        text_analyzer(sys.argv)
    else:
        text_analyzer(sys.argv[1])

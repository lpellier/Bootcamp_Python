import re
import sys
import string

def extract_words(string):
    extracted = re.findall(r"\w+", string)
    return (extracted)

def check_len(extracted, integer):
    return([word for word in extracted if len(word) >= integer])  
 
def filterwords(string, integer):
    extracted = extract_words(string)
    extracted = check_len(extracted, integer)
    print(extracted)

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print("ERROR")
        exit(0)
    filterwords(sys.argv[1], int(sys.argv[2]))

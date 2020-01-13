def kata_03():
    phrase = "The right format"
    for i in range(41 - len(phrase)):
        phrase = '-' + phrase
    print(phrase)

if __name__ == "__main__":
    kata_03()

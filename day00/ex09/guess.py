import sys
import random

def display_menu():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.\nGood luck!")

def guess(valeur, count):
   print("\nWhat's your guess between 1 and 99?")
   string = input(">> ")   
   if string == "exit":
       exit(0)
   else:
       for a in string:
           if a.isalpha():
               print("InputError")
               guess(valeur, count)
   choice = int(string)
   if choice > valeur:
       print("Too high!")
       count += 1
   elif choice < valeur:
       print("Too low!")
       count += 1
   elif choice == valeur:
       if valeur == 42:
           print("The answer to the ultimate question of life, the universe and everything is 42.")
       else:
           print("Congratulations, you've got it!")
       if (count == 1):
           print("Impressive! You won on your first try!")
       else:
           print("You won in", count, "attempts!")
       return(1)
   else:
       print("InputError\n")
   guess(valeur, count)

if __name__ == "__main__":
    display_menu()
    count = 1
    valeur = random.randint(1, 99)
    if guess(valeur, count) == 0:
        exit(0)

from random import *
import random

def number_game():
   
    print("********************\n WELCOME\n The number guessing game \n********************")
    print("Hello, please enter your name.")
    player_name = input()

    secret_number = random.randint(1,100)
    print("Thanks, " + player_name + ". Please enter any number between 1 and 100. Remember, you have only 5 attempts")

    
    number = random.randint(0,100)
    for i in range (4,-1,-1):
        x = int(input("Guess the number between 0 to 100: "))
        if x > number:
            print("Your guess is above the number, please guess again")
            print("Number of chances left: ",i)
        elif x == number:
            print("Yep, you guess it correct. Congrats!")
            print("Number of chances left: ",i)
            break
        else:
            print("Nope, Your guess is below the number, please guess again")
            print("Number of chances left: ",i)
    if x!=number:
        print("The Secret Number is: ",number)

if __name__ == "__main__":
    number_game()

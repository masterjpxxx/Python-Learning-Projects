# This project involves guessing a computer generated random number. 
# The program gives the user hints whether the guessed number is higher or lower

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input("Input a number: "))
        if guess < random_number:
            print("Sorry guess again. The number is too low")
        elif guess > random_number:
            print("Sorry guess again. Then number is too high!")
        
    print(f"Congratulation you guessed it right! The number is {random_number}!")
    
guess(10)
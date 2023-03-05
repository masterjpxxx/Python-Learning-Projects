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
 
#guess(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
  
    while feedback != 'c' and low != high:
        guess = random.randint(low,high)
        feedback = input(f"Is {guess} the number correct? L - for lower, H - for Higher and C - Correct: ".lower())
        if feedback == 'l':
            high = guess -1 
        elif feedback == 'h':
            low = guess + 1
            
    print(f"Congratulations! you have guessed the number which is {guess}!")

computer_guess(6)        
    

    

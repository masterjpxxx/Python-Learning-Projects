#This program is called Hangman Game, users guess the random picked word per letter
#The program outputs the letter used and what are the remaining letters guessed for each word

import random
import string
#collection of random words
words = ["field", "instrument", "mail", "miscarriage", "absent", "imposter", "attachment", "bucket", "first", "family"]

def play():
    word = random.choice(words)
    wordletters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    life = 8
    #print(wordletters)
    while life > 0 and len(wordletters) > 0:
        user_letter = input("Guess a Letter: ")
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in wordletters:
                wordletters.remove(user_letter)
            else:
                life = life - 1
        elif user_letter in used_letters:
            print("You have already used that letter!")
        else:
            print("Invalid characters! try again")
            
        print("You have used the letters: ", " ".join(used_letters))
        wordlist = [letter if letter in used_letters else '-' for letter in word]
        print(f"Remaining Lives: {life} Current word is: ", " ".join(wordlist))
    
    #print(len(wordletters))
    if len(wordletters) == 0 :
        print("Congratulations! You have guessed the correct word!")
    if life == 0:
        print("Sorry you have failed to guessed the word!")

play()
    
    
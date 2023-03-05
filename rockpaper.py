#This program is used to simulate a rock paper scissors game.
#The rules are simple Rock > Scissors, Paper > Rock, Scissors > Paper


import random

def play():
    
    choice = input("What is your choice? r-rock s-scissors p-paper: ")
    computer = random.choice(['r', 's', 'p'])
    print(computer)
    if choice == computer:
        return 'It\'s a tie!'
    if is_win(choice, computer):
        return 'You won!'
    return 'You Lost!'

def is_win(player, computer):

#Rock > Scissors, Paper > Rock, Scissors > Paper
    if(player == 'r' and computer == 's') or (player == 'p' and computer == 'r') or (player == 's' and computer =='p'):
        return True
    
print(play())
    



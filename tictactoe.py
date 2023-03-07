# This a tictactoe game made in python

import random

class Tictactoe:
    
    #initialize the class instance
    def __init__(self):
        self.board = []
    
    #function to create the tictactoe board
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)
    
    #function to display the created board      
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print() 
            
    #function to determine the winner      
    def is_win(self, player):
        win = None
        n = len(self.board)
        #print(n)
        
        #Checking winning pattern per row
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win
        
        #checking winning pattern per column
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
            
        #checking winning pattern diagonally
        for i in range(n):
            win = True
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win
        
        #checking for the other diagonal pattern
        for i in range(n):
            win = True
            if self.board[i][n - 1 - i] != player:
                    win = False
                    break
        if win:
            return win
        
    #swap players turn 
    def swap_player(self, player):
        if player == 'O':
            return 'X'
        else:
            return 'O'
        
    #check if board is filled with values then declare TIE!  
    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True
    
     #Display players symbol in the board
    def fix_spot(self, row, col, player):
        self.board[row][col] = player
    
    #start the game
    def start(self):
        
        self.create_board()
        player = random.choice(['X', 'O'])
   
        
        while(True):
            print(f"It is now player {player} turn")
            move = input('Enter the move: (1-9): ')
            
            match move:
                case '1':
                    self.fix_spot(0, 0, player)
                
                case '2':
                    self.fix_spot(0, 1, player)
                    
                case '3':
                    self.fix_spot(0, 2, player)
                
                case '4':
                    self.fix_spot(1, 0, player)
                
                case '5':
                    self.fix_spot(1, 1, player)
                    
                case '6':
                    self.fix_spot(1, 2, player)
                
                case '7':
                    self.fix_spot(2, 0, player)
                
                case '8':
                    self.fix_spot(2, 1, player)
                    
                case '9':
                    self.fix_spot(2, 2, player)
                    
                case _:
                    print("Invalid Selection!, try again")
                    #break
            
            winner = self.is_win(player)
           
            if winner:
                print(f"Player {player} wins!")
                break
            
            board_flag = self.is_board_filled()
            if board_flag:
                print("It's a tie!")
                break
            player = self.swap_player(player)
            self.show_board()
        
            
#play the game
            
x = Tictactoe()
x.start()
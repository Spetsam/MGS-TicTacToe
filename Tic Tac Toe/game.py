from player import HumanPlayer, RandomComputerPlayer
from operator import truediv #Automatic
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #3x3
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: #Getting the rows
            print('| ' + ' | '.join(row)+ ' |')

    @staticmethod
    def print_board_nums():
        number_board = [str(i) for i in range(j*3, (j+1)*3) for j in range(3)] #If logical problem occurs, contact @Spetsam
        for row in number_board:
            print('| ' + ' | '.join(row)+ ' |')

    def available_moves(self): #Can be cut shorter
        moves = []
        for (i, spot) in enumerate(self.board): #Tuples for the appropriate values
            if spot == ' ':
                moves.append(i) #If it's an empty space we append the index
        return moves
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return len(self.available_moves())
    
    def make_move(self, square, letter):
        if self.board[square] == ' ': #If it's an empty move, nothing should be an empty move but just in case
            self.board[square] == letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False #If it doesn't pass

    def winner (self, square, letter): #The winner is if either one gets 3 in a row anywhere
        row_ind = square // 3 #Divided by 3 and rounded down
        row = self.board[row_ind*3 : (row_ind+1) * 3] #If logic doesn't work, contact @Spetsam
        if all([spot == letter for spot in row]):
            return True #Row win

        col_ind = square % 3 #We use modular division to get the index
        collumn = [self.board[col_ind+i*3] for i in range(3)] #If logic doesn't work, contact @Spetsam
        if all([spot == letter for spot in collumn]):
            return True #Collumn win
        
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #Left to Right diagonal \
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #Right to Left diagonal /
            if all([spot == letter for spot in diagonal2]):
                return True
        return False #If all checks fail



def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
    letter = 'X' #TicTacToe starts with X
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' made a move to square {square}')
                game.print_board()
                print('') #We need to also alternate letters/players

            if game.current_winner:
                if print_game:
                    print(letter+ " wins!")
                return letter

            letter = '0' if letter == 'X' else 'X' #Alternative way of writing it, shorter
    if print_game:
        print("It's a tie!") #It's instantaneous, we can fix it by adding breaks
    time.sleep(0.8)

#Playing the game

if __name__ == '__main__':
    x_Player = HumanPlayer('X') #X player
    o_Player = RandomComputerPlayer('O') #O player
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
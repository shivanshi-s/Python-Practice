#interactive program : visual representation -> user input -> function to update the board visual

# displaying information

class TicTacToe:
   def __init__(self):
      self.board = [' 'for _ in range(9)] #use a single list to rep 3X3 borad
      self.current_winner = None # keeps track of the winner

   def print_board(self):
      # this is just getting the rows
      for row in [self.board[i*3:(i+1)*3]for i in range(3)]:
         print('| '+ ' |'.join(row) + ' |')
   
   @staticmethod
   def print_board_nums():
   # 0,1,2 etc (tells us what number corresponds to what box)
      number_board = [[str(i) for i in range((j*3),(j+1)*3)] for j in range(3)]
      for row in number_board:
         print('| '+ ' |'.join(row) + ' |')

   def available_moves(self):
      return [i for i, spot in enumerate(self.board) if spot == ' ']
      # moves = []
      # for (i,spot) in enumerate(self.board):
      #    if spot == ' ':
      #       moves.append(i)
      # return moves
   def empty_squares(self):
      return ' ' in self.board
   
   def num_emplty_squares(self):
      return self.board.count(' ')


def play(game,x_player,o_player,print_game = True):
   if print_game:
      game.print_board_nums()

   letter = 'X'
   while game.empty_squares():
      if letter == '0':
         square = o_player.get_move(game)
      else:
         square = x_player.get_move(game)

# ===================
# incomplete
# ===================

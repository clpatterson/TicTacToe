
import datetime

# TODO: create game class
class TicTacToe:
	# Initializer
	def __init__(self, start, end, move_count, winner):
		self.board = list("\n_1_|_2_|_3_\n_4_|_5_|_6_\n 7 | 8 | 9 \n")
		self.start = start
		self.end = end
		self.move_count = move_count
		self.winner = winner

    # Update the board with the latest move
	def update_board(self,move,player):
		if self.move_count == 9:
			return 'The Game is over! There are no more moves to make.'
		if player == 'player_1':
			# Use list board and this algorithm to find place on board to change board[move*4-2]
			self.board[move*4-2] = 'X'
			self.move_count += 1
		else:
			self.board[move*4-2] = 'O'
			self.move_count += 1
		return None

	def show_board(self):
		return "".join(self.board)

	def get_positions(self):
		x_positions =[]
		o_positions =[]
		for position in range(len(self.board)):
			if self.board[position] == 'X':
				x_positions.append(position)
			elif self.board[position] == 'O':
				o_positions.append(position)
			else:
				pass
		return x_positions, o_positions

	def check_score(self):
		positions = self.get_positions()
		x_positions = positions[0]
		o_positions = positions[1]
		winning_position_combos = [[2, 18, 34], 
		                   [10, 18, 26],
		                   [2, 6, 10],
		                   [14, 18, 22],
		                   [26, 30, 34],
		                   [2, 14, 26],
		                   [6, 18, 30],
		                   [10, 22, 34]]
		for combo in winning_position_combos:
			x_position_count = 0
			o_position_count = 0
			for position in combo:
				try:
					x_positions.index(position)
					x_position_count += 1
				except:
					pass
				try:
					o_positions.index(position)
					o_position_count += 1
				except:
					pass
			if x_position_count == 3:
				self.winner = "player_1"
				return "Player 1 wins!"
			elif o_position_count == 3:
				self.winner = "player_2"
				return "Player 2 wins!"
		# Declare a draw after 9 moves and no win
		if self.move_count == 9:
			self.winner = 'draw'
			return "The game is a draw! Neither player triumphed!"


	def game_over(self):
		self.end = datetime.datetime.now()
		return None

# # Test Game
# game = TicTacToe(datetime.datetime.now(),None,0,None)
# print(game.show_board())
# print(game.update_board(1,'player_2'))
# print(game.show_board())
# print(game.update_board(3,'player_1'))
# print(game.show_board())
# print(game.update_board(5,'player_2'))
# print(game.show_board())
# print(game.update_board(7,'player_2'))
# print(game.show_board())
# print(game.update_board(6,'player_2'))
# print(game.show_board())
# print(game.check_score())
# print(game.update_board(4,'player_1'))
# print(game.show_board())
# print(game.update_board(2,'player_2'))
# print(game.show_board())
# print(game.update_board(8,'player_1'))
# print(game.show_board())
# print(game.update_board(9,'player_1'))
# print(game.show_board())
# print(game.check_score())
# game.game_over(None)
# print(game.start,game.end)

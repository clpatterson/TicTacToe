
import datetime

class TicTacToe:
	def __init__(self):
		self.board = list("\n_1_|_2_|_3_\n_4_|_5_|_6_\n 7 | 8 | 9 \n")
		self.start = datetime.datetime.now()
		self.end = None
		self.move_count = 0
		self.winner = None

    # Update the board with the latest move
	def update_board(self,move,marker):
		self.board[move*4-2] = marker
		self.move_count += 1
		return None

	def show_board(self):
		return "".join(self.board)

	def check_score(self):
		winning_position_combos = [[2, 18, 34], 
		                           [10, 18, 26],
		                           [2, 6, 10],
		                           [14, 18, 22],
		                           [26, 30, 34],
		                           [2, 14, 26],
		                           [6, 18, 30],
		                           [10, 22, 34]]
		for c in winning_position_combos:
			if all([self.board[idx] == 'X' for idx in c]):
				self.winner = "player_1"
				return self.winner
			elif all([self.board[idx] == 'O' for idx in c]):
				self.winner = "player_2"
				return self.winner
			else:
				continue
		if self.move_count == 9 and self.winner == None:
			self.winner = "draw"
			return self.winner
		else:
			return None

	def game_over(self):
		self.end = datetime.datetime.now()
		return None

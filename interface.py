import datetime
import tictactoe
import pyfiglet

# -- intro --
# Welcome players to tictactoe game
figlet = pyfiglet.Figlet(font='slant')
print(figlet.renderText("Terminal TicTacToe"))
print("\n Welcome to Terminal Tic-Tac-Toe, a game for the understimulated.\n ")
print("There are two players in Tic-Tac-Toe, player 1 who plays 'X' markers",
      "and player 2 who plays 'O' markers.")

willing_to_play = True
games = []

# TODO: Validate User Input
# def validate_player_move():
# 	# Validation rules
# 	# must enter a number, must be integer, must be an available move
# 	while True:
# 		try:
# 			player_move = int(input("Enter move:"))
# 		except ValueError:
# 			print("Please try again. Enter a whole number",
# 				"from 1 to 9.")
# 			continue
# 		else:


def game_turn(move,player):
	print("{}, please enter your move.".format(player),
				"(Enter the number for the space on the board",
				"you wish to occupy.")
	# TODO: Validate use input
	player_move = int(input("Enter move:"))

	game.update_board(player_move,player)
	if player == 'player_1':
		move += 1
		print(move)
		return move
	else:
		move -= 1
		print(move)
		return move

# Allow players to play multiple games, if they wish
while willing_to_play == True:
	# TODO: Use numpy to implement random coin flip
	print("Please enter 'flip' now to flip a coin and determine who goes first.")
	move = 1
	games.append(tictactoe.TicTacToe(datetime.datetime.now(),None,0,None))
	game = games[-1]
	# Allow players to make moves until the game is over
	while game.end == None:
		print(game.show_board())
		if move == 0:
			move = game_turn(move,'player_1')
		else:
			move = game_turn(move,'player_2')
		if game.check_score() is not None:
			print(game.check_score())
			game.game_over()
	# TODO: Validate input
	play_again = input("Would you like to play again? (yes/no):")
	if play_again.lower() == 'no':
		willing_to_play = False
	else:
		pass

# Exit out of the program
print(figlet.renderText("Thank You! Play Again!."))


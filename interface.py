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
	# TODO: Collect user input and validate
	player_move = int(input("Enter move:"))

	game.update_board(player_move,player)
	if player is 'player_1':
		move += 1
		print(move)
		return move
	else:
		move -= 1
		print(move)
		return move

# # Allow players to play multiple games, if they wish
# while willing_to_play == True:
# 	# Determine who will start by flipping
# 	# TODO: Use numpy to implement coin fair coin flip
# 	print("Please enter 'flip' now to flip a coin and determine who goes first.")
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
		print(game.end)

print(figlet.renderText("Thank You! Goodbye."))

# Ask players to choose who will be 1,2
# Explain how to make moves & rules

# -- game play --
# Flip a coin to determine who goes first (x or o)
# Take player moves sequentially
# Announce winner
# Ask if players wish to play again or quit?
# Repeat for new game


#Isaiah Lucas
#Rock, Paper, Scissors
#RPS6.py
# added comment for gh
import random
# Variables
pScore = 0
cScore = 0
ties = 0
cMoves = ["rock", "paper", "scissors"]

# Welcome Message
# PRint a welcome message :
print ("Welcome to Rock Paper Scissors")
# prompt for name
pName = input("What is your name?")


# Score Tracker
# make a function
def printScore():

	# Prints Score:
	print("Score: ")
# Shows player score
	print(pName +": " + str(pScore))
# Shows computer score
	print("Com Score: " + str(cScore))
# Shows how many ties
	print("Ties: " + str(ties))

#Game Loop
# loop until "q" is entered
while True:
	# prompt for player move (r, p, s, q)
	pMove = input("Enter 'r' for Rock, 'p' for Paper, 's' for Scissors or 'q' for quit")
# print the score
	printScore()
# check if "q" is entered if so end the game:
	if pMove == 'q':
		break
# get a computer move (random)
	cMove = random.choice(cMoves)
# compare player move with the computer move
	# player picks rock
	if pMove == "r":
		print(pName + " picked Rock")
		if cMove == "rock":
			print ("com picks Rock")
			print("Tie")
			ties += 1
		elif cMove == "paper":
			print("Com picks Paper")
			print("Paper covers Rock")
			cScore += 1
		else:
			print("Com picks Scissors")
			print("Rock breaks Scissors")
			pScore += 1
# player picks paper
	elif pMove == "p":
		print(pName + " picked Paper")
		if cMove == "rock":
			print ("com picks Rock")
			print("Paper covers rock")
			pScore += 1
		elif cMove == "paper":
			print("Com picks Paper")
			print("Tie")
			ties += 1
		else:
			print("Com picks Scissors")
			print("Scissors cuts paper")
			cScore += 1
		
# player picks scissors
	elif pMove == "s":
		print(pName + " picked Scissors")
		if cMove == "rock":
			print ("com picks Rock")
			print("Rock breaks Scissors")
			cScore += 1
		elif cMove == "paper":
			print("Com picks Paper")
			print("Scissors cuts Paper")
			pScore += 1
		else:
			print("Com picks Scissors")
			print("This is a tie")
			ties += 1
# check if "p" move is valid
	else:
		print("That is not an option")
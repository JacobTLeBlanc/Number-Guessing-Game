#Number guessing game between 1 - 100

#imports
import random

#Introduction
print("Your goal in this game is to guess the random number chosen between 1 - 100 in 10 guesses. If the number is 10 away then you are 'hot', 5 away then 'very hot'. Enjoy!")

user = input("Do you want to play (yes/no)? ")

while user == "yes" :

	#Random number
	randomNumber = random.randint(1, 100)
		
	for x in range(10) :

		userInput = int(input("Enter guess here: "))
		if userInput == randomNumber :
			print("WINNER!")
			break
		elif abs(userInput - randomNumber) <= 5 :
			print("Very hot!")
		elif abs(userInput - randomNumber) <= 10 :
			print("Hot!")
		else :
			print("Cold")

	print("Answer was", randomNumber)
	user = input("Do you want to play again (yes/no)? ")



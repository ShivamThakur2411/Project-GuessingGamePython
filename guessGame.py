import random

number = random.randrange(0,9)
guess = int(input("ENTER THE NUMBER YOU THINK OF - "))
attemptCount=1

while attemptCount!=5:
	if guess>number:
		attemptCount = attemptCount + 1
		print("The number you guessed was higher than the correct number")
		guess = int(input("ENTER THE NUMBER YOU THINK OF - "))
	elif guess<number:
		attemptCount = attemptCount + 1
		print("The number you guessed was lower than the correct number")
		guess = int(input("ENTER THE NUMBER YOU THINK OF - "))
	elif guess==number:
		attemptCount = attemptCount + 1
		print("CONGRATULATIONS, YOU WON!!")
		break
print("Sorry, you lost the game, the correct number was - ")
print(number)
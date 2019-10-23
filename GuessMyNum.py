# Guess myNumber
import random;
secreteNum = random.randint(1,25);

print('I am thinking of a number between 1 to 25');

global guess;
for guess_Count in range(1,7):
	print("Take a guess");
	guess = int(input())
	if guess < secreteNum:
		print("your guess is too low.")
	elif guess > secreteNum:
		print("your guess is too high.")
	else:
		break #u reach ur dest
	
if guess == secreteNum:
	print("Good job! you guessed my number in "+str(guess_Count)+ ' guesses!')
else:
	print('Nope. The number I was thinking of was '+ str(secreteNum))

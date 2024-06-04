import random
name=input("What is your name? ")
print("Good Luck ,",name)
choices = [
    "elephant", "soccer", "pineapple", "shakespeare", "guitar", "basketball",
    "leonardo", "carrot", "judo", "kangaroo", "hollywood", "cucumber", "tennis",
    "beethoven", "marathon", "tomato", "einstein", "cricket", "dolphin", "ballet",
    "potato", "picasso", "baseball", "giraffe", "swimming", "broccoli", "spielberg",
    "boxing", "zebra", "hockey"
]
word= random.choice(choices)
guesses =""
turn =10
while turn >0:
	failed=0
	for char in word:
		if char in guesses:
			print(char,end =" ")
		else:
			print("_",end =" ")
			failed += 1
	print()
	if failed == 0:
		print("You Won :) \n The word is ",word)
		break
	guess= input("Enter you guess:").lower()
	if len(guess) != 1:
		print("Enter a single letter")
		continue
	if guess in guesses:
		print("You already guessed this letter")
		continue

	guesses += guess
	if guess not in word:
		turn -=1
		print("Wrong Guess")
		print("You have",turn,"more guesses left!")
	

		if turn ==0:
			print("You loose :( \n The word is:",word)
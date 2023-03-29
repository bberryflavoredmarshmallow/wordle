import random

def processGuess(theCorrect, theGuess):
    position = 0
    clue = ""
    for letter in theGuess:
        if letter == theCorrect[position]:
            clue += "G"
        elif letter in theCorrect:
            clue += "Y"
        else:
            clue += "-"
        position += 1
    print(clue)
    return clue == "GGGGG" #correct, otherwise not correct

word_list = []
word_file = open(r"GET PATH OF FILE HERE")

for word in word_file:
    word_list.append(word.strip())

#choose a word
correct = random.choice(word_list)

num_of_guesses = 0
guessed_correctly = False

while num_of_guesses < 6 and not guessed_correctly:
    #get guess from users
    guess = input("Your 5-letter word: ")
    num_of_guesses += 1
    
    #process guess
    guessed_correctly = processGuess(correct, guess)

#display end of game message
if guessed_correctly:
    print("Congratulations! You got the correct word in", num_of_guesses, "tries.")
else:
    print("You have used up your guesses...")


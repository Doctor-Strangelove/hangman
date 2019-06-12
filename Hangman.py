#importing the time module
import time

#import random module
import random

#welcoming the user
name = input("What is your name? ")

print ("Hello, " + name, "please choose the game difficulty by entering the \
        number next to the option you prefer from those listed.")

#Difficulty options (NO impact on game currently)
difficulty = {1: 'Easy',2: 'Medium',3: 'Hard'}

#Present difficulty options
print(difficulty)

#Prompt user to select difficulty level
diff_input = input("Enter number of difficulty level ")

# Verify user input is int
try:
    diff_set = int(diff_input)
    print("You entered a valid level number: ", diff_set)
except ValueError:
    print("Please enter a number. E1") 
    # Check for failure to loop above.  Most likely fails.

diff_set = int(diff_input)

#Difficulty level chosen match those offered?
if diff_set in difficulty:
    print("You chose difficulty level " + diff_input)
else: 
    print("Please enter a valid difficulty level: E2")
    diff_input = input("Enter difficulty level (number) ") 
# Need to establish proper loop for screening out values >3.  
# Validation fails after 1st pass...cause it's not a real loop.

#wait for 1 second
time.sleep(1)

print ("Start guessing...")
time.sleep(0.5)

#here is a list of words to choose as our secret word
word_bank = ["barf","walnut","grand","leaf","missouri","crayon","bizarre"
            ,"chicken"]

#select random word from word_bank for use this round
word = random.choice(word_bank)
    
#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:

# make a counter that starts with zero
    failed = 0

# for every character in secret_word
    for char in word:

# see if the character is in the players guess
        if char in guesses:

# print then out the character
            print(char, )

        else:

# if not found, print a dash
            print("_", )

# and increase the failed counter with one
            failed += 1

# if failed is equal to zero

# print You Won
    if failed == 0:
        print ("\nYou won!")

# exit the script
        break

    print

# ask the user go guess a character
    guess = input("guess a character:")

# set the players guess to guesses
    guesses += guess

# if the guess is not found in the secret word
if guess not in word:

# turns counter decreases with 1 (now 9)
    turns -= 1

# print wrong
    print ("Wrong")

# how many turns are left
    print ("You have", + turns, 'more guesses' )

# if the turns are equal to zero
    if turns == 0:

# print "You Lose"
        print ("You Lose")
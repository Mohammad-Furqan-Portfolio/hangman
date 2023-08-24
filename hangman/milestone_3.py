while True:  # Step 1: Create a while loop with the condition set to True
    guess = input("Please guess a letter: ")  # Step 2: Ask the user to guess a letter

    if len(guess) == 1 and guess.isalpha():  # Step 3: Check if the guess is a single alphabetical character
        print("Good guess!")
        break  # Step 4: Break out of the loop if the guess is valid
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")  # Step 5: Print an error message if the guess is not valid


import random

word_list = ["Papaya", "Banana", "Cherry", "Mango", "Blueberry"] 
word = random.choice(word_list)

while True:
    guess = input("Please guess a letter: ")
    
    if len(guess) == 1 and guess.isalpha():
        if guess in word:  # Step 1: Check if the guess is in the word
            print(f"Good guess! {guess} is in the word.")  # Step 2: Print a success message
            break  # You may or may not want to break here, depending on whether you want the game to continue
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")  # Step 3: Print a message if the guess is not in the word
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

import random

# Function to check if the guess is in the word
def check_guess(guess, word):
    guess = guess.lower()  # Step 2: Convert the guess into lower case
    if guess in word:  # Step 3: Check if the guess is in the word
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False

# Function to ask for user input and validate it
def ask_for_input(word):
    while True:  # Infinite loop to keep asking for input until a valid guess is made
        guess = input("Please guess a letter: ")  # Step 2: Ask user for a guess
        if len(guess) == 1 and guess.isalpha():  # Step 3: Check if guess is valid
            if check_guess(guess, word):  # Step 4: Check if the guess is in the word
                break
        else: 
            print("Invalid letter. Please, enter a single alphabetical character.")

# Main code
word_list = ["Papaya", "Banana", "Cherry", "Mango", "Blueberry"]   # Replace this with your list of 5 favorite fruits
word = random.choice(word_list)  # Select a random word from the word list
ask_for_input(word)  # Step 5: Call the ask_for_input function to start the game


import random
# Create a list with favorite fruits for reference
word_list = ["Papaya", "Banana", "Cherry", "Mango", "Blueberry"]

# Create the random.choice method and pass the word_list variable into the choice method.
# Assign the randomly generated word to a variable called word.
word = random.choice(word_list)

# Step 5: Print out word to the standard output.
print(word)

# Using the input function, ask the user to enter a single letter.
# Assign the input to a variable called guess.
guess = input("Please enter a single letter: ")

# Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical
if len(guess) == 1 and guess.isalpha():
    # In the body of the if statement, print a message
    print("Good guess!")
else:
    # Create an else block
    print("Oops! That is not a valid input.")

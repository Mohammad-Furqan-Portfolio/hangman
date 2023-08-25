import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1  # Reduce 'num_lives' by 1
            print(f"Sorry, {guess} is not in the word.")  # Inform the user the guess was incorrect
            print(f"You have {self.num_lives} lives left.")  # Update the user on remaining lives

    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

if __name__ == "__main__":
    words = ["Papaya", "Banana", "Cherry", "Mango", "Blueberry"]
    hangman_game = Hangman(words)
    while hangman_game.num_lives > 0 and hangman_game.num_letters > 0:
        print("Word to guess:", hangman_game.word)
        print("Word guessed so far:", ' '.join(hangman_game.word_guessed))
        print("Number of unique letters:", hangman_game.num_letters)
        print("Number of lives:", hangman_game.num_lives)
        print("List of guesses:", hangman_game.list_of_guesses)
        hangman_game.ask_for_input()

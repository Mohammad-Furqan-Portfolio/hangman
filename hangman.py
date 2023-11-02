import random

class Hangman:
    """
    A class to represent the Hangman game.
    
    Attributes:
        word (str): The word to be guessed.
        word_guessed (list): A list representing the word to be guessed, with unguessed letters as underscores.
        num_letters (int): Number of unique letters in the word.
        num_lives (int): Number of lives the player has.
        word_list (list): List of possible words.
        list_of_guesses (list): List of letters already guessed.
    """
    def __init__(self, word_list, num_lives=5):
        """
        The constructor for Hangman class.
        
        Parameters:
            word_list (list): The list of words to choose from.
            num_lives (int): The number of lives the player starts with.
        """
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        Checks if the guessed letter is in the word and updates the game state.
        
        Parameters:
            guess (str): The letter guessed by the player.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """
        Continuously prompts the user for a letter until a valid guess is made.
        """
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

def play_game(word_list):
    """
    Function to play the Hangman game.
    
    Parameters:
        word_list (list): The list of words to choose from for the game.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

if __name__ == "__main__":
    words = ["Papaya", "Banana", "Cherry", "Mango", "Blueberry"]
    play_game(words)

# wordle


This is a simple game that prompts the user to guess a randomly selected word from a list of words based on the chosen difficulty level. The user has six chances to guess the word correctly. If the user guesses the word correctly within six tries, their time to guess the word will be recorded on the leaderboard. If the user fails to guess the word within six tries, the game will end and the user will be informed of the correct word.

# Requirements

Python 3.x

# Usage

Clone this repository to your local machine.
Open a terminal in the cloned directory.
Run python game.py to start the game.
Follow the prompts to play the game.
To view the leaderboard, select option 2 from the main menu.

# Game Logic

The game logic is implemented using a combination of conditional statements, loops, and functions. Here's an overview of the main components:

get_word(difficulty): A function that randomly selects a word from a list of words based on the chosen difficulty level.
check_guess(guess, word): A function that checks the user's guess against the selected word and returns the positions and letters that are correct.
play_game(): A function that prompts the user to enter a guess and checks the guess against the selected word. The user has six chances to guess the word correctly. If the user guesses the word correctly within six tries, their time to guess the word will be recorded on the leaderboard. If the user fails to guess the word within six tries, the game will end and the user will be informed of the correct word.
add_score(name, score): A function that appends the player's name and score to the leaderboard file.
show_leaderboard(): A function that reads the leaderboard file and displays the contents.

# License

This project is licensed under the MIT License.
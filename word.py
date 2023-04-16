import random
import time

def get_word(difficulty):
    if difficulty == "easy":
        words = ["apple", "baker", "candy", "drama", "eagle"]
    elif difficulty == "medium":
        words = ["juice", "image", "lemon", "melon", "music"]
    else:
        words = ["python", "shell", "heart", "swift", "unity"]

    return random.choice(words)

def check_guess(guess, word):
    correct_positions = []
    correct_letters = []

    for i in range(len(guess)):
        if guess[i] == word[i]:
            correct_positions.append(i)
        elif guess[i] in word:
            correct_letters.append(guess[i])

    return correct_positions, correct_letters

def play_game():
    difficulty = input("Choose a difficulty level: easy, medium, or hard? ")
    word = get_word(difficulty)

    guesses = 0
    start_time = time.time()
    while guesses < 6:
        guess = input("Enter your guess: ")
        guess = guess.lower()

        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        correct_positions, correct_letters = check_guess(guess, word)

        if len(correct_positions) == 5:
            end_time = time.time()
            total_time = round(end_time - start_time, 2)
            print("Congratulations! You guessed the word in {} seconds!".format(total_time))
            return total_time

        print("Your guess:")
        for i in range(len(guess)):
            if i in correct_positions:
                print("{} (correct position)".format(guess[i]))
            elif guess[i] in correct_letters:
                print("{} (correct letter)".format(guess[i]))
            else:
                print("{}".format(guess[i]))

        guesses += 1

    if guesses == 6:
        print("Sorry, you didn't guess the word in time. The word was {}".format(word))
        return None

def add_score(name, score):
    with open("leaderboard.txt", "a") as f:
        f.write("{} - {} seconds\n".format(name, score))

def show_leaderboard():
    with open("leaderboard.txt", "r") as f:
        leaderboard = f.readlines()

    if len(leaderboard) == 0:
        print("The leaderboard is empty.")
    else:
        print("Leaderboard:")
        for line in leaderboard:
            print(line.strip())

def main():
    while True:
        print("\nWelcome to the Word Guessing Game!\n")
        print("1. Play game")
        print("2. Show leaderboard")
        print("3. Quit\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            score = play_game()

            if score is not None:
                add_score(name, score)

        elif choice == "2":
            show_leaderboard()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

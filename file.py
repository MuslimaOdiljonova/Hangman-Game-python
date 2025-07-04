import random
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\  |
         |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    =========""",
    """
     -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    ========="""
]

with open("words.txt", "r") as file:
    content = file.read()
    target = random.choice(content.split())
    # print(target)

guessed_letters = []
wrong_guesses = 0
max_wrong = len(hangman_stages) - 1
print("🕹️ Welcome to Hangman!")
print("\nA B C D E F G H I")
print("J K L M N O P Q R")
print("S T U V W X Y Z")


while True:
    print(hangman_stages[wrong_guesses])

    display = ""
    for char in target:
        if char in guessed_letters:
            display += char + " "
        else:
            display += "_ "
    print("\nWord: " + display)

    user_input = input("\nChoose a letter: ").lower()

    if len(user_input) != 1 or not user_input.isalpha():
        print("Please enter a single letter.")
        continue

    if user_input in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(user_input)

    if user_input in target:
        print("Good guess!")
    else:
        print("Wrong guess!")
        wrong_guesses += 1

    if all(char in guessed_letters for char in target):
        print("\nCongratulations! You guessed the word:", target)
        break

    if wrong_guesses >= max_wrong:
        print(hangman_stages[wrong_guesses])
        print("\nGame over! The word was:", target)
        break


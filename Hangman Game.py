#HANGMAN GAME
import random

words = ["python", "uranus", "world", "success", "love"]
word = random.choice(words)
display = ["_"] * len(word)
tries = 11
guessed_letters = set()

print("Guess the word!")

while tries > 0 and "_" in display:
    print(" ".join(display))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("Correct!")
        for i, letter in enumerate(word):
            if letter == guess:
                display[i] = guess
    else:
        tries -= 1
        print(f"Wrong! You have {tries} tries left.")

if "_" not in display:
    print(f"Congratulations! The word was {word}.")
else:
    print(f"Sorry, the word was {word}.")

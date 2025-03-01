import random
from hangman_words import words

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']

lives = 6
chosen_word = random.choice(words)

guessed_letters = []
tam = len(chosen_word)
display = ["_"] * tam

game_over = False

while not game_over:

    print(stages[lives])
    print(" ".join(display))
    print(f"You have {lives} lives remaining")
    guess = input("Try guessing a letter: ")
    guess.lower()

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'")
        continue

    for i, letter in enumerate(chosen_word):
        if letter == guess:
            display[i] = guess
            guessed_letters.append(guess)

    if guess not in chosen_word:
        lives -= 1
        print(f"You've guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"You Lose!! The word is {chosen_word}")

    if "_" not in display:
        game_over = True
        print("Great Job! You Win")

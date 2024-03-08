import random

from jallod_words import word_list

word = random.choice(word_list)


# print(word)
def play():
    word_complete = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    life = 6
    name = input("What is your name? ")
    print("Hello " + name + "! Let's Play Hangman!")
    print(word_complete)
    print('\n')

    while not guessed and life > 0:
        guess = input("Please guess a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Oops! You've already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                life -= 1
                guessed_letters.append(guess)
            else:
                print("Good job!", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_complete)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_complete = "".join(word_as_list)
                if "_" not in word_complete:
                    guessed = True
        elif len(guess) == len(word):
            if guess in guessed_words:
                print("Oops! You've already guessed the word", guess)
            elif guess != word:
                print(guess, "is not in the word.")
                life = 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_complete = word
        else:
            print('Not a valid guess.')
        print(word_complete)
        print('\n')
    if guessed:
        print("Woah, You won! :)")
    else:
        print("you lose!")


print(play())

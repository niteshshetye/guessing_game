import random
from utils import update_clue


lives = 9
words = ['alone', 'smile', 'house', 'dream', 'death', 'india']
secrete_word = random.choice(words)
clue = list('_____')
heart_symbol = u'\u2764'
guessed_word_correctly = False

while lives > 0:
    print(clue)
    print(f"lives left: {heart_symbol * lives}")
    guess_word = input("Enter a letter or whole word: ")

    if '_' not in clue:
        print(f'You win! The word was: {secrete_word}')
        guessed_word_correctly = True
        break

    if guess_word == secrete_word:
        guessed_word_correctly = True
        break

    if guess_word in secrete_word:
        update_clue(guess_word, secrete_word, clue)
    else:
        print(f"Incorrect! You loose one life")
        lives -= 1

if guessed_word_correctly:
    print(f"You won the game secrete word is {secrete_word}")
else:
    print(f"You loose the game, secrete word is {secrete_word}")

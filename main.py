from rich import print as rprint
import random

with open('5-letter-words.txt', 'r') as f:
    content = f.read().splitlines()

def is_valid_word(word):
    if word in content:
        return True
    else:
        return False

def choose_word(word_bank):
    answer_word = random.choice(word_bank)
    return answer_word


def print_grid(grid):
    '''takes the list of guessed words and prints it beautiful using rich library'''
    for col in grid:
        rprint('['+ col[0][1] + ']' + col[0][0] + ' ' + 
               '['+ col[1][1] + ']' + col[1][0] + ' ' + 
               '['+ col[2][1] + ']' + col[2][0] + ' ' + 
               '['+ col[3][1] + ']' + col[3][0] + ' ' + 
               '['+ col[4][1] + ']' + col[4][0] + ' ')

def verify_word(guess_word, answer_word, current_column):
    cols = [''] * 5

    if guess_word == answer_word:
        cols = ['green'] * 5
    else:
        for i in range(len(guess_word)):
            if guess_word[i] == answer_word[i]:
                cols[i] = 'green'
            elif guess_word[i] in answer_word:
                cols[i] = 'yellow'
            else:
                cols[i] = 'black'
    
    i = 0
    for item in grid[current_column]:
        item[1] = cols[i]
        i += 1

answer_word = choose_word(content)

reset_grid = [
    [['_', 'white'], ['_', 'white'], ['_', 'white'], ['_', 'white'], ['_', 'white']],
    [['_', 'white'], ['_', 'white'], ['_', 'white'], ['_', 'white'], ['_', 'white']],
    [['_', 'white'], ['_', 'white'], ['_', 'white'], ['_', 'white'], ['_', 'white']],
    [['_', 'white'], ['_', 'white'], ['_', 'white'], ['_', 'white'], ['_', 'white']],
    [['_', 'white'], ['_', 'white'], ['_', 'white'], ['_', 'white'], ['_', 'white']]
]

grid = reset_grid.copy()

current_column = 0
loop = True

while loop:
    guess = ''
    guess = input('input guess: ')

    if guess == 'q':
        print('quitting...')
        loop = False
    elif len(guess) == 5 and is_valid_word(guess):
        verify_word(guess, answer_word, current_column)
        i = 0
        for item in grid[current_column]:
            item[0] = guess[i]
            i += 1
        current_column += 1
        guess = ''

        print_grid(grid)
        print(current_column, '/', len(grid))
    else:
        rprint('enter a [italic bold]valid word')
                
    if current_column > 4:
        print(current_column)
        print(f"You ran out of guesses. Thanks for playing!\nThe word was {answer_word}")
        replay = input('Play again? (Y/N): ')
        if replay.lower() == 'y' or 'yes':
            current_column = 0
            grid = reset_grid.copy()
            answer_word = choose_word(content)
        loop = False
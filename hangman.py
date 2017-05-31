# hangman.py

from random import randrange
from string import *

# -----------------------------------
# Import hangman words

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()

# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()


def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
# secret_word = 'claptrap'
secret_word = get_word()
letters_guessed = []


# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True


def print_guessed():
    """
    Prints out the characters you have guessed in the secret word so far
    """
    global secret_word
    global letters_guessed
    
    ####### YOUR CODE HERE ######
    character_list = []
    for i in secret_word:
        if i in letters_guessed:
            character_list.append(i)
        else:
            character_list.append('-')

    return join(character_list, '')


def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    # secret_word  = get_word()
    ####### YOUR CODE HERE ######
    while mistakes_made < MAX_GUESSES:
        print str(MAX_GUESSES-mistakes_made) + ' guesses left'
        print print_guessed()

        letter = lower(raw_input('Enter a letter: '))
        if letter not in letters_guessed:
            letters_guessed.append(letter)

            if letter in secret_word:
                if word_guessed():
                    print 'You\'ve got it right! The secret word is ' + secret_word + '.'
                    break
            else:
                mistakes_made += 1
                print_hangman_image(mistakes_made)

        else:
            print 'You\'ve have already guessed this letter. Try again.'

    print 'Sorry. The correct answer is ' + secret_word + '.'
    return None


def print_hangman_image(mistakes = 6):
    """
    Prints out a gallows image for hangman. The image printed depends on
    the number of mistakes (0-6).
    """

    if mistakes <= 0:
        print''' ____________________
    | .__________________|
    | | / /
    | |/ /
    | | /
    | |/
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    """"""""""""""""""""""""|
    |"|"""""""""""""""""""|"|
    | |                   | |
    : :                   : :
    . .                   . .'''

    elif mistakes == 1:
        print''' ___________.._______
    | .__________))______|
    | | / /      ||
    | |/ /       ||
    | | /        ||.-''.
    | |/         |/  _  \\
    | |          ||  `/,|
    | |          (\\\\`_.'
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    """"""""""""""""""""""""|
    |"|"""""""""""""""""""|"|
    | |                   | |
    : :                   : :
    . .                   . .'''
    elif mistakes == 2:
        print''' ___________.._______
    | .__________))______|
    | | / /      ||
    | |/ /       ||
    | | /        ||.-''.
    | |/         |/  _  \\
    | |          ||  `/,|
    | |          (\\\\`_.'
    | |          -`--'
    | |          |. .|
    | |          |   |
    | |          | . |
    | |          |   |
    | |          || ||
    | |
    | |
    | |
    | |
    """"""""""""""""""""""""|
    |"|"""""""""""""""""""|"|
    | |                   | |
    : :                   : :
    . .                   . .'''
    elif mistakes == 3:
        print''' ___________.._______
    | .__________))______|
    | | / /      ||
    | |/ /       ||
    | | /        ||.-''.
    | |/         |/  _  \\
    | |          ||  `/,|
    | |          (\\\\`_.'
    | |         .-`--'
    | |        /Y . .|
    | |       // |   |
    | |      //  | . |
    | |     ')   |   |
    | |          || ||
    | |
    | |
    | |
    | |
    """"""""""""""""""""""""|
    |"|"""""""""""""""""""|"|
    | |                   | |
    : :                   : :
    . .                   . .'''
    elif mistakes == 4:
        print''' ___________.._______
    | .__________))______|
    | | / /      ||
    | |/ /       ||
    | | /        ||.-''.
    | |/         |/  _  \\
    | |          ||  `/,|
    | |          (\\\\`_.'
    | |         .-`--'.
    | |        /Y . . Y\\
    | |       // |   | \\\\
    | |      //  | . |  \\\\
    | |     ')   |   |   (`
    | |          || ||
    | |
    | |
    | |
    | |
    """"""""""""""""""""""""|
    |"|"""""""""""""""""""|"|
    | |                   | |
    : :                   : :
    . .                   . .'''
    elif mistakes == 5:
        print''' ___________.._______
    | .__________))______|
    | | / /      ||
    | |/ /       ||
    | | /        ||.-''.
    | |/         |/  _  \\
    | |          ||  `/,|
    | |          (\\\\`_.'
    | |         .-`--'.
    | |        /Y . . Y\\
    | |       // |   | \\\\
    | |      //  | . |  \\\\
    | |     ')   |   |   (`
    | |          ||'||
    | |          ||
    | |          ||
    | |          ||
    | |         / |
    """"""""""""""""""""""""|
    |"|"""""""""""""""""""|"|
    | |                   | |
    : :                   : :
    . .                   . .'''
    else: #mistakes >= 6
        print''' ___________.._______
    | .__________))______|
    | | / /      ||
    | |/ /       ||
    | | /        ||.-''.
    | |/         |/  _  \\
    | |          ||  `/,|
    | |          (\\\\`_.'
    | |         .-`--'.
    | |        /Y . . Y\\
    | |       // |   | \\\\
    | |      //  | . |  \\\\
    | |     ')   |   |   (`
    | |          ||'||
    | |          || ||
    | |          || ||
    | |          || ||
    | |         / | | \\
    """"""""""|_`-' `-' |"""|
    |"|"""""""\ \       '"|"|
    | |        \ \        | |
    : :         \ \       : :
    . .          `'       . .'''

      
main = raw_input('')

if main == 'play_hangman()':
    play_hangman()
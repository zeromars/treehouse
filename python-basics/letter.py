#import random
import random
import os

# create a list of words
letters = ['koda','erin','landon','kathy','megan']

# be able to get a random word from the list
def get_word():
    word = random.choice(letters)
    return word

def print_letters(letters):
    for letter in letters:
        print(letter)

def guess_word(answer):
    word = str(input("Guess the word"))
    if word == answer:
        print("You Win!")
        return True
    else:
        print("Try Again")
        return False

def clear():
    if os.name == 'nt':
        #windows
        os.system('cls')
    else:
        #mac
        os.system('clear')

def again():
    play = input("Play again? (yes|no)")
    if play == 'yes':
        game()
    else:
        print('Thank you for playing')

# user to be able to guess letters in the word
def game():
    count = 1
    print("Welcome to the letter game!")
    print("Wrong guesses subtract a guess , and right ones add a guess")
    print("""Available commands are:
        HELP: show this message
        SHOW: show letters in your list
        GUESS: quit this app""")
    print(letters)
    word = get_word()
    # print(word)
    correct = []
    while count <= 9:
        try:
            letter = str(input("Guess a letter"))
        except ValueError:
            print("That is not a letter!")
            count += 1
        else:
            if letter == "GUESS":
                if guess_word(word):
                    break
                else:
                    continue
            elif letter == "SHOW":
                print_letters(correct)
            elif letter == "HELP":
                print("""Available commands are:
                    HELP: show this message
                    SHOW: show letters in your list
                    GUESS: quit this app""")
            else:
                if letter in word:
                    print("Correct {} was found in the word.".format(letter))
                    if letter not in correct:
                        if letter != "":
                            correct.append(letter)
                    print("Here is the correct letters so far!")
                    print_letters(correct)
                    if count > 0:
                        count -= 1
                else:
                    print("Letter not found in the word: {}".format(letter))
                    count += 1
        print("Currently {} out of 9 guesses used.".format(count))
    else:
        again()
    again()
game()
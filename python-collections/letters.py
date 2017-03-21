# 2 player version of letter game
# each player picks a word then trys to guess the other persons word.

#import random
import random
import os

# show welcome screen
# ask 1 players or 2 players
# 2 players
# set 2 dictionaries (1 for each player) containing player name , score, current word
# allow each player to pick their word
# words must be 5 chars or longer
# start with player one and draw _ for each letter of player 2's word
# player 1 guess 's a letter
# If it's found then fill it in if not tell them nope 
# repeat for player 2
# Each letter guessed correctly is one point , each letter guessed incorrectly is -1 points
# Guessing the word correctly is 5 points

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

def welcome():
    print("Welcome to the letter game!")
    print("Wrong guesses subtract a guess , and right ones add a guess")

def get_help():
    print("""Available commands are:
        HELP: show this message
        SHOW: show letters in your list
        GUESS: quit this app""")

def get_players():
    players = input('How many players? Enter 1 or 2 and press the ENTER key')
    print(players)
    return players

def play(word, player, player_score):
    correct = []
    try:
        letter = str(input("Guess a letter"))
    except ValueError:
        print("That is not a letter!")
        count += 1
    else:
        if letter == "GUESS":
            if guess_word(word):
                if player == 'player_1':
                    player_score += 1
                elif player == 'player_2':
                    player_score += 1
        elif letter == "SHOW":
            print_letters(correct)
        elif letter == "HELP":
            get_help()
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
# user to be able to guess letters in the word
def game():
    welcome()
    get_help()
    players = get_players()
    print(players)
    if int(players) == 2:
        games = 3
        correct = []
        player_1 = {}
        player_2 = {}
        player_1_name = input("Enter player 1 name")
        print("Have opponent look away for next one")
        player_1_word = input("Enter your word player 1")
        player_1_score = 0
        player_2_name = input("Enter player 2 name")
        print("Have opponent look away for next one")
        player_2_word = input("Enter your word player 2")
        player_2_score = 0

        while games > 0:            
            count = 1
            print("Player 2 here is player 1's word'")
            for letter in player_1_word:
                print(" _ ", end='')
            print("\n\n")
            word = player_1_word
            while count <= 9:
                correct = []
                try:
                    letter = str(input("Guess a letter"))
                except ValueError:
                    print("That is not a letter!")
                    count += 1
                else:
                    if letter == "GUESS":
                        if guess_word(word):
                            player_2_score += 1
                            break
                        else:
                            continue
                    elif letter == "SHOW":
                        print_letters(correct)
                    elif letter == "HELP":
                        get_help()
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
                player_1_score += 1
            print("Player 1 here is player 2's word'")
            for letter in player_2_word:
                print(" _ ", end='')
            print("\n\n")
            word = player_2_word
            while count <= 9:
                try:
                    letter = str(input("Guess a letter"))
                except ValueError:
                    print("That is not a letter!")
                    count += 1
                else:
                    if letter == "GUESS":
                        if guess_word(word):
                            player_1_score += 1
                            break
                        else:
                            continue
                    elif letter == "SHOW":
                        print_letters(correct)
                    elif letter == "HELP":
                        get_help()
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
                player_2_score += 1
            games -= 1
            count = 0
        if player_1_score > player_2_score:
            print("player 1 you win!")
        else:
            print("player 2 you win!")
        again()
    else:
        count = 1
        word = get_word()
        correct = []
        print(letters)
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
                    get_help()
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
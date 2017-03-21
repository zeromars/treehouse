import random
def take_guess():
    guess = input("What is your guess?")
    return guess
def main():
    total = 1
    allowed = 5
    # generate a random number 1 to 10
    number = random.randint(1,10)
    # get a number guess from the player
    # compare guess to secret number
    while total <= allowed:
        try:
            my_guess = int(take_guess())
        except ValueError:
            print("That is not a number")
        else:
            if my_guess > number:
                print("To high")
            elif my_guess < number:
                print("To low")
            elif my_guess == number:
                print("You WIN!")
                break
            else:
                continue
        print("Total guesses so far are {} out of {}".format(total, allowed))
        total += 1
    # print hit or miss
    else:
        print("Game Over!")
    play = input("Play again? (yes|no)")
    if play == 'yes':
        main()
    else:
        print('Thank you for playing')
main()

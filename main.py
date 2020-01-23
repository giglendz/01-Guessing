import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


quit = False
range = 15

while not quit:
    random_number = random.randint(1,range)
    count = 1
    number = -1
    while number != random_number:
        number = input("Go ahead and guess a number between 1 and {}: ".format(range))
        if not number.isdigit():
            print("Hey! Guess a number!")
        else:
            number = int(number)
            count = count + 1
            print("Sorry, that's not correct.  That's okay, try again!")
            if number > random_number:
                print("That's too high!")
            elif number < random_number:
                print("That's too low!")
    print("Great job! You got it right!")
    print("You got it in {} tries! Good job!".format(count))
    play_again = input("\nWant to try again (yes or no)? ")
    play_again = play_again.lower()
    if play_again == "yes" or play_again == "y":
        quit = False
    else:
        quit = True

print("\n\nThanks for playing!  Catch you on the flip side!")
import random
import sys


def main():
    n = 0
    while n < 1:
        try:
            n = int(input("Level: "))
        except:
            n <= 0
            pass
        else:
            continue

    number = random.randrange(1, n, 1)
    guess = 0

    while True:
        try:
            guess = int(input("Guess: "))
        except:
            guess <= 0
            pass
        else:
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit()

main()

import random


def main():
    score = 0
    n = get_level()
    for _ in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        try:
            if attempt(x, y):
                score += 1
        except ValueError or TypeError:
            print("EEE")
        else:
            continue

    print(f"Score: {score}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass
        else:
            continue

def attempt(x, y):
    turn = 0
    score = False
    while turn <= 3 and score == False:
        try:
            guess = 0
            guess = int(input(f"{x} + {y} = "))
            if guess == (x + y):
                score = True
                return score
            else:
                print("EEE")
                turn += 1
        except ValueError:
            print("EEE")
            turn += 1
    else:
        if turn == 4:
            print(f"{x} + {y} =", (x + y))


def generate_integer(level):

    if level == 1:
        n = random.randint(0, 9)
    elif level == 2:
        n = random.randint(10, 99)
    else:
        n = random.randint(100, 999)
    return n


if __name__ == "__main__":
    main()

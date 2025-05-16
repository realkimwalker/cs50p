def main():

    percent = get_int()
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")


def get_int():

    while True:
        try:
            value = input("Fraction: ").split("/")
            x = int(value[0])
            y = int(value[1])
            percent = int(round(x/y * 100))
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
        else:
            return percent


main()

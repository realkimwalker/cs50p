
def main():
    greeting = input("Please enter a greeting: ").strip().lower()
    payment = value(greeting)
    print(payment)


def value(greeting):
    if greeting.startswith("hello"):
        due = "$0"
    elif greeting.startswith("h"):
        due = "$20"
    else:
        due = "$100"
    return due


if __name__=="__main__":
    main()

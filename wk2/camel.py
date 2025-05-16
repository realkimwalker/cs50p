def main():
    camelcase = input("enter a name in camelcase: ")
    for c in camelcase:
        if c.islower():
            print(c, end="")
        elif c.isupper():
            print("_" + c.lower(), end="")
    print()

main()

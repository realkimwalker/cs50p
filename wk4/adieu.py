import inflect
p = inflect.engine()

def main():
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            print()
            break
        else:
            continue

    print("Adieu, adieu, to " + p.join(names))


main()

def main():
    vowel = ["a","e","i","o","u","A","E","I","O","U"]
    s = input("Input: ")
    print("Output: ")
    for c in s:
        if c in vowel:
            print("", end="")
        else:
            print(c, end="")
    print()


main()

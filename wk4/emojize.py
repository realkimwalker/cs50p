import emoji

def main():
    emojized = input()
    print(emoji.emojize(f"{emojized}", language='alias'))


main()

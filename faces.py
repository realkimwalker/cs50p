def convert(message):
    message = message.replace(":)", "🙂")
    message = message.replace(":(", "🙁")
    return message


def main():
    faces = input("Enter some text with a smiley or frown: ")
    emoji = convert(faces)
    print(emoji)


main()

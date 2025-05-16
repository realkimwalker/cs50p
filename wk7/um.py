import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    words = []
    words = s.split(" ")
    for word in words:
        if matches := re.findall(r"^(\bum[\.\?,!]*\s*)*$", word, re.IGNORECASE):
            count += 1
    return(count)


if __name__ == "__main__":
    main()

import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    if matches := re.match(r'^<iframe(?:\w*)?\s.*(http://|https://)(www\.)?(youtu)be\.com/embed(/.{11})"\s?(.*\w*)?></iframe>$', s, re.DOTALL):
        hyperlink = matches.group(1)
        if "s" not in hyperlink:
            hyperlink = "https://"
        address = matches.group(3)
        address = address + ".be"
        embed = matches.group(4)
        return(f"{hyperlink}{address}{embed}")


if __name__ == "__main__":
    main()

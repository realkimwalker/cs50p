import re
import sys

def main():
    print(validate(input("IPv4 Adress: ").strip()))


def validate(ip):
    if matches := re.search(r"^(([0-9]?[0-9]|[0-1]?[0-9]?[0-9]|24[0-9]|[0-2]?[0-5]?[0-5])\.){3}([0-9]?[0-9]|[0-1]?[0-9]?[0-9]|24[0-9]|[0-2]?[0-5]?[0-5])$", ip):
        return True
    else:
        return False


if __name__=="__main__":
    main()

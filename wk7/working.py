import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    if matches := re.search(r"^([1][0-2]|[1-9]):?([0-5][0-9]):?\s(AM|PM) to ((?:[1][0-2])|[1-9]):?([0-5][0-9]):?\s(AM|PM)$", s):
        start_hour = matches.group(1)
        start_ap = matches.group(3)
        end_hour = matches.group(4)
        end_ap = matches.group(6)
        if matches.group(2) == None:
            start_min = "00"
        else:
             start_min = matches.group(2)
        if start_ap == "PM":
            start_hour = int(start_hour) + 12
        if start_ap == "AM" and start_hour == "12":
             start_hour = "00"
        if matches.group(5) == None:
             end_min = "00"
        else:
             end_min = matches.group(5)
        if end_ap == "PM" and int(end_hour) < 12:
            end_hour = int(end_hour) + 12
        return(f"{int(start_hour):02}:{start_min} to {int(end_hour):02}:{end_min}")
    else:
        raise ValueError


if __name__ == "__main__":
    main()


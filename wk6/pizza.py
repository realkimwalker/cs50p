from tabulate import tabulate
import sys
import csv

def main():
    menu = []
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line argument")
    elif sys.argv[1].endswith(".txt"):
        sys.exit("Not a python file")
    elif sys.argv[1].find(".py") == False:
        sys.exit("Not a python file")
    else:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                menu.append(row)
        name, small, large = (menu[0])

    print(tabulate(menu[1:], headers=(name,small,large), tablefmt="grid"))


if __name__=="__main__":
    main()

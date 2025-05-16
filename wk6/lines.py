import sys

def main():
    count = 0
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".txt"):
        sys.exit("Not a python file")
    elif sys.argv[1].find(".py") == False:
        sys.exit("Not a python file")
    else:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.lstrip(" ").startswith("#"):
                    continue
                elif line.isspace():
                    continue
                else:
                    count += 1
        print(count)


if __name__=="__main__":
    main()

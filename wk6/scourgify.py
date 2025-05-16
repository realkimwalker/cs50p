import sys
import csv

def main():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line argument")
        else:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                with open(sys.argv[2], "w") as file:
                    header = ["first", "last", "house"]
                    writer = csv.DictWriter(file, fieldnames=header)
                    writer.writeheader()
                    for row in reader:
                        last, first = row["name"].split(", ", 1)
                        house = row["house"]
                        writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__=="__main__":
    main()

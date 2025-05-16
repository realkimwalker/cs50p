import sys

def main():


    while True:
        try:
            outdated = input("Date: ")
            if "/" in outdated:
                date = outdated.split("/")
                month, day, year = date
            else:
                date = outdated.split()
                month, day_comma, year = date
                if "," in day_comma:
                    day = int(day_comma.replace(",", ""))
                else:
                    pass
                months = [
                 "January",
                 "February",
                 "March",
                 "April",
                 "May",
                 "June",
                 "July",
                 "August",
                 "September",
                 "October",
                 "November",
                 "December"
                ]
                if month in months:
                    month = months.index(month) + 1

            if 1 <= int(month) <= 12:
                if 1 <= int(day) <= 31:
                    break

        except:
            NameError
            ValueError
            EOFError
            pass

        else:
            continue
    month = int(month)
    day = int(day)
    year = int(year)
    print(f"{year}-{month:02}-{day:02}")


main()

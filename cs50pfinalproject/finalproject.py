from datetime import date, timedelta
import sys
import operator

def main():
    year, month, day = get_todays_date()
    gyear, gmonth, gday = get_goal_date(input("Goal Date: ").split("-"))
    current_date = date(year, month, day)
    goal_date = date(gyear, gmonth, gday)
    num_days = str(operator.__sub__(goal_date, current_date))
    total_days = num_days.split(" ", 2)
    total_pounds = calculate_weight_loss(int(total_days[0]))
    print(f"{total_pounds} pounds")


def calculate_weight_loss(days):
    daily_calorie_reduction = 400
    total_calories = days * daily_calorie_reduction
    calories_per_pound = 3500
    pounds = total_calories / calories_per_pound
    return(round(pounds, 2))


def get_goal_date(prompt):
        try:
            year, month, day = prompt
            return(int(year), int(month), int(day))
        except ValueError:
            SystemExit("Invalid date format")


def get_todays_date():
    todays_date = date.today()
    year, month, day = str(todays_date).split("-")
    return(int(year), int(month), int(day))


if __name__ == "__main__":
    main()

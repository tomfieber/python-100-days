#!/usr/bin/env python3

def is_leap_year(year):
    year_as_int = int(year)
    if year_as_int % 4 == 0:
        if year_as_int % 100 == 0:
            if year_as_int % 400 == 0:
                return True
            else:
                return False
        else:
            return False

def run_helper():
    year = input("Enter a year: ")
    if is_leap_year(year):
        print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    run_helper()
#!/usr/bin/env python3
# Created by: Alex OBrien
# Created on: October 30, 2026
# This program tells the user if the inputed year is a leap
# year or not.


def main():
    # Ask the user to enter year
    user_year = input("Enter a year to check if it's a leap year: ")

    try:
        # Convert the user's input into an integer6
        year = int(user_year)
    # Display an error message if cannot be turned into int
    except ValueError:
        print(f"'{user_year}' is not a valid input!")
        return

    # Check if year is a leap year
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a leap year!")
    else:
        print(f"{year} is not a leap year!")


if __name__ == "__main__":
    main()

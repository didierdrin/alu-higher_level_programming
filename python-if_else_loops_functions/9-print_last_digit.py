#!/usr/bin/python3
def print_last_digit(number):
    # Ensure the number is positive
    number = abs(number)
    # Get the last digit
    last_digit = number % 10
    # Print the last digit
    return last_digit

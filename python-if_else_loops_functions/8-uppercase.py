#!/usr/bin/python3
def uppercase(str):
  for char in str:
    # Convert character to uppercase using ASCII difference
    new_char = chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char
    print("{0}".format(new_char), end="")  # Print without newline initially
  print()

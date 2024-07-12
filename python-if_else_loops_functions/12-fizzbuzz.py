#!/usr/bin/python3
def fizzbuzz():
  for i in range(1, 101):
    # Check for multiples of 3 and 5 first (combined condition)
    if i % 15 == 0:
      print("FizzBuzz", end=" ")
    # Check for multiples of 3
    elif i % 3 == 0:
      print("Fizz", end=" ")
    # Check for multiples of 5
    elif i % 5 == 0:
      print("Buzz", end=" ")
    # Otherwise, print the number itself
    else:
      print(i, end=" ")

def uppercase(str):

  for char in str:
    # Convert character to uppercase using ASCII difference
    new_char = chr(ord(char) - 32 if ord(char) < 91 else ord(char))
    print(new_char, end="")  # Print without newline initially

  print()

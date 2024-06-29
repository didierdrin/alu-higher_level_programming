#!/usr/bin/python3 
with open("thezenofpython.txt", "r") as file:
    file_lines = file.readlines() 
    for line in file_lines:
        print(line.strip())

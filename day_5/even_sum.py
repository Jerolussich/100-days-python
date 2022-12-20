#!/usr/bin/python3
count = 0


for number in range(1, 101):
    if number % 2:
        count += number
print(count)
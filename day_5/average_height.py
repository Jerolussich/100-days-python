#!/usr/bin/python3

total = 0
len = 0

student_heights = [180, 124, 165, 173, 189, 169, 146]

for height in student_heights:
    total += height
    len += 1
print(round(total/len))

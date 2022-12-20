#!/usr/bin/python3

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
highest_score = 0
student_scores.sort()
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")
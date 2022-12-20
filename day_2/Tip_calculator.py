#!/usr/bin/python3


print("welcome to the tip calclulator")
total = float(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
tip = int(input("what porcentage would you like to tip? 10, 12 or 15? "))
amount_person = round((total * (1 + tip))/ people, 0)
print(f"Each person should pay:{amount_person}")

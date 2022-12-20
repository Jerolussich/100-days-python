#!/usr/bin/python3
import random
import string

print("Welcome to the PyPassword Generator\n")
letters = int(input("how many letters do you want in your password?\n"))
symbols = int(input("How many symbols do you like?\n"))
numbers = int(input("How many numbers would you like?\n"))
password = ""
numbers_random = ""
letters_random = ""
symbols_random = ""

for i in range(numbers):
    numbers_random += str(random.choice(string.digits))
for i in range(letters):
    letters_random += (random.choice(string.ascii_letters))    
for i in range(symbols):
    symbols_random += (random.choice(string.punctuation))

password = random.sample(letters_random + numbers_random + symbols_random, k=(letters + symbols + numbers))
print(''.join(password))



#!/usr/bin/python3
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

map = [row1, row2, row3]

print(*map, sep = "\n")

position = input("In what coordiantes do you want to bury the treasure?\n")

column = (int(position[0])) - 1
row = (int(position[1])) - 1
map [column][row] = 'x'

print(*map, sep = "\n")


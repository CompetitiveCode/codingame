#Answer to Ghost Legs - https://www.codingame.com/ide/puzzle/ghost-legs

import sys
import math

w, h = [int(i) for i in input().split()] #To get the width and height which is separated by a space
letters = [x for x in input().split('  ')] #To get the letters present in the game
line = []
for i in range(h-2): #h-2 as we are taking the letters and the numbers differently for mapping purpose
    line.append(' '+input()+' ') #A space is added in addition to the line for easier comparison purpose
numbers = [x for x in input().split('  ')] #Numbers are taken. Numbers here are not necessary to start from 0 or 1

for i in range(len(letters)): #We need to find for all the letters
    res = i #Initially, we are following the line of the letter and later it is changed based on connections
    for j in line: #Now each line is observed for connection
        if j[res*3+2] == '-': #For this purpose, an extra space is added at the end. Check's whether a connection to the right is present.
            res += 1
        elif j[res*3-1] == '-': #For this purpose, an extra space is added at the start. Check's whether a connection to the left is present.
            res -= 1
    letters[i] += numbers[res] #Using the number array, we map the number with the letter

for i in letters:
    print(i)
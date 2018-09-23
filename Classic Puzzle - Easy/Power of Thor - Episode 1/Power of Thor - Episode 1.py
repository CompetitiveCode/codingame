#Answer to Power of Thor - Episode 1 in C

import sys
import math

lightX, lightY, initialTX, initialTY = [int(i) for i in input().split()]

while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    if(initialTX>lightX and initialTY==lightY):
        print("W")
        initialTX-=1
    elif (initialTX<lightX and initialTY==lightY):
        print("E")
        initialTX+=1
    elif (initialTX==lightX and initialTY>lightY):
        print("N")
        initialTY-=1
    elif (initialTX==lightX and initialTY<lightY):
        print("S")
        initialTY+=1
    elif (initialTX<lightX and initialTY<lightY):
        print("SE")
        initialTX+=1
        initialTY+=1
    elif (initialTX<lightX and initialTY>lightY):
        print("NE")
        initialTX+=1
        initialTY-=1
    elif (initialTX>lightX and initialTY<lightY):
        print("SW")
        initialTX-=1
        initialTY+=1
    elif (initialTX>lightX and initialTY>lightY):
        print("NW")
        initialTX-=1
        initialTY-=1
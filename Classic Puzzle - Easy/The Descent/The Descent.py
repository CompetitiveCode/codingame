#Answer to The Descent in Python

import sys
import math

while True:
    j = 0
    l = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if mountain_h > j:
            j=mountain_h
            l=i
    print(l)
    j=0
    l=0

#Answer to Horse-racing Duals in Python

import sys
import math

n = int(input())
p = []
for i in range(n):
    pi = int(input())
    p.append(pi)
p.sort()
q = 10000000
for i in range(n - 1):
    dif = int(abs(p[i] - p[i + 1]))

    if dif < q:
        q = dif
print(q)
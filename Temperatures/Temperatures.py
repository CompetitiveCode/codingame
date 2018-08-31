#Answer to Temperatures in C

import sys
import math

n = int(input())  # the number of temperatures to analyse
k,m=10000,10000
l=0
for i in input().split():
    t = int(i)
    l=t
    if(t<0):
        l*=-1
    if(m>=l):
        m=l
        if(t==(k*-1) and t<0):
            k=k
        else:
            k=t
if(k==10000):
    k=0
print(k)
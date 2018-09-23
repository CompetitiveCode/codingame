#Answer to Defibrillators in Python

from math import *
lona=float(input().replace(',', '.'))
lata=float(input().replace(',', '.'))
n = int(input())
d=3.402823e+38
result=""
for i in range(n):
    defib = input().split(";")
    lonb=float(defib[4].replace(',', '.'))
    latb=float(defib[5].replace(',', '.'))
    x=((lonb-lona)*cos((lata + latb)/2))
    y=(latb - lata)
    e=sqrt(x**2 + y**2) * 6371
    if(e<d):
        result=defib[1]
        d=e
print(result)
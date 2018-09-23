#Answer to MIME Type in Python

import sys
import math

n = int(input())
q = int(input())
ext={}
for i in range(n):
    a,b=input().split()
    ext[a.lower()]=b
for i in range(q):
    k=input().lower()
    f = k.split('.')
    if len(f)>1:
        try:
            print(ext[f[-1].lower()])
        except KeyError:
            print("UNKNOWN")
        except IndexError:
            print("UNKNOWN")
    else:
        print("UNKNOWN")
#Answer to Chuck Norris in Python

import sys
import math

message = input()
binmsg = ''.join(format(ord(x), 'b').zfill(7) for x in message)
i=0
while i < len(binmsg):
    if(binmsg[i]=='0'):
        print("00 ",end="")
        while(binmsg[i]=='0'):
            print(binmsg[i],end="")
            i+=1
            if(i==len(binmsg)):
                quit()
    elif(binmsg[i]=='1'):
        print("0 ",end="")
        while(binmsg[i]=='1'):
            print("0",end="")
            i+=1
            if(i==len(binmsg)):
                quit()
    print(" ",end="")
#Answer to The River I. in Python

a=int(input())
b=int(input())
while(a!=b):
    if(a<b):
        if(a<10):a+=a
        else:
            j=0
            for i in str(a):
                j+=int(i)
            a+=j
    else:
        if(b<10):b+=b
        else:
            j=0
            for i in str(b):
                j+=int(i)
            b+=j
print(a)
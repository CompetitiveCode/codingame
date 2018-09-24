#Answer to Brackets, extreme edition in Python

a=[]
b,k=0,0
for i in input():
    if(i=="{" or i=="[" or i=="("):
        a.append(i)
        k+=1
    elif(i=="}" or i=="]" or i==")"):
        if(k==0):b+=1
        else:
            if(i=="}"):
                if(a.pop()!="{"):
                    b+=1
                    k-=1
            elif(i=="]"):
                if(a.pop()!="["):
                    b+=1
                    k-=1
            elif(i==")"):
                if(a.pop()!="("):
                    b+=1
                    k-=1
if(len(a)>0):
    b+=1
print("false" if b>0 else "true")
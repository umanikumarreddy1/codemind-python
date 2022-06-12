a=int(input())
b=int(input())
ma=c=0
for i in range(a,b+1):
    su=0
    for j in range(i,b+1):
        su+=j
        if su%2!=0:
            c+=1
print(c)
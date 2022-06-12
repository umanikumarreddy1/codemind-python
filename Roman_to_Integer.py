a=input()
c=0
for i in range(len(a)):
    if a[i]=='I':
        c+=1
    elif a[i]=='V':
        if a[i-1]=='I' and i>0:
            c+=3
        else:
            c+=5
    elif a[i]=='X':
        if a[i-1]=='I' and i>0:
            c+=8
        else:
            c+=10
    elif a[i]=='L':
        if a[i-1]=='X' and i>0:
            c+=30
        else:
            c+=50
    elif a[i]=='C':
        if a[i-1]=='X' and i>0:
            c+=80
        else:
            c+=100
    elif a[i]=='D':
        if a[i-1]=='C' and i>0:
            c+=300
        else:
            c+=500
    elif a[i]=='M':
        if a[i-1]=='C' and i>0:
            c+=800
        else:
            c+=1000
print(c)
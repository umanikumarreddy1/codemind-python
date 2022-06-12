def add(a):
    su=0
    temp=a
    while True:
        su=0
        while temp>0:
            r=temp%10
            su+=r
            temp//=10
        if su<10:
            return su
        else:
            temp=su
            su=0
            continue
a=int(input())
res=add(a)
print(res)
        
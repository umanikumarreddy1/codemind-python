def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0
a=int(input())
b=int(input())
for i in range(1,1000):
    if prime(i+a+b)==1:
        print(i)
        break
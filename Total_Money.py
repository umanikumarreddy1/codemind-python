t=int(input())
for k in range(t):
    D,d,p,q=map(int,input().split())
    n=D//d
    n2=D%d
    s=0
    for i in range(n):
        s+=(p+i*q)*d
    s+=(p+n*q)*n2
    print(s)
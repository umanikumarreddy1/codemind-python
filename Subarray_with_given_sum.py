t=int(input())
for k in range(t):
    a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    i1=i2=f=0
    for i in range(a):
        s=0
        for j in range(i,a):
            s+=arr[j]
            if s==b:
                i1=i
                i2=j
                f=1
                break
        if f==1:
            break
    if f==1:
        print(i1+1,end=" ")
        print(i2+1)
    else:
        print(-1)
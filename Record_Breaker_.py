t=int(input())
for k in range(t):
    a=int(input())
    arr=list(map(int,input().split()))
    c=0
    for i in range(a):
        if i==0:
            if arr[i]>arr[i+1]:
                c+=1
        elif i==a-1:
            f=0
            for j in range(i):
                if arr[i]>arr[j]:
                    f=1
                else:
                    f=0
                    break
            if f==1:
                c+=1
        else:
            f=0
            for j in range(i):
                if arr[i]>arr[j]:
                    f=1
                else:
                    f=0
                    break
            if f==1:
                if arr[i]>arr[i+1]:
                    c+=1
    if a==1:
        c+=1
    print("Case #",end="")
    print(k+1,end=": ")
    print(c)
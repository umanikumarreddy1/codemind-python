a=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(a):
    c=0
    for j in range(a):
        if i!=j:
            if arr[i]==arr[j]:
                c=1
                break
    if c==1:
        print(arr[i])
        break
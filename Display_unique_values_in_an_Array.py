a=int(input())
arr=[a]
arr=list(map(int,input().split()))
for i in range(a):
    for j in range(a):
        if i!=j:
            if arr[i]==arr[j] and arr[i]!=-1:
                arr[i]=-1
                arr[j]=-1
c=0
for i in arr:
    if i!=-1:
        print(i,end=" ")
        c+=1
if c==0:
    print(-1)
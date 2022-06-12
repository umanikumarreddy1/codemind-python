a=int(input())
arr=list(map(int,input().split()))
b=int(input())
brr=list(map(int,input().split()))
res=[None]
for i in range(a):
    res.insert(brr[i],arr[i])
for i in range(a):
    print(res[i],end=" ")
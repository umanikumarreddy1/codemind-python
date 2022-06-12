a=int(input())
arr=list(map(int,input().split()))
b=int(input())
f=ind=0
for i in range(a):
    if arr[i]==b:
        f=1
        ind=i
        break
if f==1:
    print(ind)
else:
    print(-1)
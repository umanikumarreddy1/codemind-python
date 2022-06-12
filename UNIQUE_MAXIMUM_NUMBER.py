a=int(input())
arr=[a]
arr=list(map(int,input().split()))
c=co=0
ma=0
for i in range(a):
    c=0
    for j in range(a):
        if i!=j:
            if arr[i]==arr[j]:
                c=1
                break
    if c==1:
        continue
    else:
        if ma<arr[i]:
            ma=arr[i]
            co+=1
if co>0:
    print(ma)
else:
    print(-1)
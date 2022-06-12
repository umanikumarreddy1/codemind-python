a,b=map(int,input().split())
arr=list(map(int,input().split()))
c=0
s=0
for i in range(a):
    s=0
    for j in range(i,a):
        s+=arr[j]
        if s==b:
            c+=1
print(c)
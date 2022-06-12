a=int(input())
arr=list(map(int,input().split()))
i1=i2=m=0
for i in range(a):
    zc=oc=0
    for j in range(i,a):
        if arr[j]==0:
            zc+=1
        elif arr[j]==1:
            oc+=1
        if zc==oc:
            if m<j-i:
                m=j-i
                i1=i
                i2=j
if m==0:
    print(-1)
else:
    print(i1,i2)
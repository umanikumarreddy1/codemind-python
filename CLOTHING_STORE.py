a=int(input())
arr=[a]
arr=list(map(int,input().split()))
pairs=0
for i in range(a):
    for j in range(a):
        if i!=j:
            if arr[i]==arr[j] and arr[i]!=-1:
                arr[i]=-1
                arr[j]=-1
                pairs+=1
print(pairs)
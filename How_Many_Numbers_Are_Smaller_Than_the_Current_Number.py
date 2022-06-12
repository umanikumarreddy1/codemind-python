a=int(input())
lst=[a]
lst=list(map(int,input().split()))
c=0
for i in range(a):
    c=0
    for j in range(a):
        if i!=j:
            if lst[i]>lst[j]:
                c+=1
    print(c,end=" ")
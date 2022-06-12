a=int(input())
arr=list(map(int,input().split()))
arr2=list(map(int,input().split()))
c=s1=s2=0
for i in arr:
    if i==-1:
        c+=1
    else:
        s1+=i
for i in arr2:
    if i==-1:
        c+=1
    else:
        s2+=i
if c==2:
    print("Infinite")
else:
    count=0
    for i in range(10000):
        if i+s1==s2:
            count+=1
    print(count)
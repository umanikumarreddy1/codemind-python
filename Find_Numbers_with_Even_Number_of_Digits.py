def nod(a):
    c=0
    while a>0:
        r=a%10
        c+=1
        a//=10
    return c
a=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(a):
    if nod(arr[i])%2==0:
        c+=1
print(c)
a=int(input())
lst=[a]
lst=list(map(int,input().split()))
se=so=0
for i in range(a):
    if i%2==0:
        se+=lst[i]
    else:
        so+=lst[i]
if se==so:
    print("YES")
else:
    print("NO")
    
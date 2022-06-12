a=int(input())
arr=list(map(int,input().split()))
xs=ys=0
for i in range(a):
    if i%2==0:
        xs+=arr[i]
    else:
        ys+=arr[i]
diff=abs(xs-ys)
if diff%4==0:
    print("X")
else:
    print("Y")
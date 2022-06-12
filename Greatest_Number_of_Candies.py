a=int(input())
arr=list(map(int,input().split()))
b=int(input())
ma=0
for i in arr:
    if ma<i:
        ma=i
for i in arr:
    if i+b>=ma:
        print("True",end=" ")
    else:
        print("False",end=" ")
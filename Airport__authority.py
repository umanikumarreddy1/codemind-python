a=int(input())
arr=[]
for i in range(a):
    v=int(input())
    arr.append(v)
we=int(input())
va=0
for i in arr:
    if i>we:
        va+=2
    else:
        va+=1
print(va)
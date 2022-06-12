a=input()
s1=""
for i in a:
    if i.isdigit():
        s1+=i
arr=[]
for i in s1:
    if i not in arr:
        arr.append(i)
ec=0
for i in arr:
    if (ord(i)-48)%2==0:
        ec+=1
if ec>0:
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    miev=arr[len(arr)-1]
    for i in range(len(arr)-1,-1,-1):
        if ((ord(arr[i])-48)%2==0):
            miev=arr[i]
            break
    for i in arr:
        if i!=miev:
            print(i,end="")
    print(miev)
else:
    print(-1)
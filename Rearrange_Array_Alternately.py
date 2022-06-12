t=int(input())
for l in range(t):
    a=int(input())
    arr=list(map(int,input().split()))
    for i in range(a):
        for j in range(a-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    mid=a//2
    if a%2==0:
        for i in range(mid):
            if i<mid-1:
                print(arr[a-i-1],end=" ")
                print(arr[i],end=" ")
            else:
                print(arr[a-i-1],end=" ")
                print(arr[i],end="")
    else:
        for i in range(mid):
            print(arr[a-i-1],end=" ")
            print(arr[i],end=" ")
        print(arr[mid],end="")
    print(""),
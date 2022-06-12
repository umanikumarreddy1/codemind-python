a=input()
arr=list(a.split(","))
for i in arr:
    arr2=list(i.split(":"))
    name=arr2[0]
    num=arr2[1]
    ma='0'
    for i in num:
        if ord(i)>ord(ma):
            if ord(i)-48<=len(name):
                ma=i
    ind=ord(ma)-48
    name10=name*10
    if ma=='0':
        print("X",end="")
    else:
        print(name10[ind-1],end="")
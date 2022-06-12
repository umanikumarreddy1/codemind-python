def cor(a):
    s=str(a)
    if '0' in s:
        return 0
    arr=[]
    for i in s:
        arr.append(i)
    f=1
    for i in range(len(s)-1):
        if ord(arr[i])<ord(arr[i+1]):
            f=1
        else:
            return 0
    return 1
a=int(input())
if a==1:
    for i in range(10):
        print(i,end=" ")
elif a==2:
    for i in range(12,90):
        if cor(i)==1:
            print(i,end=" ")
elif a==3:
    for i in range(123,790):
        if cor(i)==1:
            print(i,end=" ")
elif a==4:
    for i in range(1234,6790):
        if cor(i)==1:
            print(i,end=" ")
elif a==5:
    for i in range(12345,56790):
        if cor(i)==1:
            print(i,end=" ")
elif a==6:
    j=0
    for i in range(123456,456790):
        if cor(i)==1:
            print(i,end=" ")
            if i%10==9:
                i+=j
                j+=1
elif a==7:
    for i in range(1234567,3456790):
        if cor(i)==1:
            print(i,end=" ")
elif a==8:
    i=12345678
    j=0
    while i<23456790:
        print(i,end=" ")
        i+=10**j
        j+=1
elif a==9:
    print(123456789)
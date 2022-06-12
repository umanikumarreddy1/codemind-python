def selfdiv(a):
    temp=a
    flag=0
    while temp>0:
        rem=temp%10
        if rem==0:
            flag=0
            break
        if a%rem==0:
            flag=1
            temp//=10
        else:
            flag=0
            break
    if flag==1:
        return 1
    else:
        return 0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if selfdiv(i)==1:
        print(i,end=" ")
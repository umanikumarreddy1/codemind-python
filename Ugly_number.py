a=int(input())
f=0
if a>0:
    while a>0:
        if a%2==0:
            a//=2
        elif a%3==0:
            a//=3
        elif a%5==0:
            a//=5
        else:
            f=1
            break
    if f==1:
        if a==1:
            print("Ugly Number")
        else:
            print("Not Ugly Number")
    else:
        print("Ugly Number")
else:
    print("Not Ugly Number")
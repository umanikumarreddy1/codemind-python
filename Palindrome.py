def rev(a):
    r=0
    while (a>0):
        rem=a%10
        r=(r*10)+rem
        a//=10
    return r
a=int(input())
if (a==rev(a)):
    print("True")
else:
    print("False")

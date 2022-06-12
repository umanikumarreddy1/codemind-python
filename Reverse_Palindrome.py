def rev(a):
    r=0
    while a>0:
        rem=a%10
        r=(r*10)+rem
        a//=10
    return r
a=int(input())
a=a+rev(a)
while True:
    if a==rev(a):
        break
    else:
        a=a+rev(a)
print(a)
def fact(a):
    f=1
    for i in range(1,a+1):
        f*=i
    return f
a=int(input())
sum=0
temp=a
while (temp>0):
    r=temp%10
    sum+=fact(r)
    temp//=10
if sum==a:
    print("The number",a,"is a strong number")
else:
    print("The number",a,"is not a strong number")
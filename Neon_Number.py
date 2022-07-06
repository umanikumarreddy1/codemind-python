#20-->400 sum=4
n=int(input())
m=n**2
s=0
while m:
    a=m%10
    m=m//10
    s+=a
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")
    
    
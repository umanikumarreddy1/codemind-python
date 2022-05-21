n=int(input())
rev=0
while(n):
    r=n%10
    rev=rev*10+r
    n//=10
print(rev)
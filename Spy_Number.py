##=-45-->9  20-->22 4 3
n=int(input())
s=0
p=1

while n:
    a=n%10
    n=n//10
    s=s+a
    p=p*a
if(s==p):
    print("Spy Number")
else:
    print("Not Spy Number")


















n=int(input())
c=[]
while n:
    a=n%10 
    n=n//10
    c.append(a)
c=c[::-1]
for i in range(0,len(c)):
    if c[i]==6:
        c[i]=9
        break
for i in c:
    print(i,end='')
    
    
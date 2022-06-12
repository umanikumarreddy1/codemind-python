s=input()
b=int(input())
c=ac=count=0
c=len(s)
for i in s:
    if i=='a':
        ac+=1
l=b//c
k=b%c
count=l*ac
for i in range(k):
    if s[i]=='a':
        count+=1
print(count)
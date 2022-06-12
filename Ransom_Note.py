a=input()
s1,s2=a.split()
s2arr=[]
for i in s2:
    s2arr.append(i)
f=0
for i in s1:
    if i in s2arr:
        f=1
        s2arr.remove(i)
    else:
        f=0
        break
if f==1:
    print("True")
else:
    print("False")
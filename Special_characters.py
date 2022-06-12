a=input()
s1=""
spch="!@#$%^&*()_+-?><:{}[]\|.,/"
c=0
for i in a:
    if i in spch:
        c+=1
for i in a:
    if i.isdigit():
        s1+=i
arr=list(s1)
ev=[]
od=[]
for i in arr:
    if (ord(i)-48)%2==0:
        ev.append(i)
    else:
        od.append(i)
if c%2==0:
    for i in range(max(len(ev),len(od))):
        if i<len(ev):
            print(ev[i],end="")
        if i<len(od):
            print(od[i],end="")
else:
    for i in range(max(len(ev),len(od))):
        if i<len(od):
            print(od[i],end="")
        if i<len(ev):
            print(ev[i],end="")
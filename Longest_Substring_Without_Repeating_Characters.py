def wrc(s):
    s1=""
    for i in s:
        s1+=i.lower()
    arr=[]
    f=0
    for i in s1:
        arr.append(i)
    for i in arr:
        c=0
        for j in arr:
            if i==j:
                c+=1
        if c==1:
            f=1
        else:
            f=0
            break
    if f==1:
        return 1
    else:
        return 0
a=input()
mas=""
ma=0
for i in range(len(a)):
    s=""
    for j in range(i,len(a)):
        s+=a[j]
        if wrc(s)==1:
            if s in a:
                if len(s)>ma:
                    mas=s
                    ma=len(mas)
if ma==0:
    print(-1)
elif ma<3:
    print(-1)
else:
    print(mas)
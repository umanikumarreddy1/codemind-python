a=input()
arr=list(a)
sss=[]
if len(a)==1:
    print(a)
elif len(a)==2:
    for i in range(len(a)):
        for j in range(len(a)):
            if i!=j:
                s=""
                s+=arr[i]+arr[j]
                sss.append(s)
elif len(a)==3:
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                if i!=j and i!=k and j!=k:
                    s=""
                    s+=arr[i]+arr[j]+arr[k]
                    sss.append(s)
elif len(a)==4:
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                for l in range(len(a)):
                    if i!=j and i!=k and j!=k and k!=l and i!=l and j!=l:
                        s=""
                        s+=arr[i]+arr[j]+arr[k]+arr[l]
                        sss.append(s)
for i in sss:
    print(i)
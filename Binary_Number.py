def dec_bin(a):
    s=""
    while a>0:
        r=a%2
        s+=str(r)
        a//=2
    return s[::-1]
a=int(input())
for i in range(2**a):
    s=dec_bin(i)
    if len(s)!=a:
        for j in range(a-len(s)):
            print("0",end="")
        print(s)
    else:
        print(s)
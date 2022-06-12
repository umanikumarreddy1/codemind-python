a=input()
for i in a:
    if (ord(i)-48)%2==0:
        continue
    else:
        print((ord(i)-48)*(ord(i)-48),end="")
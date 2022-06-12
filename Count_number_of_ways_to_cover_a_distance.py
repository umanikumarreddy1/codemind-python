def now(a):
    if a<=0:
        return 0
    if a==1:
        return 1
    if a==2:
        return 2
    if a==3:
        return 4
    return now(a-1)+now(a-2)+now(a-3)
a=int(input())
print(now(a))
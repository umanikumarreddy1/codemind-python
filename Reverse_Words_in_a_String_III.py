def reverse(s):
    s1=""
    for i in range(len(s)-1,-1,-1):
        s1+=s[i]
    return s1
a=input()
arr=list(a.split())
for i in arr:
    print(reverse(i),end=" ")
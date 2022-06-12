a=int(input())
arr=[]
fa=fb=2
fn=0
for i in range(a):
    arr.append(fa)
    fn=fa+fb
    fa=fb
    fb=fn
print(arr[a-1])
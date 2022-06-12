a=int(input())
fa=0
fb=1
fn=fa+fb
for i in range(a):
    print(fa,end=" ")
    fn=fa+fb
    fa=fb
    fb=fn
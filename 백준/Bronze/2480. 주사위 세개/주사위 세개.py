a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

if a==b==c :
    r=10000+a*1000
elif a==b :
    r=1000+a*100
elif b==c :
    r=1000+b*100
elif a==c :
    r=1000+a*100
else:
    d=0
    if d<a:
        d=a
    if d<b:
        d=b
    if d<c:
        d=c
    r=d*100

print(r)
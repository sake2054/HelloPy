a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a <= b and a <= c :
    r1 = a
elif b <= a and b <= c :
    r1 = b
elif c <= a and c <= b :
    r1 = c

if d <= e :
    r2 = d
elif e <= d :
    r2 = e

print(r1 + r2 - 50)
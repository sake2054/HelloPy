a,b,c,d,e = input().split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)

a = a ** 2
b = b ** 2
c = c ** 2
d = d ** 2
e = e ** 2

f = a+b+c+d+e
f = f % 10

print(f)
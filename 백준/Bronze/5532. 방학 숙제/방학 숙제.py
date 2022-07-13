l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % c == 0 :
    e = a // c
else :
    e = a // c + 1

if b % d == 0 :
    f = b // d
else :
    f = b // d + 1

if e >= f :
    print(l - e)
else :
    print(l - f)

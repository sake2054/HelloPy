n = int(input())
d = n
o = 0
while True:
    o += 1
    a = d // 10
    b = d % 10
    c = a + b
    d = b * 10 + c % 10
    if d == n:
        break
print(o)
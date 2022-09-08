ht,mt = input().split()
t = int(input())

h = int(ht)
m = int(mt)

m = m + t

if m < 60 :
    pass
else :
    while m >= 60 :
        m = m - 60
        h = h + 1
    if h >= 24 :
        h = h % 24

print(f'{h} {m}')
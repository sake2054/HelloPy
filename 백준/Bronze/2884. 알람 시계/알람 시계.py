ht,mt = input().split()
h = int(ht)
m = int(mt)

if m - 45 >= 0 :
    m = m - 45
else :
    m = m + 15
    h = h - 1

if h >= 0 :
    pass
else :
    h = h + 24

print(f'{h} {m}')
n = int(input())
l = []
for _ in range(n):
    l.append(str(input()))
for x in range(1, len(l[0])+1):
    r = []
    for y in range(n):
        if l[y][-x:] in r:
            break
        else:
            r.append(l[y][-x:])
    if len(r) == n:
        print(x)
        break
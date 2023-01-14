i = input().lower()
a = list(set(i))
b = []
for x in a:
    c = i.count(x)
    b.append(c)
if b.count(max(b)) >= 2:
    print("?")
else:
    print(a[b.index(max(b))].upper())
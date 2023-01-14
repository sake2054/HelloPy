o = []
for i in range(0,10):
    a = int(input()) % 42
    if a not in o:
        o.append(a)
print(len(o))
a = {"P":13, "K":13, "H":13, "T":13}
i = input()
l = []
for x in range(0,len(i)-2,3):
    l.append(i[x:x+3])

if len(set(l)) != len(l):
    print("GRESKA")
    exit(0)
else:
    for y in l:
        a[y[0]] += -1
    print(a["P"], a["K"], a["H"], a["T"])
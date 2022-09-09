a = int(input())

for i in range(0, a):
    r = 0
    o = 0
    q = input()
    l = len(q)
    for j in range(0, l):
        if q[j] == "O" :
            r += 1
            o += r
        else :
            r = 0
    print(o)
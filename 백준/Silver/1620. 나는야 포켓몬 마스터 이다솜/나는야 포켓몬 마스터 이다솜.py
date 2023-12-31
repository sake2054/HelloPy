import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
d1 = {}
d2 = {}
for x in range(n):
    a = sys.stdin.readline().rstrip()
    d1[x+1] = a
    d2[a] = x+1
for y in range(m):
    q = sys.stdin.readline().rstrip()
    if q.isdigit():
        q = int(q)
        print(d1[q])
    else:
        print(d2[q])
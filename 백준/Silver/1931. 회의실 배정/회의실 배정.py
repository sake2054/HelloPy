import sys
input = sys.stdin.readline
o = 0
n = int(input().strip())
t = []
for i in range(n):
    i1, i2 = map(int, input().strip().split())
    t.append([i1, i2])
t = sorted(t, key = lambda x : x[0])
t = sorted(t, key = lambda x : x[1])
i3 = 0
for i1, i2 in t:
    if i1 >= i3:
        o += 1
        i3 = i2
print(o)
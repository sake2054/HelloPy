import sys

n, s = map(str, sys.stdin.readline().strip().split())
o = 0
n = int(n)
for x in range(n):
    i, j = map(str, sys.stdin.readline().strip().split())
    if i == s or "_" + s + "_" in i or i.startswith(s + "_") or i.endswith("_" + s):
        o += int(j)
print(o)
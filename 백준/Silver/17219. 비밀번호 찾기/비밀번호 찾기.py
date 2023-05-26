import sys

n, m = map(int, sys.stdin.readline().split())
a = {}

for x in range(0, n):
    b, c = sys.stdin.readline().split()
    a[b] = c

for y in range(0, m):
    print(a[sys.stdin.readline().strip()])
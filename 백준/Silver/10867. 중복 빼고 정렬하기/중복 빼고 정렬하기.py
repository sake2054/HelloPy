import sys
input = sys.stdin.readline
a = int(input().strip())
l = list(map(int, input().strip().split()))
s = set(l)
l = list(s)
l.sort()
print(*l)
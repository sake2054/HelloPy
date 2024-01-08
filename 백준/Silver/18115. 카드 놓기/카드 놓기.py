import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
l = list(map(int, sys.stdin.readline().rstrip().split()))
l.reverse()
o = deque()
for i in range(n):
    if l[i] == 1:
        o.appendleft(i+1)
    elif l[i] == 2:
        o.insert(1, i+1)
    elif l[i] == 3:
        o.append(i+1)
print(*o)
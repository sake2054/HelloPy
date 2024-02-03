import sys
import math
input = sys.stdin.readline
n = int(input().strip())
a = list(map(int, input().strip().split()))
o, p = 0, 0
for i in range(n):
    if i == 0:
        p = 1
    elif a[i] > a[i-1]:
        p += 1
    else:
        o += p * (p + 1) // 2
        p = 1
print(o+ (p * (p + 1) // 2))
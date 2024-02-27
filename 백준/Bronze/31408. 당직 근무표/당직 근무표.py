from collections import Counter
import math

n = int(input())
a = list(map(int, input().split()))
b = dict(Counter(a))
c = []
for x in b.values():
    c.append(x)
if max(c) > math.ceil(n/2):
    print("NO")
else:
    print("YES")
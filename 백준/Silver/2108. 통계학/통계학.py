import sys
from collections import Counter
n = int(sys.stdin.readline())
l = []
o = []
for x in range(0, n):
    l.append(int(sys.stdin.readline()))
o.append(round(sum(l)/n))
l.sort()
o.append(l[n//2])
c = Counter(l).most_common()
if len(c) > 1 and c[0][1]== c[1][1]:
    o.append(c[1][0])
else:
    o.append(c[0][0])
o.append(max(l)-min(l))
for y in range(0, 4):
    print(o[y])
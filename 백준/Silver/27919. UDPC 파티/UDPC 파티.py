import sys
i = sys.stdin.readline().strip()
o = ''

u = i.count('U')
d = i.count('D')
p = i.count('P')
c = i.count('C')

if u + c > (d + p + 1) / 2:
    o += 'U'
if d + p > 0:
    o += 'DP'
print(o)
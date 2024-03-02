import sys

s = sys.stdin.readline().strip()
s = s.split('-')
o = 0
for x in s[0].split('+'):
    o += int(x)
for y in s[1:]:
    for z in y.split('+'):
        o -= int(z)
print(o)
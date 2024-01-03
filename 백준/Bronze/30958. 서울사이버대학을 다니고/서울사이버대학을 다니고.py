import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()
o = 0
for x in range(26):
    if s.count(chr(ord('a')+x)) > o:
        o = s.count(chr(ord('a')+x))
print(o)
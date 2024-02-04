import sys
input = sys.stdin.readline
n = int(input().strip())
o = abs(100 - n)
M = int(input().strip())
if M == 0:
    x = set()
else:
    x = set(input().strip().split())
for i in range(1000001): 
    for N in str(i):
        if N in x:
            break
    else:
        o = min(o, len(str(i)) + abs(i - n))
print(o)
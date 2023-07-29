import sys

n = int(sys.stdin.readline().rstrip())
d = 0
p = 0
for _ in range(0, n):
    a = sys.stdin.readline().rstrip()
    if a == 'D':
        d += 1
    else:
        p += 1

    if d - p > 1 or p - d > 1:
        print(f'{d}:{p}')
        break
else:
    print(f'{d}:{p}')
import sys

t = int(sys.stdin.readline().strip())
for _ in range(0, t):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    if n == 0:
        a = sys.stdin.readline().strip()
        a = []
    else:
        a = sys.stdin.readline().strip()[1:-1].split(',')
    b = 0
    e = 0
    for x in range(0, len(p)):
        if p[x] == 'R':
            b = (b + 1) % 2
        else:
            if len(a) == 0:
                e = 1
                break
            if b == 0:
                del a[0]
            else:
                del a[-1]
    if b == 1:
        a.reverse()
    if len(a) != 0:
        for y in range(0, len(a)):
            if y == 0:
                print('[', end='')
            print(a[y], end='')
            if y == len(a) - 1:
                print(']')
            else:
                print(',', end='')
    elif e == 1:
        print('error')
    else:
        print('[]')
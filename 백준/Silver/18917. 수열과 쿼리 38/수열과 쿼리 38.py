import sys
m = int(sys.stdin.readline())
s = 0
x = 0
for i in range(0, m):
    q = list(map(int, sys.stdin.readline().split()))
    if q[0] == 1:
        s += q[1]
        x = x^q[1]
    elif q[0] == 2:
        s += -q[1]
        x = x^q[1]
    elif q[0] == 3:
        print(s)
    elif q[0] == 4:
        print(x)
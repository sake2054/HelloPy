n = int(input())
for x in range(1, n):
    print(' ' * ( n - x ) + '*' * ( 2 * x - 1 ))
for x in range(n, 0, -1):
    print(' ' * ( n - x ) + '*' * ( 2 * x - 1 ))
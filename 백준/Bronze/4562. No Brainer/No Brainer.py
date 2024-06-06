n = int(input())
for x in range(n):
    x, y = map(int, input().split())
    if x >= y:
        print('MMM BRAINS')
    else:
        print('NO BRAINS')
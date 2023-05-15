a, b = map(int, input().split())
c = list(map(int, input().split()))
d = a * b
for x in range(0, len(c)):
    print(c[x] - d, end=' ')
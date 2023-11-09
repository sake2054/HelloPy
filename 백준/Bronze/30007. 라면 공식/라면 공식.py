n = int(input())
for x in range(n):
    a, b, x = map(int, input().split())
    print(b + a * (x-1))
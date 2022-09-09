a = int(input())
b = list(map(int, input().split()))
b.sort()

print(f'{b[0]} {b[a-1]}')
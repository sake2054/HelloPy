t = int(input())

for j in range(0,t):
    c = int(input())
    q = c // 25
    d = (c % 25) // 10
    n = (c % 25 % 10) // 5
    p = c % 5
    print(f'{q} {d} {n} {p}')
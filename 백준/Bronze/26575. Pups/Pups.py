n = int(input())
for _ in range(n):
    d, f, p= map(float, input().split())
    o = d*f*p
    print(f'${o:.2f}')
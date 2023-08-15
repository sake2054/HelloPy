n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
q = int(input())
for _ in range(q):
    p = list(map(int, input().split()))
    if p[0] == 1:
        a = m[p[1]-1][n-1]
        del m[p[1]-1][n-1]
        m[p[1]-1].insert(0, a)
    elif p[0] == 2:
        k = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                k[c][n-1-r] = m[r][c]
        m = k
print('\n'.join([' '.join(map(str, m[i])) for i in range(n)]))
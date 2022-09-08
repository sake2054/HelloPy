n, t = list(map(int, input().split()))
w = list(map(int, input().split()))
a = 0
b = 0

for i in range(0, n):
    if a + w[i] > t :
        break
    else :
        a += w[i]
        b += 1

print(b)
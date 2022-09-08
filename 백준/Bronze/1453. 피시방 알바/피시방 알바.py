a = []
b = 0
n = int(input())
m = list(map(int, input().split()))

for i in range(0, n):
    if a.count(m[i]) == 0 :
        a.append(m[i])
    else :
        b += 1
print(b)
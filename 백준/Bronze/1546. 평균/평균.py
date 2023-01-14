n = int(input())
i = list(map(int, input().split()))
m = max(i)
a = []
for x in i:
    a.append(x/m*100)
o = sum(a)/n
print(o)
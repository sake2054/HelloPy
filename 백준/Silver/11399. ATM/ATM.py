n = int(input())
i = list(map(int, input().split()))
o = 0

i.sort()
for x in range(0, n):
    o += sum(i[0:x+1])
print(o)
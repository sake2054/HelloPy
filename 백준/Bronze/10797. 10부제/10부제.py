a = int(input())
i = input().split()

s = 0
o = 0

while s < 5:
    s += 1
    if int(i[s-1]) == a :
        o += 1

print(o)
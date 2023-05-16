n = int(input())
o = 0
for x in range(n):
    a = int(input()[2:])
    if a <= 90:
        o += 1
print(o)
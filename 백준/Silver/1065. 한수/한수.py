n = int(input())
o = 0

for i in range(1, n+1):
    if i <= 99:
        o += 1
    else:
        s = str(i)
        if int(s[0]) - int(s[1]) == int(s[1]) - int(s[2]):
            o += 1
print(o)
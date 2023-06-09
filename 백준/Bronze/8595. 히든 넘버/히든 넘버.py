n = int(input())
i = input()
o = 0
t = ""
for x in range(0, n):
    if i[x].isdigit():
        t += i[x]
    else:
        if t != "":
            o += int(t)
            t = ""
    if x == n - 1 and t != "":
        o += int(t)
print(o)
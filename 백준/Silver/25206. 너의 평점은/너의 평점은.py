grade = {"A+" : 4.5, "A0" : 4,"B+" : 3.5, "B0" : 3, "C+" : 2.5, "C0" : 2, "D+" : 1.5, "D0" : 1, "F" : 0}
t = 0
o = 0

for i in range(0, 20):
    a, b, c = input().split()
    if c == "P" :
        pass
    else :
        b = round(float(b))
        t += int(b)
        o += int(b) * grade[c]
o = o / t
print(o)
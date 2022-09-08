amt = int(input())
grade = {"A+" : 4.3, "A0" : 4, "A-" : 3.7, "B+" : 3.3, "B0" : 3, "B-" : 2.7, "C+" : 2.3, "C0" : 2, "C-" : 1.7, "D+" : 1.3, "D0" : 1, "D-" : 0.7, "F" : 0}
o = 0
t = 0

for i in range(0, amt):
    a, b, c= input().split()
    t += int(b)
    o += int(b) * grade[c]
o = o / t
o = o * 1000
if o % 10 >= 5 :
    o += 10 - o % 10
o = o / 1000
print(f"{o:.2f}")
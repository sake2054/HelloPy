now = input().split()
h = int(now[0])
m = int(now[1])
s = int(now[2])
t = int(input())

h += t // 3600
m += (t % 3600) // 60
s += t % 60

while s >= 60 :
    s += -60
    m += 1
while m >= 60 :
    m += -60
    h += 1
while h >= 24 :
    h += -24
print(f"{h} {m} {s}")
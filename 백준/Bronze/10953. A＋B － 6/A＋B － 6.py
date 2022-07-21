t = int(input())

s = 0
while s < t:
    s += 1
    i=input()
    i=i.split(",")
    o=int(i[0])+int(i[1])
    print(o)
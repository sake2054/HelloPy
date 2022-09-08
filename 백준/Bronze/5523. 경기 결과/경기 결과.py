t = int(input())

a = 0
b = 0

s = 0
while s < t:
    s += 1
    i=input()
    i=i.split()
    if int(i[0]) > int(i[1]) :
        a += 1
    elif int(i[1]) > int(i[0]) :
        b += 1

print(f"{a} {b}")
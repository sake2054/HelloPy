t = int(input())
a = 0
i = 0
j = input().split()

for i in range(0, t) :
    if i+1 != int(j[i]) :
        a += 1

print(a)
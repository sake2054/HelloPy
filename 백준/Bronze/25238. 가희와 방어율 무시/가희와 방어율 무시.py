i = input().split(" ")
a = int(i[0])
b = int(i[1]) / 100

c = a - (a * b)

if c >= 100 :
    print(0)
else :
    print(1)

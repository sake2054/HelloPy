n = int(input())
i = input()

j = 0
o = i[0]
while True:
    j += 1
    try:
        tmp = i[j*n]
    except:
        break
    o = o + tmp
print(o)
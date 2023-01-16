i = list(map(int, input().split()))
o = min(i[0], i[1], i[2]-i[0], i[3]-i[1])
print(o)
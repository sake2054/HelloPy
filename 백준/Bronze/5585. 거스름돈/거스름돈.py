i = 1000 - int(input())
o = 0
coinType = [500, 100, 50, 10, 5, 1]

for coin in coinType:
    o += i // coin
    i %= coin

print(o)
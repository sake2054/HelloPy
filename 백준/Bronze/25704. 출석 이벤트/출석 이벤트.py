n = int(input())
p = int(input())
if n >= 20:
    o = p * 0.75
    if p - 2000 <= o:
        o = p - 2000
elif n >= 15:
    o = p * 0.9
    if p - 2000 <= o:
        o = p - 2000
elif n >= 10:
    o = p * 0.9
    if p - 500 <= o:
        o = p - 500
elif n >= 5:
    o = p - 500
else:
    o = p
if o <= 0:
    o = 0
print(int(o))
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

while True:
    a2 += b1 * -1
    b2 += a1 * -1
    if a2 <= 0 or b2 <= 0 :
        break
if a2 <= 0 and b2 > 0 :
    print("PLAYER B")
elif b2 <= 0 and a2 > 0 :
    print("PLAYER A")
elif a2 <= 0 and b2 <= 0 :
    print("DRAW")
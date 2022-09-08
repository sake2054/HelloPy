t = int(input())

for j in range(0,t):
    i = input()
    g1 = i.count('g')
    g2 = i.count('G')
    b1 = i.count('b')
    b2 = i.count('B')
    g = g1 + g2
    b = b1 + b2
    
    if g > b:
        print(f'{i} is GOOD')
    elif g < b:
        print(f'{i} is A BADDY')
    else:
        print(f'{i} is NEUTRAL')

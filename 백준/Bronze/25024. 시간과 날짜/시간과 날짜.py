t = int(input())

s = 0
while s < t:
    s += 1
    i=input()
    i=i.split(' ')
    a=int(i[0])
    b=int(i[1])
    
    if a <= 23 and b <= 59:
        o1 = "Yes"
    else:
        o1 = "No"
    
    if a in [1, 3, 5, 7, 8, 10, 12] and b <= 31 and b > 0:
        o2 = "Yes"
    elif a in [4, 6, 9, 11] and b <= 30 and b > 0:
        o2 = "Yes"
    elif a == 2 and b <= 29 and b > 0:
        o2 = "Yes"
    else:
        o2 = "No"
    
    print(f'{o1} {o2}')
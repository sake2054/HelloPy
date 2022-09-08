n = int(input())
r = input()

a = r.count("A")
b = r.count("B")

if a > b :
    print("A")
elif b > a :
    print("B")
else :
    print("Tie")

i = input()
o = 1

a = i.find("U")
if a == -1 :
    o = 0
i = i[a+1:]
a = i.find("C")
if a == -1 :
    o = 0
i = i[a+1:]
a = i.find("P")
if a == -1 :
    o = 0
i = i[a+1:]
a = i.find("C")
if a == -1 :
    o = 0
if o != 0 :
    o = 1
if o == 0 :
    print("I hate UCPC")
elif o == 1 :
    print("I love UCPC")
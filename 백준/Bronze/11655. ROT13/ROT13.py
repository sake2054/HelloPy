i = input()
o = ""
for a in range(len(i)):
    if i[a] == " " or ord(i[a]) < ord("A") :
        o += i[a]
    else:
        if ord(i[a]) + 13 > 122:
            o += chr(96 + (ord(i[a]) + 13) - 122)
        elif ord(i[a]) + 13 > 90 and ord(i[a]) < 91:
            o += chr(64 + (ord(i[a]) + 13) - 90)
        else:
            o += chr(ord(i[a]) + 13)
print(o)
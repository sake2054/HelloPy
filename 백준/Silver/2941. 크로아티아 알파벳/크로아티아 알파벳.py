rep = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
i = input()
for x in range(0, 8):
    i = i.replace(rep[x], '0')
print(len(i))
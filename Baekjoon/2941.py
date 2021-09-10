# 크로아티아 알파벳
a = input()
b = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')
for c in b:
    a = a.replace(c, 'A')
print(len(a))

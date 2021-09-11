# 다이얼
a = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
print(sum(a.index(_) + 3 for n in input() for _ in a if n in _))

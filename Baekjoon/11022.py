# A+B - 8
import sys
_ = input()
for i, l in enumerate(sys.stdin, 1):
    l = [int(_) for _ in l.split()]
    print(f'Case #{i}: {l[0]} + {l[1]} = {sum(l)}')

# A+B - 7
import sys
_ = input()
for i, l in enumerate(sys.stdin, 1):
    print(f'Case #{i}: {sum(int(_) for _ in l.split())}')

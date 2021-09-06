# A+B - 7
import sys
_ = input()
print(*(f'Case #{i}: {sum(map(int, l.split()))}' for i,
      l in enumerate(sys.stdin, 1)))

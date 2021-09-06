# A+B - 8
import sys


def print_case(i, a, b):
    print(f'Case #{i}: {a} + {b} = {a + b}')


_ = input()
for i, l in enumerate(sys.stdin, 1):
    a, b = map(int, l.split())
    print_case(i, a, b)

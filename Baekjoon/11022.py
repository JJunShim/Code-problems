# A+B - 8
import sys
def print_case(i, a, b):
    print(f'Case #{i}: {a} + {b} = {a + b}')
for i in range(1, int(input()) + 1):
    a, b = map(int, sys.stdin.readline().split())
    print_case(i, a, b)

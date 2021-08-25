# A+B - 7
import sys
def print_case(i, res):
    print(f'Case #{i}: {res}')

n = int(input()) + 1
for i in range(1, n):
    print_case(i, sum(map(int, sys.stdin.readline().split())))

# A+B - 5
import sys
while True:
    a, b = map(int, sys.stdin.readline().split())
    if not (a and b):
        break
    print(a + b)

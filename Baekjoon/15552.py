# 빠른 A+B
import sys
_ = input()
for l in sys.stdin:
    print(sum(int(_) for _ in l.split()))

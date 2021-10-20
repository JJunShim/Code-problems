# 직각삼각형
import sys
for l in sys.stdin:
    a = sorted(pow(int(s), 2) for s in l.split())
    if any(a):
        print('right' if a[-1] == sum(a[:-1]) else 'wrong')

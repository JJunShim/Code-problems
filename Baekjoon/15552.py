# 빠른 A+B
import sys
_ = input()
print(*(sum(map(int, l.split())) for l in sys.stdin))

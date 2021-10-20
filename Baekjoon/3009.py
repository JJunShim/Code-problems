# 네 번째 점
import sys
a = [], []
for l in sys.stdin:
    for i, v in enumerate(map(int, l.split())):
        if v in a[i]:
            a[i].remove(v)
        else:
            a[i].append(v)
print(*a[0], *a[1])

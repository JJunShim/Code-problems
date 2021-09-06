# 최댓값
from math import prod
a = [0] * 10
for k in str(prod((int(input()) for _ in range(3)))):
    a[int(k)] += 1
print(*a)

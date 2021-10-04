# 숫자의 개수
import math
n = math.prod(int(input()) for _ in range(3))
a = [0] * 10
while n:
    n, r = divmod(n, 10)
    a[r] += 1
print(*a)

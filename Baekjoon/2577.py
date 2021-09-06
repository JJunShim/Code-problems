# 숫자의 개수
from math import prod
a = str(prod((int(input()) for _ in range(3))))
print(*{k: a.count(str(k)) for k in range(10)}.values())

# 평균
n = int(input())
a = [int(_) for _ in input().split()]
m = max(a)
print(sum((_ / m * 100 for _ in a)) / n)
